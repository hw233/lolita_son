# coding: utf-8
# 
import app.base.game_module_mgr
from app.core.game_event_def import *
from app.protocol.ProtocolDesc import *
import app.protocol.netutil as netutil
from twisted.python import log
import app.util.helper as helper
import app.util.lang_config as lang_config
import app.game.memmode as memmode
from firefly.server.globalobject import GlobalObject
import app.core.game_module_def as game_module_def
import app.config.item
import app.config.itemmerge
import app.config.itemtype
import app.base.utils

ITEM_EQUIP = 1
ITEM_ADDEXP = 2
ITEM_ADDGOLD = 3
class item_main(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(item_main,self).__init__();
		self.game_ins = None;
		self.item_type_2_id = {};
		return
	def start(self):
		super(item_main,self).start();
		self.register_net_event(C2S_ITEM_GETLIST,self.on_get_itemlist);
		self.register_net_event(C2S_ITEM_USE,self.on_itemuse);
		self.register_net_event(C2S_ITEM_MOVE,self.on_itemmove);
		self.register_net_event(C2S_ITEM_BUY,self.on_itembuy);
		self.game_ins = self.get_module(game_module_def.GAME_MAIN);
		for k,v in app.config.itemtype.itemtype_map.items():
			tp = v["tp"];
			self.item_type_2_id[tp] = k;
		return

	def _gen_senditemdata(self,id,shape,used,pos):
		ret = {};
		ret['id'] = id;
		ret['sid'] = shape;
		ret['key'] = used;
		ret['pos'] = pos;
		ret['amount'] = 1;
		ret['quality'] = 0;
		ret['extra'] = 0;
		ret['battle'] = 0;
		return ret;
	def _get_itemlist_by_cId(self,cId):
		itemlist = memmode.tb_item_admin.getAllPkByFk(cId)
		itemobjlist = memmode.tb_item_admin.getObjList(itemlist)
		return itemobjlist
	def _get_result_merge(self,srcshape,dstshape):
		for k,v in app.config.itemmerge.itemmerge_map.items():
			s1 = v['src1'];
			s2 = v['src2'];
			r = v['shape'];
			if srcshape == s1 and dstshape == s2:
				return r;
			if srcshape == s2 and dstshape == s1:
				return r;
		return None;
	def _delitem(self,dId,cId,itemid):
		srcitemobj = memmode.tb_item_admin.getObj(itemid);
		if not srcitemobj:
			return False;
		memmode.tb_item_admin.deleteMode(itemid);
		return True;
	def _send_delitem_netpack(self,dId,cId,itemid):
		send_data = {};
		send_data['id'] = itemid;
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_ITEM_DEL,cId,send_data]);
		return
	def _mergeitem(self,dId,cId,srcid,dstid):
		if srcid == dstid:
			return

		srcitemobj = memmode.tb_item_admin.getObj(srcid);
		if not srcitemobj:
			return;
		srcitemdata = srcitemobj.get('data');
		dstitemobj = memmode.tb_item_admin.getObj(dstid);
		if not dstitemobj:
			return;
		dstitemdata = dstitemobj.get('data');
		srcshape = srcitemdata['shape'];
		dstshape = dstitemdata['shape'];
		result = self._get_result_merge(srcshape,dstshape);
		if not result:
			return;
		if self._delitem(dId,cId,srcid):
			self._send_delitem_netpack(dId,cId,srcid);
		if self._delitem(dId,cId,dstid):
			self._send_delitem_netpack(dId,cId,dstid);

		addpos = self._getemptyslot(cId);
		addid = self._additem(result,cId,0,addpos);
		if addid != 0:
			self._send_additem_netpack(addid,dId,cId);
		return

	
	def _getemptyslot(self,cId):
		itemlist = self._get_itemlist_by_cId(cId);
		pos_map = {};
		for itemobj in itemlist:
			idata = itemobj.get('data');
			pos = idata['pos'];
			pos_map[pos] = pos;
		start_pos = 0;
		while(True):
			if pos_map.has_key(start_pos):
				start_pos = start_pos + 1;
			else:
				break;
		return start_pos;
	def _additem(self,shape,cId,used,pos):
		itemc = app.config.item.create_Item(shape);
		if not itemc:
			return 0;
		data = {};
		data['characterId'] = cId;
		data['used'] = used;
		data['shape'] = shape;
		data['pos'] = pos;
		log.msg("_additem incry id:%s %s"%(memmode.tb_item_admin.get("_incrvalue"),memmode.tb_item_admin._incrkey));
		newitemmode = memmode.tb_item_admin.new(data);
		new_data = newitemmode.get('data');
		itemId = new_data['id'];
		log.msg("_additem %s %s %s %s"%(memmode.tb_item_admin.get("_incrvalue"),(new_data),newitemmode.id,str(newitemmode.data)));
		return itemId
	def _send_additem_netpack(self,itemid,dId,cId):
		itemdata = memmode.tb_item_admin.getObj(itemid);
		if not itemdata:
			return
		iteminfo = itemdata.get('data');
		if not iteminfo:
			return
		send_data = {};
		send_data['item'] = self._gen_senditemdata(itemid,iteminfo['shape'],iteminfo['used'],iteminfo['pos']);
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_ITEM_ADD,cId,send_data]);
		return

	def _use_item_func(self,dId,cId,itemc):
		if self.item_type_2_id.has_key(itemc.tp):
			if self.item_type_2_id[itemc.tp] == ITEM_ADDEXP:
				count = app.base.utils._str2int(itemc.d1);
				if count > 0:
					self.fire_event(EVENT_ADDEXP2PLAYER,[cId,count]);
			elif self.item_type_2_id[itemc.tp] == ITEM_ADDGOLD:
				count = app.base.utils._str2int(itemc.d1);
				if count > 0:
					self.fire_event(EVENT_ADDGOLD2PLAYER,[cId,count]);
		return
	def on_get_itemlist(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		if not self.game_ins._is_cId_valid(cId):
			return
		send_list = [];
		itemlist = self._get_itemlist_by_cId(cId);
		for itemobj in itemlist:
			idata = itemobj.get('data');
			id = idata['id'];
			sid = idata['shape'];
			key = idata['used']
			pos = idata['pos'];
			send_list.append(self._gen_senditemdata(id,sid,key,pos));
			
		send_data = {};
		send_data['items'] = send_list;
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_ITEM_LIST,cId,send_data]);
		return
	def on_itemuse(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		if not self.game_ins._is_cId_valid(cId):
			return
		data = ud["data"];
		c_data = data;
		itemid = c_data["id"];
		amount = c_data["amount"];

		roledata = memmode.tb_character_admin.getObj(cId);
		if not roledata:
			return
		roleinfo = roledata.get('data');
		if not roleinfo:
			return
		plv = roleinfo["level"];

		itemobj = memmode.tb_item_admin.getObj(itemid);
		if not itemobj:
			return;
		itemdata = itemobj.get('data');
		if not itemdata:
			return;
		shape = itemdata['shape'];
		itemc = app.config.item.create_Item(shape);
		if not itemc:
			return
		reqlv = itemc.reqlv;
		if reqlv > plv:
			self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_NOTIFY_FLOAT,cId,{'msg':lang_config.LANG_NOTENOUGHLV}]);
			return
		###todo
		self._use_item_func(dId,cId,itemc);
		###end todo
		if self._delitem(dId,cId,itemid):
			self._send_delitem_netpack(dId,cId,itemid);
		return
	def on_itemmove(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		c_data = data;
		srcid = c_data["id"];
		dstpos = c_data["dstpos"];

		if not self.game_ins._is_cId_valid(cId):
			return
		srcitemobj = memmode.tb_item_admin.getObj(srcid);
		if not srcitemobj:
			return;
		srcitemdata = srcitemobj.get('data');
		itemlist = self._get_itemlist_by_cId(cId);
		for itemobj in itemlist:
			idata = itemobj.get('data');
			id = idata['id'];
			sid = idata['shape'];
			key = idata['used']
			pos = idata['pos'];
			if pos == dstpos:
				if id == srcid:
					return;
				self._mergeitem(dId,cId,srcid,id);
				return;
			if id == srcid:
				continue;
		srcitemobj.update_multi({'pos':dstpos});
		send_data = {};
		send_data['id'] = srcid;
		send_data['key'] = srcitemdata['used'];
		send_data['pos'] = dstpos;
		send_data['amount'] = 1;
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_ITEM_UPDATE,cId,send_data]);
		return
	def on_itembuy(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		c_data = data;
		shape = c_data["id"];
		if not self.game_ins._is_cId_valid(cId):
			return
		itemc = app.config.item.create_Item(shape);
		if not itemc:
			return
		price = itemc.price;
		roledata = memmode.tb_character_admin.getObj(cId);
		if not roledata:
			return
		roleinfo = roledata.get('data');
		if not roleinfo:
			return
		gold = roleinfo["gold"];
		if gold < price:
			self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_NOTIFY_FLOAT,cId,{'msg':lang_config.LANG_NOTENOUGHGOLD}]);
			return

		
		addpos = self._getemptyslot(cId);
		addid = self._additem(shape,cId,0,addpos);
		if addid != 0:
			gold -= price;
			roledata.update_multi({"gold":gold});
			self.fire_event(EVEVT_FLUSHPLAYERINFO,cId);
			self._send_additem_netpack(addid,dId,cId);
		return
	def dispose(self):
		super(item_main,self).dispose();
		return
# coding: utf-8
# 
import app.base.game_module_mgr
from app.game.core.game_event_def import *
from app.protocol.ProtocolDesc import *
import app.protocol.netutil as netutil
from twisted.python import log
import app.util.helper as helper
import app.util.lang_config as lang_config
import app.game.memmode as memmode
from firefly.server.globalobject import GlobalObject
import app.config.item
import app.config.itemmerge
import app.game.core.game_module_def as game_module_def
class game_main(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(game_main,self).__init__();
		self.character_map = {};
		return
	def _init_module(self):
		self.get_module(game_module_def.GM_MAIN).start();
		self.get_module(game_module_def.MAIN_PLAYER).start();
		self.get_module(game_module_def.PET).start();
		self.get_module(game_module_def.PARTNER).start();
		return
	def start(self):
		super(game_main,self).start();
		self.register_event(EVENT_LOGIN,self.on_login);
		self.register_event(EVENT_LOGOUT,self.on_logout);
		self.register_net_event(C2S_ITEM_GETLIST,self.on_get_itemlist);
		self.register_net_event(C2S_ITEM_USE,self.on_itemuse);
		self.register_net_event(C2S_ITEM_MOVE,self.on_itemmove);
		self.register_net_event(C2S_ITEM_BUY,self.on_itembuy);
		self.register_net_event(C2S_LOGIN_ASYN_TIME,self.on_asyn_time);
		self.register_event(EVENT_SEND2CLIENT,self._send2client);
		self.register_net_event(C2S_LV_UP,self.on_req_lvup);
		self.register_net_event(C2S_SKILL_INFO,self.on_req_skillinfo);
		self.register_net_event(C2S_SKILL_LVUP,self.on_req_skilllvup);
		self._init_module();
		return
	def _send2client(self,ud):
		cmd = ud[0]
		dId = ud[1];
		data = ud[2];
		buf = netutil.s2c_data2bufbycmd(cmd,data);
		GlobalObject().remote['gate'].callRemote("pushObject",cmd,buf, [dId])
		return
	def on_req_skilllvup(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		if not self._is_cId_valid(cId):
			return
		rid = data["id"];
		if rid == 1:
			self.get_module(game_module_def.MAIN_PLAYER).on_req_skilllvup(ud);
		elif rid == 2:
			self.get_module(game_module_def.PET).on_req_skilllvup(ud);
		elif rid == 3:
			self.get_module(game_module_def.PARTNER).on_req_skilllvup(ud);
		return
	def on_req_skillinfo(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		if not self._is_cId_valid(cId):
			return
		rid = data["id"];
		if rid == 1:
			self.get_module(game_module_def.MAIN_PLAYER).on_req_skillinfo(ud);
		elif rid == 2:
			self.get_module(game_module_def.PET).on_req_skillinfo(ud);
		elif rid == 3:
			self.get_module(game_module_def.PARTNER).on_req_skillinfo(ud);
		return
	def on_req_lvup(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		if not self._is_cId_valid(cId):
			return
		rid = data["id"];
		if rid == 1:
			self.get_module(game_module_def.MAIN_PLAYER).on_req_lvup(ud);
		elif rid == 2:
			self.get_module(game_module_def.PET).on_req_lvup(ud);
		elif rid == 3:
			self.get_module(game_module_def.PARTNER).on_req_lvup(ud);
		return;
	def on_asyn_time(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		if not self._is_cId_valid(cId):
			return
		c_data = data;
		client_tm = c_data["time"];

		svr_tm = helper.get_svr_tm();
		send_data = {};
		send_data['srvtime'] = svr_tm;
		send_data['time'] = client_tm;
		self.fire_event(EVENT_SEND2CLIENT,[S2C_ASYNTIME,dId,send_data]);
		return
	def _float_msg(self,dId,msg):
		c_data = {};
		c_data['msg'] = msg;
		self.fire_event(EVENT_SEND2CLIENT,[S2C_NOTIFY_FLOAT,dId,c_data]);
		return;
	def _is_cId_valid(self,cId):#其实就是角色是否在线的判定
		return self.character_map.has_key(cId);
	def on_login(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		self.character_map[cId] = dId;
		return
	def on_logout(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		del self.character_map[cId];
		return
	
	def _get_item_goldspd(self,shape):
		itemc = app.config.item.create_Item(shape);
		if itemc:
			return itemc.goldspd;
		return 0
	def _get_itemlist_by_cId(self,cId):
		itemlist = memmode.tb_item_admin.getAllPkByFk(cId)
		itemobjlist = memmode.tb_item_admin.getObjList(itemlist)
		return itemobjlist
	def _add_gold(self,dId,cId,count):
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			return False
		c_info = c_data.get('data');
		gold = c_info['gold'];
		c_data.update_multi({"gold":gold+count});
		return True
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
	def on_get_itemlist(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		if not self._is_cId_valid(cId):
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
		self.fire_event(EVENT_SEND2CLIENT,[S2C_ITEM_LIST,dId,send_data]);
		return
	def on_itemuse(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		c_data = data;
		itemid = c_data["id"];
		amount = c_data["amount"];

		itemobj = memmode.tb_item_admin.getObj(itemid);
		if not itemobj:
			return;
		itemdata = itemobj.get('data');
		if not itemdata:
			return;
		v = itemdata['used'];
		if v == 0:
			v = 1;
		else:
			v = 0;
		itemobj.update_multi({'used':v});
		send_data = {};
		send_data['id'] = itemid;
		send_data['key'] = v;
		send_data['pos'] = itemdata['pos'];
		send_data['amount'] = itemdata['amount'];
		self.fire_event(EVENT_SEND2CLIENT,[S2C_ITEM_UPDATE,dId,send_data]);
		return
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
		self.fire_event(EVENT_SEND2CLIENT,[S2C_ITEM_DEL,dId,send_data]);
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

	def on_itemmove(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		c_data = data;
		srcid = c_data["id"];
		dstpos = c_data["dstpos"];

		if not self._is_cId_valid(cId):
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
		self.fire_event(EVENT_SEND2CLIENT,[S2C_ITEM_UPDATE,dId,send_data]);
		return
	def on_itembuy(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		c_data = data;
		shape = c_data["id"];
		if not self._is_cId_valid(cId):
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
			self._float_msg(lang_config.LANG_NOTENOUGHGOLD);
			return

		
		addpos = self._getemptyslot(cId);
		addid = self._additem(shape,cId,0,addpos);
		if addid != 0:
			gold -= price;
			roledata.update_multi({"gold":gold});
			self._push_role_info(dId,cId);
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
		self.fire_event(EVENT_SEND2CLIENT,[S2C_ITEM_ADD,dId,send_data]);
		return
	def dispose(self):
		super(game_main,self).dispose();
		return
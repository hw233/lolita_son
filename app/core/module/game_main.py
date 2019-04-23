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
import app.config.item
import app.config.itemmerge
import app.core.game_module_def as game_module_def
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
		self.get_module(game_module_def.CARD_MAIN).start();
		self.get_module(game_module_def.ITEM_MAIN).start();
		return
	def start(self):
		super(game_main,self).start();
		self.register_event(EVENT_LOGIN,self.on_login);
		self.register_event(EVENT_LOGOUT,self.on_logout);
		self.register_event(EVENT_RELOGIN,self.on_relogin);
		
		self.register_net_event(C2S_LOGIN_ASYN_TIME,self.on_asyn_time);
		self.register_event(EVENT_SEND2CLIENT,self._send2client);
		self.register_event(EVENT_SEND2CLIENTBYCID,self._send2clientbycid)
		self.register_net_event(C2S_LV_UP,self.on_req_lvup);
		self.register_net_event(C2S_SKILL_INFO,self.on_req_skillinfo);
		self.register_net_event(C2S_SKILL_LVUP,self.on_req_skilllvup);
		self._init_module();
		return
	def _getdidbycid(self,cId):
		if self.character_map.has_key(cId):
			return self.character_map[cId];
		return
	def _send2clientbycid(self,ud):
		cmd = ud[0]
		cId = ud[1];
		dId = self._getdidbycid(cId);
		if dId == None:
			log.err("_send2clientbycid err:%s %s"%(cId,ud));
			return
		data = ud[2];
		buf = netutil.s2c_data2bufbycmd(cmd,data);
		GlobalObject().remote['gate'].callRemote("pushObject",cmd,buf, [dId])
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
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_ASYNTIME,cId,send_data]);
		return
	def _is_cId_valid(self,cId):#其实就是角色是否在线的判定
		return self.character_map.has_key(cId);
	def on_login(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		self.character_map[cId] = dId;
		return
	def on_relogin(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		if self.character_map.has_key(cId):
			self.character_map[cId] = dId;
		return
	def on_logout(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		if self.character_map.has_key(cId):
			del self.character_map[cId];
		return
	
	
	def dispose(self):
		super(game_main,self).dispose();
		return
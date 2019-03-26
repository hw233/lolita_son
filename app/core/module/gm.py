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
class gm_main(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(gm_main,self).__init__();
		return
	def start(self):
		super(gm_main,self).start();
		self.register_net_event(C2S_CHAT_GM,self.on_chat_gm)
		return
	def _parse_gm_cmd(self,params,dId,cId):
		gm_cmd = params[0];
		if gm_cmd == "$addgold":
			if len(params) > 1:
				game_ins = self.get_module(game_module_def.GAME_MAIN);
				count = int(params[1]);
				if game_ins._add_gold(dId,cId,count):
					game_ins._push_role_info(dId,cId);
		elif gm_cmd == "$fightself":
			data = {};
			data['type'] = 0;
			data['team1'] = [cId];
			data['team2'] = [cId];
			GlobalObject().remote['gate'].callRemote("startCombat",dId,cId,data);
		elif gm_cmd == "$fight":
			if len(params) > 1:
				data = {};
				data['type'] = 1;
				data['group'] = int(params[1]);
				GlobalObject().remote['gate'].callRemote("startCombat",dId,cId,data);
		elif gm_cmd == "$lvup":
			print "_parse_gm_cmd lvup"
			roledata = memmode.tb_character_admin.getObj(cId);
			if not roledata:
				return
			roleinfo = roledata.get('data');
			if not roleinfo:
				return
			lv = roleinfo["level"];
			staminia = roleinfo["staminia"];
			spirit = roleinfo["spirit"];
			dex = roleinfo["dex"];
			point = roleinfo["point"]
			roledata.update_multi({"level":lv+1,"staminia":staminia+1,"spirit":spirit+1,"dex":dex+1,"point":point+3});
			game_ins = self.get_module(game_module_def.MAIN_PLAYER);
			game_ins._push_role_info(dId,cId);
		return
	def on_chat_gm(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		data = ud["data"];
		print "gm on_chat_gm %d %d %s"%(dId,cId,str(data));
		game_ins = self.get_module(game_module_def.GAME_MAIN);
		if not game_ins._is_cId_valid(cId):
			return
		c_data = data;
		msg = c_data["msg"];
		if msg != None and len(msg) > 0:
			params = msg.split();
			if len(params) > 0:
				self._parse_gm_cmd(params,dId,cId);

		return
	def dispose(self):
		super(gm_main,self).dispose();
		return
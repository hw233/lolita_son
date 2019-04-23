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

import app.config.player_exp
import app.combat.skill
import app.combat.skillpassive

class mainplayer(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(mainplayer,self).__init__();
		self.game_ins = None;
		self.lv_max = 99;
		return
	def start(self):
		super(mainplayer,self).start();
		self.register_net_event(C2S_ROLE_INFO,self.on_get_roleinfo);
		self.register_net_event(C2S_CLICK,self.on_click);
		self.register_event(EVEVT_FLUSHPLAYERINFO,self.on_event_flushplayerinfo);
		self.register_event(EVENT_ADDEXP2PLAYER,self.on_event_addexp2player);
		self.register_event(EVENT_ADDGOLD2PLAYER,self.on_event_addgold2player);
		self.game_ins = self.get_module(game_module_def.GAME_MAIN);
		max_lv = 0;
		for lvkey in app.config.player_exp.player_exp_map:
			if lvkey > max_lv:
				max_lv = lvkey;
		self.lv_max = max_lv;

		return
	def on_event_flushplayerinfo(self,ud):
		cid = ud;
		self._push_role_info(cid);
		return
	def _use_skill(self,cid,skillid,useidx):
		skillpklist = memmode.tb_skill_admin.getAllPkByFk(cid)
		skillobjlist = memmode.tb_skill_admin.getObjList(skillpklist)
		for skillobj in skillobjlist:
			idata = skillobj.get('data');
			sid = idata['skillid'];
			if sid == skillid:
				skillobj.update_multi({"useidx":useidx});
				return True
		return False
	def _study_skill(self,cid,skillid,slv = 1):
		skillpklist = memmode.tb_skill_admin.getAllPkByFk(cid)
		skillobjlist = memmode.tb_skill_admin.getObjList(skillpklist)
		for skillobj in skillobjlist:
			idata = skillobj.get('data');
			sid = idata['skillid'];
			if sid == skillid:
				return False
		data = {};
		data['characterId'] = cid;
		data['skillid'] = skillid;
		data['skilllv'] = slv;
		data['useidx'] = 0;
		newskillmode = memmode.tb_skill_admin.new(data);
		return True
	def _lvup_skill(self,cid,skillid):
		skillpklist = memmode.tb_skill_admin.getAllPkByFk(cid)
		skillobjlist = memmode.tb_skill_admin.getObjList(skillpklist)
		for skillobj in skillobjlist:
			idata = skillobj.get('data');
			sid = idata['skillid'];
			slv = idata['skilllv'];
			if sid == skillid:
				lv_max = app.combat.skill.get_skill_max(sid);
				if lv_max <= 0:
					return True
				if slv >= lv_max:
					return True
				slv += 1;
				skillobj.update_multi({"skilllv":slv});
				return True
		return False
	def on_click(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		return
	def req_lvup(self,cId,use_exp = True):
		if not self.game_ins._is_cId_valid(cId):
			return
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('req_lvup err %d'%(cId));
			return
		c_info = c_data.get('data');
		lv = c_info['level'];
		exp = c_info['exp'];
		
		if lv >= self.lv_max:
			self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_NOTIFY_FLOAT,cId,{'msg':lang_config.LANG_LVMAX}]);
			return
		if use_exp:
			req_exp_info = app.config.player_exp.create_Player_exp(lv);
			if req_exp_info == None:
				return
			req_exp = req_exp_info.exp;
			if exp < req_exp:
				self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_NOTIFY_FLOAT,cId,{'msg':lang_config.LANG_NOTENOUGHEXP}]);
				return
			exp -= req_exp;
		staminia = c_info["staminia"];
		spirit = c_info["spirit"];
		dex = c_info["dex"];
		point = c_info["point"];
		c_data.update_multi({"exp":exp,"level":lv+1,"staminia":staminia+1,"spirit":spirit+1,"dex":dex+1,"point":point+3});
		
		self._push_role_info(cId);
		return

	def on_req_skilllvup(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		data = ud["data"];
		skillid = data["skillid"];
		
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('on_req_skilllvup err %d'%(cId));
			return
		if self._lvup_skill(cId,skillid):
			self._push_role_info(cId);
			self.on_req_skillinfo(ud);
			return
		#study new skill
		self._study_skill(cId,skillid);
		self._push_role_info(cId);
		self.on_req_skillinfo(ud);
		
		return
	def on_req_skillinfo(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		#todo
		skillpklist = memmode.tb_skill_admin.getAllPkByFk(cId)
		skillobjlist = memmode.tb_skill_admin.getObjList(skillpklist)

		#skillid1 = self.skill1id;
		#skillid2 = self.skill2id;
		#skill1lv = 0;
		#skill2lv = 0;
		#for skillobj in skillobjlist:
		#	idata = skillobj.get('data');
		#	id = idata['id'];
		#	sid = idata['skillid'];
		#	slv = idata['skilllv']
		#	if sid == skillid1:
		#		skill1lv = slv;
		#	if sid == skillid2:
		#		skill2lv = slv;

		#send_data = {};
		#send_data['id'] = 1;
		#send_data['skill1lv'] = skill1lv;
		#send_data['skill2lv'] = skill2lv;
		#self.fire_event(EVENT_SEND2CLIENT,[S2C_SKILL_INFO,dId,send_data]);
		return
	def on_get_roleinfo(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		
		if not self._push_role_info(cId):
			self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_NOTIFY_FLOAT,cId,{'msg':lang_config.LANG_INVALID_ROLE+' %d'%cId}]);
			log.msg('_push_role_info err %d'%(cId));
			return
		return
	def on_event_addgold2player(self,ud):
		cId = ud[0];
		gold = ud[1];
		if not self.game_ins._is_cId_valid(cId):
			return
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('on_event_addgold2player err %d'%(cId));
			return False
		curgold = c_info['gold'];
		c_data.update_multi({"gold":curgold+gold});
		self._push_role_info(cId)
		return
	def on_event_addexp2player(self,ud):
		cId = ud[0];
		exp = ud[1];
		if not self.game_ins._is_cId_valid(cId):
			return
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('on_event_addgold2player err %d'%(cId));
			return False
		curexp = c_info['exp'];
		c_data.update_multi({"exp":curexp+exp});
		self._push_role_info(cId)
		return
	def _sync_role_gold_exp(self,cId):
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('_sync_role_gold_exp err %d'%(cId));
			return False

		c_info = c_data.get('data');
		gold = c_info['gold'];
		goldspd = c_info['goldspd'];
		exp = c_info['exp'];
		expspd = c_info['expspd'];
		energy = c_info['energy'];
		energyspd = c_info['energyspd'];
		goldtm = c_info['goldtm'];
		tm = c_info['tm'];
		if int(goldtm) == 0:
			goldtm = tm;
		svr_tm = helper.get_svr_tm();
		plus_tm = svr_tm - goldtm;

		
		plus_gold = goldspd*plus_tm;
		gold += plus_gold;
		plus_exp = expspd*plus_tm;
		exp += plus_exp;
		plus_energy = energyspd*plus_tm;
		energy += plus_energy;

		c_data.update_multi({"gold":gold,"goldspd":goldspd,"exp":exp,"expspd":expspd,"energy":energy,"energyspd":energyspd,"goldtm":goldtm});
		return True
	def _push_role_info(self,cId):
		c_info = memmode.tb_character_admin.getObjData(cId);
		if not c_info:
			return False
		lv = c_info['level']
		shape = c_info['figure'];
		gold = c_info['gold'];
		goldspd = c_info['goldspd'];
		exp = c_info['exp'];
		expspd = c_info['expspd'];
		goldtm = c_info['goldtm'];
		energy = c_info['energy'];
		send_data = {};
		send_data['lv'] = lv;
		send_data['shape'] = shape;
		send_data['stamina'] = energy;
		send_data['exp'] = exp;
		send_data['expspd'] = expspd;

		send_data['gold'] = gold;
		send_data['goldspd'] = goldspd;
		send_data['tm'] = goldtm;
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_ROLE_INFO,cId,send_data]);
		return True;
	def dispose(self):
		super(mainplayer,self).dispose();
		return
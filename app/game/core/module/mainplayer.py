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
import app.game.core.game_module_def as game_module_def
import app.config.player_exp
import app.config.playerskill1
import app.config.playerskill2
class mainplayer(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(mainplayer,self).__init__();
		self.game_ins = None;
		self.lv_max = 99;
		self.skill1id = 1;
		self.skill2id = 2;
		self.skill1lv_max = 99;
		self.skill2lv_max = 99;
		return
	def start(self):
		super(mainplayer,self).start();
		self.register_net_event(C2S_ROLE_INFO,self.on_get_roleinfo);
		self.register_net_event(C2S_CLICK,self.on_click);
		self.game_ins = self.get_module(game_module_def.GAME_MAIN);
		max_lv = 0;
		for lvkey in app.config.player_exp.player_exp_map:
			if lvkey > max_lv:
				max_lv = lvkey;
		self.lv_max = max_lv;

		max_lv = 0;
		for lvkey in app.config.playerskill1.playerskill1_map:
			if lvkey > max_lv:
				max_lv = lvkey;
		self.skill1lv_max = max_lv;

		max_lv = 0;
		for lvkey in app.config.playerskill2.playerskill2_map:
			if lvkey > max_lv:
				max_lv = lvkey;
		self.skill2lv_max = max_lv;
		return
	def on_click(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		if not self._sync_role_gold_exp(cId):
			self._float_msg(lang_config.LANG_CALCGOLDFAILED+' %d'%cId);
			log.msg('_sync_role_gold_exp err %d'%(cId));
			return
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('on_click err %d'%(cId));
			return
		c_info = c_data.get('data');
		lv = c_info['level'];
		exp = c_info['exp'];
		gold = c_info['gold'];

		data = ud["data"];
		x = data["x"];
		y = data["y"];

		addexp = c_info["clickexp"];
		addgold = c_info["clickgold"];
		exp += addexp;
		gold += addgold;
		c_data.update_multi({"exp":exp,"gold":gold});

		send_data = {};
		send_data['x'] = x;
		send_data['y'] = y;
		send_data['exp'] = addexp;
		send_data['gold'] = addgold;
		self.fire_event(EVENT_SEND2CLIENT,[S2C_CLICK,dId,send_data]);

		if not self._push_role_info(dId,cId):
			self._float_msg(lang_config.LANG_INVALID_ROLE+' %d'%cId);
			log.msg('_push_role_info err %d'%(cId));
			return
		return
	def on_req_lvup(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		if not self._sync_role_gold_exp(cId):
			self._float_msg(lang_config.LANG_CALCGOLDFAILED+' %d'%cId);
			log.msg('_sync_role_gold_exp err %d'%(cId));
			return
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('on_req_lvup err %d'%(cId));
			return
		c_info = c_data.get('data');
		lv = c_info['level'];
		exp = c_info['exp'];
		req_exp_info = app.config.player_exp.create_Player_exp(lv);
		if req_exp_info == None:
			self._float_msg("lvup error %d"%(lv));
			return
		if lv >= self.lv_max:
			self._float_msg(lang_config.LANG_LVMAX);
			return
		req_exp = req_exp_info.exp;
		if exp < req_exp:
			self._float_msg(lang_config.LANG_NOTENOUGHEXP);
			return
		exp -= req_exp;
		lv += 1;
		c_data.update_multi({"exp":exp,"level":lv});
		self._sync_role_click_reward();
		if not self._push_role_info(dId,cId):
			self._float_msg(lang_config.LANG_INVALID_ROLE+' %d'%cId);
			log.msg('_push_role_info err %d'%(cId));
			return
		return
	def _sync_role_produce_reward(self,cId):
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('_sync_role_click_reward err %d'%(cId));
			return
		c_info = c_data.get('data');
		pet_obj = self.get_module(game_module_def.PET)._get_pet_obj(cId);
		if pet_obj != None:
			lv = pet_obj["lv"];
			lv_info = app.config.pet_exp.create_Pet_exp(lv);
			addgold = lv_info.goldpersec;
			addexp = lv_info.exppersec;
			c_data.update_multi({"expspd":addexp,"goldspd":addgold});
		return
	def _sync_role_click_reward(self,cId):
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('_sync_role_click_reward err %d'%(cId));
			return
		c_info = c_data.get('data');
		lv = c_info['level'];
		lv_info = app.config.player_exp.create_Player_exp(lv);
		if lv_info == None:
			log.msg('_sync_role_click_reward get exp info err %d %d'%(cId,lv));
			return
		addgold = lv_info.goldperclick;
		addexp = lv_info.expperclick;

		skillpklist = memmode.tb_skill_admin.getAllPkByFk(cId)
		skillobjlist = memmode.tb_skill_admin.getObjList(skillpklist)
		for skillobj in skillobjlist:
			idata = skillobj.get('data');
			id = idata['id'];
			sid = idata['skillid'];
			slv = idata['skilllv'];
			if sid == self.skill1id:
				exp_info = app.config.playerskill1.create_Playerskill1(slv);
				addexpperclick = exp_info.expperclick;
				addexp += addexpperclick;
			elif sid == self.skill2id:
				exp_info = app.config.playerskill2.create_Playerskill2(slv);
				addgoldperclick = exp_info.goldperclick;
				addgold += addgoldperclick;
		c_data.update_multi({"clickexp":addexp,"clickgold":addgold});
		return

	def on_req_skilllvup(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		data = ud["data"];
		skillid = data["skillid"];
		
		if not self._sync_role_gold_exp(cId):
			self._float_msg(lang_config.LANG_CALCGOLDFAILED+' %d'%cId);
			log.msg('_sync_role_gold_exp err %d'%(cId));
			return
		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('on_req_lvup err %d'%(cId));
			return
		c_info = c_data.get('data');
		mainlv = c_info['level'];
		maingold = c_info['gold'];

		skillpklist = memmode.tb_skill_admin.getAllPkByFk(cId)
		skillobjlist = memmode.tb_skill_admin.getObjList(skillpklist)
		for skillobj in skillobjlist:
			idata = skillobj.get('data');
			id = idata['id'];
			sid = idata['skillid'];
			slv = idata['skilllv'];
			if sid == skillid:
				if sid == self.skill1id:
					if slv >= self.skill1lv_max:
						self._float_msg(lang_config.LANG_SKILLLVMAX);
						return;
					exp_info = app.config.playerskill1.create_Playerskill1(slv);
					if exp_info == None:
						self._float_msg("skilllvup error %d %d"%(sid,slv));
						return
					req_lv = exp_info.reqlv;
					req_gold = exp_info.gold;
					addexpperclick = exp_info.expperclick;
					if req_lv > mainlv:
						self._float_msg(lang_config.LANG_SKILLREQHIGHERLV);
						return;
					if req_gold > maingold:
						self._float_msg(lang_config.LANG_SKILLREQHIGHERGOLD);
						return;
					maingold -= req_gold;
					slv += 1;
					c_data.update_multi({"gold":maingold});
					skillobj.update_multi({"skilllv":slv});
					self._sync_role_click_reward();
					self._push_role_info(dId,cId);
					self.on_req_skillinfo(ud);
					return;
				elif sid == self.skill2id:
					if slv >= self.skill2lv_max:
						self._float_msg(lang_config.LANG_SKILLLVMAX);
						return;
					exp_info = app.config.playerskill2.create_Playerskill2(slv);
					if exp_info == None:
						self._float_msg("skilllvup error %d %d"%(sid,slv));
						return
					req_lv = exp_info.reqlv;
					req_gold = exp_info.gold;
					addgoldperclick = exp_info.goldperclick;
					if req_lv > mainlv:
						self._float_msg(lang_config.LANG_SKILLREQHIGHERLV);
						return;
					if req_gold > maingold:
						self._float_msg(lang_config.LANG_SKILLREQHIGHERGOLD);
						return;
					maingold -= req_gold;
					slv += 1;
					c_data.update_multi({"gold":maingold});
					skillobj.update_multi({"skilllv":slv});
					self._sync_role_click_reward();
					self._push_role_info(dId,cId);
					self.on_req_skillinfo(ud);
					return;
		#study new skill
		if skillid == self.skill1id:
			exp_info = app.config.playerskill1.create_Playerskill1(1);
			if exp_info == None:
				self._float_msg("study new skill error %d"%(skillid));
				return
			req_lv = exp_info.reqlv;
			req_gold = exp_info.gold;
			if req_lv > mainlv:
				self._float_msg(lang_config.LANG_SKILLREQHIGHERLV);
				return;
			if req_gold > maingold:
				self._float_msg(lang_config.LANG_SKILLREQHIGHERGOLD);
				return;
			maingold -= req_gold;
			c_data.update_multi({"gold":maingold});
			#
			
			data = {};
			data['characterId'] = cId;
			data['skillid'] = skillid;
			data['skilllv'] = 1;
			newskillmode = memmode.tb_skill_admin.new(data);
			
			self._sync_role_click_reward();
			self._push_role_info(dId,cId);
			self.on_req_skillinfo(ud);
			return;
		elif skillid == self.skill2id:
			exp_info = app.config.playerskill2.create_Playerskill2(1);
			if exp_info == None:
				self._float_msg("study new skill error %d"%(skillid));
				return
			req_lv = exp_info.reqlv;
			req_gold = exp_info.gold;
			if req_lv > mainlv:
				self._float_msg(lang_config.LANG_SKILLREQHIGHERLV);
				return;
			if req_gold > maingold:
				self._float_msg(lang_config.LANG_SKILLREQHIGHERGOLD);
				return;
			maingold -= req_gold;
			c_data.update_multi({"gold":maingold});
			#
			
			data = {};
			data['characterId'] = cId;
			data['skillid'] = skillid;
			data['skilllv'] = 1;
			newskillmode = memmode.tb_skill_admin.new(data);
			
			self._sync_role_click_reward();
			self._push_role_info(dId,cId);
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

		skillid1 = self.skill1id;
		skillid2 = self.skill2id;
		skill1lv = 0;
		skill2lv = 0;
		for skillobj in skillobjlist:
			idata = skillobj.get('data');
			id = idata['id'];
			sid = idata['skillid'];
			slv = idata['skilllv']
			if sid == skillid1:
				skill1lv = slv;
			if sid == skillid2:
				skill2lv = slv;

		send_data = {};
		send_data['id'] = 1;
		send_data['skill1lv'] = skill1lv;
		send_data['skill2lv'] = skill2lv;
		self.fire_event(EVENT_SEND2CLIENT,[S2C_SKILL_INFO,dId,send_data]);
		return
	def on_get_roleinfo(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		
		if not self._sync_role_gold_exp(cId):
			self._float_msg(lang_config.LANG_CALCGOLDFAILED+' %d'%cId);
			log.msg('_sync_role_gold_exp err %d'%(cId));
			return
		if not self._push_role_info(dId,cId):
			self._float_msg(lang_config.LANG_INVALID_ROLE+' %d'%cId);
			log.msg('_push_role_info err %d'%(cId));
			return
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
	def _push_role_info(self,dId,cId):
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
		self.fire_event(EVENT_SEND2CLIENT,[S2C_ROLE_INFO,dId,send_data]);
		return True;
	def dispose(self):
		super(mainplayer,self).dispose();
		return
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
import app.config.partner_exp
import app.config.partnerskill1
import app.config.partnerskill2
class partner(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(partner,self).__init__();
		self.game_ins = None;
		self.mainplayer_ins = None;
		self.open_lv = 10;
		self.lv_max = 99;
		self.skill1id = 1;
		self.skill2id = 2;
		self.skill1lv_max = 99;
		self.skill2lv_max = 99;
		return
	def start(self):
		super(partner,self).start();
		self.game_ins = self.get_module(game_module_def.GAME_MAIN);
		self.mainplayer_ins = self.get_module(game_module_def.MAIN_PLAYER);
		self.register_net_event(C2S_PARTNER_INFO,self.on_get_roleinfo);
		max_lv = 0;
		for lvkey in app.config.partner_exp.partner_exp_map:
			if lvkey > max_lv:
				max_lv = lvkey;
		self.lv_max = max_lv;

		max_lv = 0;
		for lvkey in app.config.partnerskill1.partnerskill1_map:
			if lvkey > max_lv:
				max_lv = lvkey;
		self.skill1lv_max = max_lv;

		max_lv = 0;
		for lvkey in app.config.partnerskill2.partnerskill2_map:
			if lvkey > max_lv:
				max_lv = lvkey;
		self.skill2lv_max = max_lv;
		return
	def _get_partner_obj(self,cId):
		partnerpklist = memmode.tb_partner_admin.getAllPkByFk(cId)
		objlist = memmode.tb_partner_admin.getObjList(partnerpklist)
		if len(objlist) <= 0:
			return None;
		return objlist[0].get('data');
		
	def on_req_lvup(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		#
		self.mainplayer_ins._sync_role_gold_exp();

		c_data = memmode.tb_character_admin.getObj(cId);
		if not c_data:
			log.msg('pet on_req_lvup err getroleinfo %d'%(cId));
			return
		c_info = c_data.get('data');
		mlv = c_info['level'];
		mexp = c_info['exp'];

		pklist = memmode.tb_partner_admin.getAllPkByFk(cId)
		objlist = memmode.tb_partner_admin.getObjList(pklist)
		if len(objlist) <= 0:
			#add new pet
			if mlv < self.open_lv:
				self._float_msg(lang_config.LANG_SKILLREQHIGHERLV);
				return;
			#
			data = {};
			data['characterId'] = cId;
			data['shape'] = skillid;
			data['lv'] = 1;
			data['exp'] = 0;
			newpetmode = memmode.tb_partner_admin.new(data);
			self.mainplayer_ins._sync_role_produce_reward();
			self.mainplayer_ins._sync_role_click_reward();
			self._push_role_info(dId,cId);
			return
		for pobj in objlist:
			idata = pobj.get('data');
			id = idata['id'];
			shape = idata['shape'];
			lv = idata['lv'];
			exp = idata['exp'];
			exp_info = app.config.partner_exp.create_Partner_exp(lv);
			if exp_info == None:
				self._float_msg("partner lvup error %d"%(lv));
				return
			if lv >= self.lv_max:
				self._float_msg(lang_config.LANG_LVMAX);
				return
			req_exp = exp_info.exp;
			if req_exp <= exp:
				lv += 1;
				exp -= req_exp;
				pobj.update_multi({"exp":exp,"lv":lv});
				self.mainplayer_ins._sync_role_produce_reward();
				self.mainplayer_ins._sync_role_click_reward();
				self._push_role_info(dId,cId);
				return;
			need_exp = req_exp - exp;
			if mexp >= need_exp:
				mexp -= need_exp;
				c_data.update_multi({"exp":mexp});
				lv += 1;
				pobj.update_multi({"exp":0,"lv":lv});
				self.mainplayer_ins._sync_role_produce_reward();
				self.mainplayer_ins._sync_role_click_reward();
				self._push_role_info(dId,cId);
				self.mainplayer_ins._push_role_info(dId,cId);
			else:
				c_data.update_multi({"exp":0});
				pobj.update_multi({"exp":exp+mexp});
				self._push_role_info(dId,cId);
				self.mainplayer_ins._push_role_info(dId,cId);
				return;
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
			log.msg('pet on_req_skilllvup err %d'%(cId));
			return
		c_info = c_data.get('data');
		mainlv = c_info['level'];
		maingold = c_info['gold'];

		pklist = memmode.tb_partner_admin.getAllPkByFk(cId)
		objlist = memmode.tb_partner_admin.getObjList(pklist)
		if len(objlist) <= 0:
			log.msg('pet on_req_skilllvup err have not pet %d'%(cId));
			return
		pobj = objlist[0];
		pinfo = pobj.get('data');
		petlv = pinfo['lv'];

		skillpklist = memmode.tb_partnerskill_admin.getAllPkByFk(cId)
		skillobjlist = memmode.tb_partnerskill_admin.getObjList(skillpklist)
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
					exp_info = app.config.partnerskill1.create_Partnerskill1(slv);
					if exp_info == None:
						self._float_msg("partner skilllvup error %d %d"%(sid,slv));
						return
					req_lv = exp_info.reqlv;
					req_gold = exp_info.gold;
					exprate = exp_info.exprate;
					if req_lv > petlv:
						self._float_msg(lang_config.LANG_PETSKILLREQHIGHERLV);
						return;
					if req_gold > maingold:
						self._float_msg(lang_config.LANG_SKILLREQHIGHERLV);
						return;
					maingold -= req_gold;
					slv += 1;
					c_data.update_multi({"gold":maingold});
					skillobj.update_multi({"skilllv":slv});
					self.mainplayer_ins._sync_role_produce_reward();
					self.mainplayer_ins._sync_role_click_reward();
					self.mainplayer_ins._push_role_info(dId,cId);
					self.on_req_skillinfo(ud);
					return;
				elif sid == self.skill2id:
					if slv >= self.skill2lv_max:
						self._float_msg(lang_config.LANG_SKILLLVMAX);
						return;
					exp_info = app.config.partnerskill2.create_Partnerskill2(slv);
					if exp_info == None:
						self._float_msg("pet skilllvup error %d %d"%(sid,slv));
						return
					req_lv = exp_info.reqlv;
					req_gold = exp_info.gold;
					goldrate = exp_info.goldrate;
					if req_lv > petlv:
						self._float_msg(lang_config.LANG_PETSKILLREQHIGHERLV);
						return;
					if req_gold > maingold:
						self._float_msg(lang_config.LANG_SKILLREQHIGHERLV);
						return;
					maingold -= req_gold;
					slv += 1;
					c_data.update_multi({"gold":maingold});
					skillobj.update_multi({"skilllv":slv});
					self.mainplayer_ins._sync_role_produce_reward();
					self.mainplayer_ins._sync_role_click_reward();
					self.mainplayer_ins._push_role_info(dId,cId);
					self.on_req_skillinfo(ud);
					return;
		#study new skill
		if skillid == self.skill1id:
			exp_info = app.config.partnerskill1.create_Partnerskill1(1);
			if exp_info == None:
				self._float_msg("pet study new skill error %d"%(skillid));
				return
			req_lv = exp_info.reqlv;
			req_gold = exp_info.gold;
			if req_lv > petlv:
				self._float_msg(lang_config.LANG_PETSKILLREQHIGHERLV);
				return;
			if req_gold > maingold:
				self._float_msg(lang_config.LANG_SKILLREQHIGHERLV);
				return;
			maingold -= req_gold;
			c_data.update_multi({"gold":maingold});
			#
			
			data = {};
			data['characterId'] = cId;
			data['skillid'] = skillid;
			data['skilllv'] = 1;
			newskillmode = memmode.tb_partnerskill_admin.new(data);
			
			self.mainplayer_ins._sync_role_produce_reward();
			self.mainplayer_ins._sync_role_click_reward();
			self.mainplayer_ins._push_role_info(dId,cId);
			self.on_req_skillinfo(ud);
			return;
		elif skillid == self.skill2id:
			exp_info = app.config.partnerskill2.create_Partnerskill2(1);
			if exp_info == None:
				self._float_msg("pet study new skill error %d"%(skillid));
				return
			req_lv = exp_info.reqlv;
			req_gold = exp_info.gold;
			if req_lv > petlv:
				self._float_msg(lang_config.LANG_PETSKILLREQHIGHERLV);
				return;
			if req_gold > maingold:
				self._float_msg(lang_config.LANG_SKILLREQHIGHERLV);
				return;
			maingold -= req_gold;
			c_data.update_multi({"gold":maingold});
			#
			
			data = {};
			data['characterId'] = cId;
			data['skillid'] = skillid;
			data['skilllv'] = 1;
			newskillmode = memmode.tb_partnerskill_admin.new(data);
			
			self.mainplayer_ins._sync_role_produce_reward();
			self.mainplayer_ins._sync_role_click_reward();
			self.mainplayer_ins._push_role_info(dId,cId);
			self.on_req_skillinfo(ud);
		return
	def on_req_skillinfo(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		#todo
		skillpklist = memmode.tb_partnerskill_admin.getAllPkByFk(cId)
		skillobjlist = memmode.tb_partnerskill_admin.getObjList(skillpklist)

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
		send_data['id'] = 3;
		send_data['skill1lv'] = skill1lv;
		send_data['skill2lv'] = skill2lv;
		self.fire_event(EVENT_SEND2CLIENT,[S2C_SKILL_INFO,dId,send_data]);
		return
	def on_get_roleinfo(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		
		if not self.game_ins._is_cId_valid(cId):
			return
		
		self._push_role_info(dId,cId);
		return
	def _push_role_info(self,dId,cId):
		petpklist = memmode.tb_partner_admin.getAllPkByFk(cId)
		petobjlist = memmode.tb_partner_admin.getObjList(petpklist)
		if len(petobjlist) <= 0:
			send_data = {};
			send_data['lv'] = 0;
			send_data['shape'] = 0;
			send_data['exp'] = 0;
			self.fire_event(EVENT_SEND2CLIENT,[S2C_PARTNER_INFO,dId,send_data]);
		else:
			for skillobj in skillobjlist:
				idata = skillobj.get('data');
				id = idata['id'];
				shape = idata['shape'];
				lv = idata['lv'];
				exp = idata['exp'];
				send_data = {};
				send_data['lv'] = lv;
				send_data['shape'] = shape;
				send_data['exp'] = exp;
				self.fire_event(EVENT_SEND2CLIENT,[S2C_PARTNER_INFO,dId,send_data]);
				return;
		return True;
	def dispose(self):
		super(partner,self).dispose();
		return
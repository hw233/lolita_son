# coding: utf-8
# 
import app.base.game_module_mgr
from app.core.game_event_def import *
from app.protocol.ProtocolDesc import *
import app.protocol.netutil as netutil
from twisted.python import log
import app.util.helper as helper
import app.util.lang_config as lang_config
import app.combatsvr.memmode as memmode
from firefly.server.globalobject import GlobalObject
import app.core.game_module_def as game_module_def

import app.combat.combat
import app.combat.warrior

import app.config.fightgroup as fightgroup
import app.config.fightconfig as fightconfig
import app.config.fightdata as fightdata

class combat_main(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(combat_main,self).__init__();
		self.character_map = {};
		
		self.combat_map = {};#combat id 2 combat inst
		self.init_char_2_combat = {};#init character 2 combat
		self.char_2_combat = {};#character 2 combat map
		return
	
	def start(self):
		super(combat_main,self).start();
		self.register_event(EVENT_LOGIN,self.on_login);
		self.register_event(EVENT_LOGOUT,self.on_logout);
		self.register_event(EVENT_RELOGIN,self.on_relogin);
		self.register_event(EVENT_STARTCOMBAT,self.on_startcombat);
		self.register_event(EVENT_ENDCOMBAT,self.on_endcombat);
		self.register_net_event(C2S_WAR_PLAYEND,self.on_war_playend)
		self.register_event(EVENT_SEND2CLIENT,self._send2client);
		self.register_event(EVENT_SEND2CLIENTBYCID,self._send2clientbycid)
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
	def _send2clientbycidlist(self,cmd,cid_list,data):
		print "combat_main _send2clientbycidlist %x %s"%(cmd,cid_list);
		dId_list = [];
		for i in cid_list:
			dId = self._getdidbycid(i);
			if dId != None:
				dId_list.append(dId);
		if len(dId_list) <= 0:
			return
		buf = netutil.s2c_data2bufbycmd(cmd,data);
		GlobalObject().remote['gate'].callRemote("pushObject",cmd,buf, dId_list)

		return;
	def _float_msg(self,dId,msg):
		c_data = {};
		c_data['msg'] = msg;
		self.fire_event(EVENT_SEND2CLIENT,[S2C_NOTIFY_FLOAT,dId,c_data]);
		return;
	def _is_cId_valid(self,cId):#其实就是角色是否在线的判定
		return self.character_map.has_key(cId);
	def on_relogin(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		if self.character_map.has_key(cId):
			self.character_map[cId] = dId;
		return
	def on_login(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		self.character_map[cId] = dId;
		#c_data = memmode.tb_character_admin.getObj(cId);
		#if not c_data:
		#	log.msg('chat_main on_login fatal err %d'%(cId));
		#	return
		#c_info = c_data.get('data');
		
		return
	def on_logout(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];
		if self.character_map.has_key(cId):
			del self.character_map[cId];
		return
	def _add_combatgroup_monster(self,combat_inst,group,pos_idx,cfgid,count,cnum):
		if count <= 0:
			return pos_idx;
		hpstr = "";
		attackstr = "";
		speedstr = "";

		cfightdata = fightdata.create_Fightdata(cfgid);
		cfightconfig = None;
		cfightnumconfig = None;

		if cfightdata:
			cfightconfig = fightconfig.create_Fightconfig(cfightdata.get("fight",0));
			if cfightconfig:
				mfcd = cfightconfig["data"];
				for i in mfcd:
					if i["num"] == cnum:
						hpstr = i["hp"];
						attackstr = i["attack"];
						speedstr = i["speed"];
						break;
		if cfightdata and cfightconfig:
			lv = cfightdata.get("lv",0);
			name = cfightdata.get("mname",str(main));
			shape = cfightdata.get("shape",1000);
			hp = 1;
			attack = 1;
			speed = 1;
			if len(hpstr) > 0:
				exec("hp = "+hpstr);
				hp = int(hp);
			if len(attackstr) > 0:
				exec("attack = "+attackstr);
				attack = int(attack);
			if len(speedstr) > 0:
				exec("speed = "+speedstr);
				speed = int(speed);

			team_pos = app.combat.combat.COMBAT_POS_MAP[1];
			for i in xrange(0,count):
				if pos_idx >= len(team_pos):
					break;
				w_inst = app.combat.warrior.warrior(team_pos[pos_idx],team_pos[pos_idx],team_pos[pos_idx]);
				pos_idx = pos_idx + 1;
				w_inst['group'] = group;
				w_inst['hp'] = hp;
				w_inst['hpmax'] = hp;
				w_inst['atk'] = attack;
				w_inst['spd'] = speed;
				w_inst['name'] = name;
				w_inst['shape'] = shape;
			
				combat_inst.addwarrior(w_inst);
		return pos_idx
	def _combat_group(self,cid,group):
		groupcfg = fightgroup.create_Fightgroup(group);
		if not groupcfg:
			return
		group_data = groupcfg.data;
		cfg = group_data[0];#todo
		main = cfg["main"]
		mainnum = cfg["mainnum"];
		sub = cfg["sub"];
		subnum = cfg["subnum"];
		small = cfg["small"];
		smallnum = cfg["smallnum"];
		other = cfg["other"];
		othernum = cfg["othernum"];
		if mainnum + subnum + smallnum + othernum <= 0:
			return

		combat_inst = app.combat.combat.combat();
		combat_inst.parent = self;

		team_pos = app.combat.combat.COMBAT_POS_MAP[0];
		
		c_data = memmode.tb_character_admin.getObj(cid);
		if not c_data:
			log.msg('combat_main on_startcombat _combat_group fatal err %d'%(cid));
			return;
		c_info = c_data.get('data');
		staminia = c_info["staminia"];
		spirit = c_info["spirit"];
		dex = c_info["dex"];
		w_inst = app.combat.warrior.warrior(team_pos[0],team_pos[0],cid);
		w_inst['group'] = 0;
		w_inst['hp'] = staminia*3;
		w_inst['hpmax'] = staminia*3;
		w_inst['atk'] = spirit*2;
		w_inst['spd'] = dex*2;
		w_inst['name'] = c_info["nickname"];
		w_inst['shape'] = c_info["figure"];
		
		combat_inst.addwarrior(w_inst);

		pos_idx = 0;

		pos_idx = self._add_combatgroup_monster(combat_inst,1,pos_idx,main,mainnum,1)
		pos_idx = self._add_combatgroup_monster(combat_inst,1,pos_idx,sub,subnum,1)
		pos_idx = self._add_combatgroup_monster(combat_inst,1,pos_idx,small,smallnum,1)
		pos_idx = self._add_combatgroup_monster(combat_inst,1,pos_idx,other,othernum,1)

		combat_inst.start();
		while True:
			#combat_inst.addwarriorcmd();
			combat_inst.on_turn();
			if combat_inst.is_end():
				break;
		return
	def _combat_character(self,team1,team2):
		combat_inst = app.combat.combat.combat();
		combat_inst.parent = self;
		team_pos = app.combat.combat.COMBAT_POS_MAP[0];
		pos_idx = 0;
		for i in team1:
			c_data = memmode.tb_character_admin.getObj(i);
			if not c_data:
				log.msg('combat_main on_startcombat fatal err team1 %d'%(i));
				continue;
			c_info = c_data.get('data');
			staminia = c_info["staminia"];
			spirit = c_info["spirit"];
			dex = c_info["dex"];
			w_inst = app.combat.warrior.warrior(team_pos[pos_idx],team_pos[pos_idx],i);
			w_inst['group'] = 0;
			w_inst['hp'] = staminia*3;
			w_inst['hpmax'] = staminia*3;
			w_inst['atk'] = spirit*2;
			w_inst['spd'] = dex*2;
			w_inst['name'] = c_info["nickname"];
			w_inst['shape'] = c_info["figure"];
			
			combat_inst.addwarrior(w_inst);
			pos_idx = pos_idx + 1;

		team_pos = app.combat.combat.COMBAT_POS_MAP[1];
		pos_idx = 0;
		for i in team2:
			c_data = memmode.tb_character_admin.getObj(i);
			if not c_data:
				log.msg('combat_main on_startcombat fatal err team2 %d'%(i));
				continue;
			c_info = c_data.get('data');
			staminia = c_info["staminia"];
			spirit = c_info["spirit"];
			dex = c_info["dex"];
			w_inst = app.combat.warrior.warrior(team_pos[pos_idx],team_pos[pos_idx],i);
			w_inst['group'] = 1;
			w_inst['hp'] = staminia*3;
			w_inst['hpmax'] = staminia*3;
			w_inst['atk'] = spirit*2;
			w_inst['spd'] = dex*2;
			w_inst['name'] = c_info["nickname"];
			w_inst['shape'] = c_info["figure"];

			combat_inst.addwarrior(w_inst);
			pos_idx = pos_idx + 1;
		combat_inst.start();
		while True:
			#combat_inst.addwarriorcmd();
			combat_inst.on_turn();
			if combat_inst.is_end():
				break;
		return
	def on_startcombat(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];#发起者
		data = ud["data"];#team1:[],team2:[]
		tp = data['type'];
		if tp == 0:
			team1 = data['team1'];
			team2 = data['team2'];
			self._combat_character(team1,team2);
		elif tp == 1:
			group = data['group'];
			self._combat_group(cId,group);
		return
	def on_endcombat(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];#发起者
		data = ud["data"];
		return
	def on_war_playend(self,ud):
		dId = ud["dId"];
		cId = ud["cId"];#发起者
		data = ud["data"];
		return

	###send s2c packet start
	def gen_s2c_combat_start(self,wid,cid,ctype,csubtype,wlineup,cplaymode,cskip,cmaxbout):
		print "combat s2c start"
		#S2C_WAR_START id type subtype lineup playmode skip maxbout
		data = {};
		data['id'] = cid;
		data['type'] = ctype;
		data['subtype'] = csubtype;
		data['lineup'] = wlineup;
		data['playmode'] = cplaymode;
		data['skip'] = cskip;
		data['maxbout'] = cmaxbout;
		self._send2clientbycidlist(S2C_WAR_START,[wid],data);
		return
	def gen_s2c_combat_end(self,wid_list,force):
		print "combat s2c end"
		
		#S2C_WAR_END force
		self._send2clientbycidlist(S2C_WAR_PREEND,wid_list,{});
		self._send2clientbycidlist(S2C_WAR_END,wid_list,{"force":force});
		return
	def gen_s2c_turn_start(self,wid_list,bout):
		print "combat s2c turn start"
		#S2C_WAR_NEXT bout
		self._send2clientbycidlist(S2C_WAR_NEXT,wid_list,{"bout":bout});
		return
	def gen_s2c_turn_end(self,wid_list):
		print "combat s2c turn end"
		#S2C_WAR_TURN
		self._send2clientbycidlist(S2C_WAR_TURN,wid_list,{});
		return
	def gen_s2c_addwarrior(self,wid_list,wid,wt,wo,ws,wshape,wd,wg,wc,wname,wzoom):
		print "combat s2c addwarrior %s"%(wid)
		#S2C_WAR_ADD warid type owner status shape desc grade classes name zoomlvl
		data = {};
		data['warid'] = wid;
		data['type'] = wt;
		data['owner'] = wo;
		data['status'] = ws;
		data['shape'] = wshape;
		data['desc'] = wd;
		data['grade'] = wg;
		data['classes'] = wc;
		data['name'] = wname;
		data['zoomlvl'] = wzoom;
		self._send2clientbycidlist(S2C_WAR_ADD,wid_list,data);
		return
	def gen_s2c_delwarrior(self,wid_list,wid):
		print "combat s2c delwarrior %s"%(wid)
		#S2C_WAR_LEAVE id
		self._send2clientbycidlist(S2C_WAR_LEAVE,wid_list,{"warid":wid});
		return
	def gen_s2c_warrior_skillbegin(self,wid_list,wid,skill_id,skill_lv,rd,dst_list):
		print "combat s2c skillbegin %s %s %s %s"%(wid,skill_id,skill_lv,dst_list)
		#S2C_WAR_PERFORM att skillid lv round lsvic
		data = {};
		data['att'] = wid;
		data['skillid'] = skill_id;
		data['lv'] = skill_lv;
		data['round'] = rd;
		data['lsvic'] = dst_list;
		self._send2clientbycidlist(S2C_WAR_PERFORM,wid_list,data);
		return
	def gen_s2c_warrior_skillend(self,wid_list,wid):
		print "combat s2c skillend %s"%(wid)
		#S2C_WAR_PERFORM_END
		self._send2clientbycidlist(S2C_WAR_PERFORM_END,wid_list,{});
		return
	def gen_s2c_warrior_attackbegin(self,wid_list,wid,dst):
		#todo need code
		print "combat s2c attackbegin %s %s"%(wid,dst);
		#S2C_WAR_ATTACK_NORMAL att vic
		self._send2clientbycidlist(S2C_WAR_ATTACK_NORMAL,wid_list,{"att":wid,'vic':dst});
		return
	def gen_s2c_warrior_attackend(self,wid_list,wid):
		#todo need code
		print "combat s2c attackend %s"%(wid);
		#S2C_WAR_ATTACK_END
		self._send2clientbycidlist(S2C_WAR_ATTACK_END,wid_list,{});
		return
	def gen_s2c_warrior_buffcd_change(self,actor,buffobj):
		print "combat s2c buffcd change %s %s %s %s %s"%(actor['pos'],actor['group'],buffobj.id,buffobj.bid,buffobj.cd)
		return
	def gen_s2c_warrior_propchg(self,wid_list,wid,status,value):
		#gen s2c netpacket
		print "combat s2c warrior propchg %s %s %s"%(wid,status,value);
		#S2C_WAR_ATTACK_STATUS target status value
		self._send2clientbycidlist(S2C_WAR_ATTACK_STATUS,wid_list,{"target":wid,"status":status,'value':value});
		return
	def gen_s2c_warrior_dodge(self,actor,skill_id,skill_lv):
		#gen s2c netpacket
		#todo need code
		print "combat s2c warrior dodge %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv)
		return
	def gen_s2c_warrior_addbuff(self,actor,buffobj,skill_id,skill_lv):
		print "combat s2c warrior addbuff %s %s %s %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv,buffobj.id,buffobj.bid,buffobj.cd)
		#gen s2c netpacket
		#S2C_WAR_BUFF_ADD warid bid overlay bout datas
		return
	def gen_s2c_warrior_delbuff(self,actor,buffobj):
		#gen s2c netpacket
		print "combat s2c warrior delbuff %s %s %s %s"%(actor['pos'],actor['group'],buffobj.id,buffobj.bid);
		#S2C_WAR_BUFF_DEL bid
		return
	def gen_s2c_warrior_status(self,wid_list,wid,hprate):
		#todo need code
		print "combat s2c warrior status %s %s "%(wid,hprate);
		#S2C_WAR_STATUS id hprate
		self._send2clientbycidlist(S2C_WAR_STATUS,wid_list,{"warid":wid,'hprate':hprate});
		return
	def gen_s2c_warrior_partnerattack(self,wid_list,wid,vic):
		#todo need code
		print "combat s2c warrior partnerattack %s %s"%(wid,vic);
		#S2C_WAR_PARTNER_ATTACK partner vic
		self._send2clientbycidlist(S2C_WAR_PARTNER_ATTACK,wid_list,{"partner":wid,'vic':vic});
		return
	def gen_s2c_warrior_backattackbegin(self,wid_list,wid,skill_id,skill_lv,rd,dst_list):
		print "combat s2c backattackbegin %s %s %s %s"%(wid,skill_id,skill_lv,dst_list)
		#S2C_WAR_BACKATTACK att skillid lv round lsvic
		data = {};
		data['att'] = wid;
		data['skillid'] = skill_id;
		data['lv'] = skill_lv;
		data['round'] = rd;
		data['lsvic'] = dst_list;
		self._send2clientbycidlist(S2C_WAR_BACKATTACK,wid_list,data);
		return
	def gen_s2c_warrior_backattackend(self,wid_list,wid):
		print "combat s2c backattackend %s"%(wid)
		#S2C_WAR_BACKATTACK_END
		self._send2clientbycidlist(S2C_WAR_BACKATTACK_END,wid_list,{});
		return
	def gen_s2c_warrior_shake(self,wid_list,wid,vic):
		#todo need code
		print "combat s2c warrior shake %s %s"%(wid,vic);
		#S2C_WAR_SHAKE att vic
		self._send2clientbycidlist(S2C_WAR_SHAKE,wid_list,{"att":wid,'vic':vic});
		return
	def gen_s2c_warrior_protect(self,wid_list,wid,vic):
		#todo need code
		print "combat s2c warrior protect %s %s"%(wid,vic);
		#S2C_WAR_PROTECT protector vic
		self._send2clientbycidlist(S2C_WAR_PROTECT,wid_list,{"protector":protector,'vic':vic});
		return
	###send s2c packet end
	def dispose(self):
		super(combat_main,self).dispose();
		return
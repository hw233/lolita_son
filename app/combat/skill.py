#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import ctriger
import cproperty
import cbuff
import ceffect

import app.config.simpleskill as skillconfig
import buff
import app.config.fightskill as boutskillconfig
SKILLTYPE_ATTACK = 0;
SKILLTYPE_CURE = 1;
SKILLTYPE_FUZHU = 2;
SKILLTYPE_REVIVE = 3;
SKILLTYPE_FENGYIN = 4;
class skillbase(object):
	def __init__(self,sid,slv):
		self.sid = sid;
		self.slv = slv;
		self.stype = SKILLTYPE_ATTACK;#0 攻击 1 回复 2 辅助 3 复活 4 封印
		self.can_dodge = False;
		self.min_dstcnt = 1;
		self.max_dstcnt = 1;
		self.effect = "";
		self.groupid = 0;
		return
	def is_canrevive(self):
		return self.stype == SKILLTYPE_REVIVE;
	def is_candodge(self):
		return self.can_dodge
	def is_attacktype(self):
		return self.stype == SKILLTYPE_ATTACK;
	def get_effect(self):
		return self.effect;
class skill(skillbase):
	def __init__(self,sid,slv):
		super(skill,self).__init__(sid,slv);
		self.dst_buff_list = [];#buff:rate
		self.clr_dst_buff_list = [];#buff:rate
		self.src_buff_list = [];#buff:rate
		self.clr_src_buff_list = [];#buff:rate
		self.init();
		return
	def get_wrapperlist_bystate(self,state):
		return [];
	def _parse_bufflist(self,buff_str,b_add = False):
		ret = [];
		if buff_str != None and len(buff_str) > 0:
			blist = buff_str.split(';');
			for i in blist:
				bdlist = i.split(',');
				bid = int(float(bdlist[0]));
				brate = int(float(bdlist[1]));
				bcd = 0;
				if b_add:
					bcd = int(float(bdlist[2]));
				if bid >= 100:
					ret.append([buff.buff(bid,bcd),brate]);
				else:
					bgrouplist = buff.get_bufflist_bygroup(bid);
					for j in bgrouplist:
						j.cd = bcd;
						ret.append([j,brate]);
		return ret
	def init(self):
		skilldata = skillconfig.create_Simpleskill(self.sid);
		for i in skilldata.skilldata:
			if i.get('lv',0) == self.slv:
				self.min_dstcnt = i.get('targetmin',1);
				self.max_dstcnt = i.get('targetmax',1);
				self.effect = i.get('effect',"");
				self.groupid = i.get('group',0);
				self.stype = i.get('stype',0);
				addbuff = i.get('addbuff',"");
				self.dst_buff_list = self._parse_bufflist(addbuff,True)
				clrbuff = i.get('clrbuff',"");
				self.clr_dst_buff_list = self._parse_bufflist(clrbuff);
				addbuffself = i.get('addbuffself',"");
				self.src_buff_list = self._parse_bufflist(addbuffself,True);
				clrbuffself = i.get('clrbuffself',"");
				self.clr_src_buff_list = self._parse_bufflist(clrbuffself);
				return;
		return


class boutskill(skillbase):
	def __init__(self,sid,slv):
		super(boutskill,self).__init__(sid,slv);
		self.sstype = "";
		self.name = "";
		self.tm = 0;

		self.senegytp = "";
		self.enegytp = 0;#0 mp 1 sp 2 enegy
		self.enegy_num = 0;
		self.hp = 0;
		self.hp_min = 0;
		self.cd = 0;

		self.dst_self = 0;
		self.dst_selfpet = 0;
		self.dst_selffri = 0;
		self.dst_selffripet = 0;
		self.dst_summon = 0;
		self.dst_enemy = 0;
		self.dst_enemypet = 0;
		self.dst_enemymonster = 0;

		self.damage = 0;
		self.damage_rate = 1.0;

		self.hit = 0;
		self.spd = 1.0;

		self.sub_damage = 0;
		
		self.eff_list = [];#[prop,triger,rate,dst,value]
		self.buff_list = [];#[buff,triger,rate,dst,value,bout]

		self.wrapper_map = {};
		self.init();
		return
	def add_wrapper(self,wrapper):
		state = wrapper.get_triger_state();
		if not self.wrapper_map.has_key(state):
			self.wrapper_map[state] = [];
		self.wrapper_map[state].append(wrapper);
		return
	def get_wrapperlist_bystate(self,state):
		if self.wrapper_map.has_key(state):
			return self.wrapper_map[state];
		return [];
	def init(self):
		skilldata = boutskillconfig.create_Fightskill(self.sid);
		if skilldata == None:
			return
		self.sstype = skilldata.stype;
		if self.sstype == "治疗技能":
			self.stype = SKILLTYPE_CURE;
		elif self.sstype == "复活技能":
			self.stype = SKILLTYPE_REVIVE;
		elif self.sstype == "辅助技能":
			self.stype = SKILLTYPE_FUZHU;
		elif self.sstype == "封印技能":
			self.stype = SKILLTYPE_FENGYIN;
		else:
			self.stype = SKILLTYPE_ATTACK;
		if self.sstype == "物理技能":
			self.can_dodge = True;
		else:
			self.can_dodge = False;
		self.name = skilldata.name;
		self.tm = skilldata.time;
		for i in skilldata.data:
			if i.get('lv',0) == self.slv:
				self.min_dstcnt = i.get('min',1);
				self.max_dstcnt = i.get('max',1);
				self.senegytp = i.get('etype','');
				if self.senegytp == "mp":
					self.enegytp = 0;
				elif self.senegytp == "sp":
					self.enegytp = 1;
				else:
					self.enegytp = 2;
				self.enegy_num = i.get('enegy',0);
				self.hp = i.get('hp',0);
				self.hp_min = i.get('hpmin',0);
				self.cd = i.get("cd",0);

				self.dst_self = i.get("self",0);
				self.dst_selfpet = i.get("spet",0);
				self.dst_selffri = i.get("team",0);
				self.dst_selffripet = i.get("tpet",0);
				self.dst_summon = i.get("summon",0);
				self.dst_enemy = i.get("enemy",0);
				self.dst_enemypet = i.get("epet",0);
				self.dst_enemymonster = i.get("esummon",0);

				self.damage = i.get("atk",0);
				self.damage_rate = i.get("rate",0);

				self.hit = i.get("hit",0);
				self.spd = i.get("spd",0);

				self.sub_damage = i.get("subatk",0);

				effdata = i.get("effdata",[]);
				self.eff_list = [];#[prop,triger,rate,dst,value]
				self.buff_list = [];#[buff,triger,rate,dst,value,bout]
				for k in effdata:
					prop = k["efftype"];
					ptriger = k["efftime"];
					prate = k["effrate"];
					pdst = k["effdst"];
					pvalue = k["effvalue"];
					if prop != "无":
						pins = None;
						if not pins and ceffect.have_effect_by_name(prop):
							pins = ceffect.get_effect_by_name(prop);
						if not pins and cproperty.have_cprop_by_name(prop):
							pins = cproperty.get_cprop_by_name(prop);
						wrapper_ins = cwrapper.combatwrapper(pins,pvalue,prate,pdst,ctriger.get_triger_by_name(ptriger));
						self.eff_list.append(wrapper_ins);
						self.add_wrapper(wrapper_ins);
					buffdata = k["buffdata"];
					for j in buffdata:
						bname = j["buff"];
						btriger = j["bufftime"];
						brate = j["buffhit"];
						bdst = j["buffdst"];
						bvalue = j["buffvalue"];
						bbout = j["buffbout"];
						if buff.have_buff_byname(bname):
							bid = buff.get_buffbid_byname(bname);
							pins = buff.get_buffcfg(bid);
							wrapper_ins = cwrapper.combatbuffwrapper(pins,bvalue,brate,bdst,ctriger.get_triger_by_name(btriger),bbout);
							self.buff_list.append(wrapper_ins);
							self.add_wrapper(wrapper_ins);
						elif cbuff.have_cbuffeff_by_name(bname):
							pins = cbuff.get_cbuffeff_by_name(bname);
							wrapper_ins = cwrapper.combatbuffwrapper(pins,bvalue,brate,bdst,ctriger.get_triger_by_name(btriger),bbout);
							self.buff_list.append(wrapper_ins);
							self.add_wrapper(wrapper_ins);
		return

g_skill_config = {};
def create_skill(sid,slv):
	global g_skill_config
	key = sid*1000+slv;
	if g_skill_config.has_key(key) == False:
		g_skill_config[key] = skill(sid,slv);
	return g_skill_config[key];
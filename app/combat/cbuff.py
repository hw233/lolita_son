#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.fightbuffeffect as fightbuffeffect

g_buff_id_start = 0;
class buffbase(object):
	def __init__(self,bid,cd = 0):
		self.bid = bid;
		self.id = self._gen_id();
		self.cd = cd;#bout count
		self.value = "";
		self.count = 1;#overlap
		self.btype = 0;
		self.effect = "";
		self.groupid = 0;
		self.spd = 0;
		self.done = False;
		self.init();
		return;
	def _gen_id(self):
		global g_buff_id_start
		g_buff_id_start = g_buff_id_start + 1;
		return g_buff_id_start
	def gen_spd(self,actor_spd):
		return self.spd + actor_spd;
	def init(self):
		return
	def is_immediate(self):
		return self.btype == 0;
	def get_effect(self):
		return self.effect;
	def get_group(self):
		return self.groupid;
	def do(self,actor,combat_ins):
		return
	def clear(self,actor,combat_ins):
		return
class combatbuffeff(object):
	def __init__(self,bid):
		self.bid = bid;
		self.name = "";
		self.tp = "";
		self.refresh = 0;
		self.overlap = 1;
		return
	def gen_spd(self,actor_spd):
		return actor_spd;
	def do(self,actor,combat_ins,value,b_done = None):
		return
	def clear(self,actor,combat_ins,value,b_done = None):
		return
class hide_3109(combatbuffeff):
	def __init__(self,bid):
		super(hide_3109,self).__init__(bid);
		return
	def do(self,actor,combat_ins,value,b_done = None):
		actor['m_hide'] = True;
		return
	def clear(self,actor,combat_ins,value,b_done = None):
		actor['m_hide'] = False;
		return
class addhp_201(combatbuffeff):
	def __init__(self,bid):
		super(addhp_201,self).__init__(bid);
		return
	def do(self,actor,combat_ins,value,b_done = None):
		if value == None or len(value <= 0):
			return
		if combat_ins.is_warrior_dead(actor):
			return
		hpmax = actor['hpmax'];
		hp = actor['hp'];
		v = int(value);
		hp = hp + v;
		if hp > hpmax:
			hp = hpmax;
		actor['hp'] = hp;
		combat_ins.gen_s2c_warrior_propchg(None,None,0-v,actor,False,0,0,False);
		combat_ins.gen_s2c_warrior_status(actor);
		return
	def clear(self,actor,combat_ins,value,b_done = None):
		return
class subhp_202(combatbuffeff):
	def __init__(self,bid):
		super(subhp_202,self).__init__(bid);
		return
	def do(self,actor,combat_ins,value,b_done = None):
		if value == None or len(value <= 0):
			return
		if combat_ins.is_warrior_dead(actor):
			return
		old_prop = actor.get_restoreprop();
		hp = actor['hp'];
		v = int(value);
		hp = hp - v;
		if hp <= 0:
			hp = 0;
			if actor['cankickout']:
				actor['kickout'] = True;
				combat_ins.on_attack_flyout(actor,0);
			else:
				actor['dead'] = True;
				combat_ins.on_attack_dead(actor,0);
		actor['hp'] = hp;
		combat_ins.gen_s2c_warrior_propchg(old_prop,actor.get_restoreprop(),v,actor,False,0,0,False);
		combat_ins.gen_s2c_warrior_status(actor);
		return
	def clear(self,actor,combat_ins,value,b_done = None):
		return
def create_cbuffeff(tid,name,tp):
	if tid == 3109:
		ret = hide_3109(tid);
		ret.name = name;
		ret.tp = tp;
		return;
	if tid == 201:
		ret = addhp_201(tid);
		ret.name = name;
		ret.tp = tp;
		return;
	if tid == 202:
		ret = subhp_202(tid);
		ret.name = name;
		ret.tp = tp;
		return;
	ret = combatbuffeff(tid);
	ret.name = name;
	ret.tp = tp;
	return ret
g_cbuffeff_map = {};

def have_cbuffeff_by_name(name):
	global g_cbuffeff_map
	if g_cbuffeff_map.has_key(name):
		return True;
	for k,v in fightbuffeffect.fightbuffeffect_map.items():
		if v["name"] == name:
			return True;
	return False
def have_cbuffeff_by_bid(bid):
	if fightbuffeffect.fightbuffeffect_map.has_key(bid):
		return True
	return False
def get_cbuffeff_by_name(name):
	ret = None;
	global g_cbuffeff_map
	if g_cbuffeff_map.has_key(name):
		ret = g_cbuffeff_map[name];
	else:
		for k,v in fightbuffeffect.fightbuffeffect_map.items():
			if v["name"] == name:
				g_cbuffeff_map[name] = create_cbuffeff(k,v["name"],v["type"]);
				ret = g_cbuffeff_map[name];
				break;
	if not ret:
		ret = create_cbuffeff(0,"","");
	return ret;
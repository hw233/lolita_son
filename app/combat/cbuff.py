#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.fightbuffeffect as fightbuffeffect

class buffbase(object):
	def __init__(self,bid,cd = 0,inst_id = 0):
		self.bid = bid;
		self.id = inst_id;
		self.cd = cd;
		self.btype = 0;
		self.effect = "";
		self.groupid = 0;
		self.spd = 0;
		self.init();
		return;
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
	def do(self,actor):
		return
class combatbuffeff(buffbase):
	def __init__(self,bid,cd = 0,inst_id = 0):
		super(combatbuffeff,self).__init__(bid,cd,inst_id);
		self.name = "";
		self.tp = "";
		return
		
def create_cbuffeff(tid,name,tp):
	#if tid == 101:
	#	ret = XXXXX;
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
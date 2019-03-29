#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.fighteffecttime as fighteffecttime

COMBAT_TRIGER_ENTER = 1;
COMBAT_TRIGER_TURNSTART = 2;
COMBAT_TRIGER_SKILLSTART = 3;
COMBAT_TRIGER_ATK = 4;
COMBAT_TRIGER_HIT = 5;
COMBAT_TRIGER_MISS = 6;
COMBAT_TRIGER_FLYOUT = 7;
COMBAT_TRIGER_DEAD = 8;
COMBAT_TRIGER_SKILLEND = 9;
COMBAT_TRIGER_TURNEND = 10;

class combattriger(object):
	def __init__(self,tid,name):
		self.id = tid;
		self.name = name;
		return
	def get_id(self):
		return self.id;
	def is_triger(self,tid):
		return tid == self.id;

def create_triger(tid,name):
	return combattriger(tid,name)
g_triger_map = {};

def get_triger_by_name(name):
	global g_triger_map
	if g_triger_map.has_key(name):
		return g_triger_map[name];
	else:
		for k,v in fighteffecttime.fighteffecttime_map.items():
			if v["name"] == name:
				g_triger_map[name] = create_triger(k,name);
				return g_triger_map[name];
	return create_triger(0,"");
def get_triger_by_id(id):
	global g_triger_map
	for k,v in g_triger_map.items():
		if v.id == id:
			return v;
	for k,v in fighteffecttime.fighteffecttime_map.items():
		if k == id:
			name = v["name"]
			g_triger_map[name] = create_triger(k,name);
			return g_triger_map[name];
	return create_triger(0,"");
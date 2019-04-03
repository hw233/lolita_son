#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.fightprop as fightprop

class combatprop(object):
	def __init__(self,tid,name,key):
		self.id = tid;
		self.name = name;
		self.key = key;
		self.spd = 0;
		return
	def gen_spd(self,actor_spd):
		return self.spd + actor_spd;
	def do(self,*args):
		return
	
def create_cprop(tid,name,key):
	return combatprop(tid,name,key)
g_cprop_map = {};


def have_cprop_by_name(name):
	global g_cprop_map
	if g_cprop_map.has_key(name):
		return True;
	for k,v in fightprop.fightprop_map.items():
		if v["name"] == name:
			return True;
	return False

def get_cprop_by_name(name):
	ret = None;
	global g_cprop_map
	if g_cprop_map.has_key(name):
		ret = g_cprop_map[name];
	else:
		for k,v in fightprop.fightprop_map.items():
			if v["name"] == name:
				g_cprop_map[name] = create_cprop(k,v["name"],v["key"]);
				ret = g_cprop_map[name];
				break;
	if not ret:
		ret = create_cprop(0,"","");
	return ret;
#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.fighteffect as fighteffect

class combateffect(object):
	def __init__(self,tid,name):
		self.id = tid;
		self.name = name;
		return
	def do(self,*args):
		return

def create_effect(tid,name):
	return combateffect(tid,name)
g_effect_map = {};

def have_effect_by_name(name):
	global g_effect_map
	if g_effect_map.has_key(name):
		return True;
	for k,v in fighteffect.fighteffect_map.items():
		if v["name"] == name:
			return True;
	return False;
def get_effect_by_name(name):
	ret = None;
	global g_effect_map
	if g_effect_map.has_key(name):
		ret = g_effect_map[name];
	else:
		for k,v in fighteffect.fighteffect_map.items():
			if v["name"] == name:
				g_effect_map[name] = create_effect(k,v["name"]);
				ret = g_effect_map[name];
				break;
	if not ret:
		ret = create_effect(0,"");
	return ret;
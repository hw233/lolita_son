#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.fighteffecttime as fighteffecttime

class combattriger(object):
	def __init__(self,tid,name):
		self.id = tid;
		self.name = name;
		return
	def is_triger(self,tid):
		if self.id == 0:
			return True;
		return tid == self.id;

def create_triger(tid,name):
	return combattriger(tid,name)
g_triger_map = {};

def get_triger_by_name(name):
	ret = None;
	global g_triger_map
	if g_triger_map.has_key(name):
		ret = g_triger_map[name];
	else:
		for k,v in fighteffecttime.fighteffecttime_map.items():
			if v["name"] == name:
				g_triger_map[name] = create_triger(k,v["name"]);
				ret = g_triger_map[name];
				break;
	if not ret:
		ret = create_triger(0,"");
	return ret;
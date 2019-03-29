#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.fightbuffeffect as fightbuffeffect

class combatbuffeff(object):
	def __init__(self,tid,name,tp):
		self.id = tid;
		self.name = name;
		self.tp = tp;
		return
	def do(self,*args):
		return
		
def create_cbuffeff(tid,name,tp):
	return combatbuffeff(tid,name,tp)
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
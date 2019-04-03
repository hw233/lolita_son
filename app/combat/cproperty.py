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

class hpmaxadd_1(combatprop):
	def __init__(self,tid,name,key):
		super(hpmaxadd_1,self).__init__(tid,name,key);
		return
class mpmaxadd_2(combatprop):
	def __init__(self,tid,name,key):
		super(mpmaxadd_2,self).__init__(tid,name,key);
		return
class atkadd_3(combatprop):
	def __init__(self,tid,name,key):
		super(atkadd_3,self).__init__(tid,name,key);
		return
class defaddbylv_4(combatprop):
	def __init__(self,tid,name,key):
		super(defaddbylv_4,self).__init__(tid,name,key);
		return
class sense_5(combatprop):
	def __init__(self,tid,name,key):
		super(sense_5,self).__init__(tid,name,key);
		return
class atkseal_6(combatprop):
	def __init__(self,tid,name,key):
		super(atkseal_6,self).__init__(tid,name,key);
		return
class mgcatkseal_7(combatprop):
	def __init__(self,tid,name,key):
		super(mgcatkseal_7,self).__init__(tid,name,key);
		return

def create_cprop(tid,name,key):
	if tid == 1:
		return hpmaxadd_1(tid,name,key);
	if tid == 2:
		return mpmaxadd_2(tid,name,key);
	if tid == 3:
		return atkadd_3(tid,name,key);
	if tid == 4:
		return defaddbylv_4(tid,name,key);
	if tid == 5:
		return sense_5(tid,name,key);
	if tid == 6:
		return atkseal_6(tid,name,key);
	if tid == 7:
		return mgcatkseal_7(tid,name,key);
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
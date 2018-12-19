# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


skillpassive_map = {};
skillpassive_map[2001] = {"id":2001,"skilldata":[{"lv":1,"effect":"actor['atk']*=1.2","group":1,},{"lv":2,"effect":"actor['atk']*=1.3","group":1,},{"lv":3,"effect":"actor['atk']*=1.4","group":1,},],};
skillpassive_map[2002] = {"id":2002,"skilldata":[{"lv":1,"effect":"actor['spd']+=20","group":1,},{"lv":2,"effect":"actor['spd']+=30","group":1,},],};
skillpassive_map[2003] = {"id":2003,"skilldata":[{"lv":1,"effect":"actor['hpmax']*=1.2","group":1,},],};


class Skillpassive:
	def __init__(self, key):
		config = skillpassive_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Skillpassive(key):
		config = skillpassive_map.get(key);
		if not config:
			return
		return Skillpassive(key)


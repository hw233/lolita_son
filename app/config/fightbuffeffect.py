# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightbuffeffect_map = {};
fightbuffeffect_map[201] = {"id":201,"type":"","name":"持续加血",};
fightbuffeffect_map[3109] = {"id":3109,"type":"","name":"隐匿",};
fightbuffeffect_map[202] = {"id":202,"type":"","name":"持续减血",};


class Fightbuffeffect:
	def __init__(self, key):
		config = fightbuffeffect_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightbuffeffect(key):
		config = fightbuffeffect_map.get(key);
		if not config:
			return
		return Fightbuffeffect(key)


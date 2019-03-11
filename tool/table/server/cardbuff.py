# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


cardbuff_map = {};
cardbuff_map[1001] = {"id":1001,"btype":0,"effect":"actor['hpmax']*=1.2","group":1,};
cardbuff_map[1002] = {"id":1002,"btype":0,"effect":"actor['spd']+=20","group":1,};
cardbuff_map[1003] = {"id":1003,"btype":0,"effect":"actor['atk']+=20","group":1,};
cardbuff_map[1004] = {"id":1004,"btype":0,"effect":"actor['def']+=20","group":1,};


class Cardbuff:
	def __init__(self, key):
		config = cardbuff_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Cardbuff(key):
		config = cardbuff_map.get(key);
		if not config:
			return
		return Cardbuff(key)


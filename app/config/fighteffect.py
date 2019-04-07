# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fighteffect_map = {};
fighteffect_map[1001] = {"id":1001,"name":"复活",};
fighteffect_map[1006] = {"id":1006,"name":"吸血",};
fighteffect_map[1038] = {"id":1038,"name":"清除buff",};


class Fighteffect:
	def __init__(self, key):
		config = fighteffect_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fighteffect(key):
		config = fighteffect_map.get(key);
		if not config:
			return
		return Fighteffect(key)


# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightdungeon_map = {};


class Fightdungeon:
	def __init__(self, key):
		config = fightdungeon_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightdungeon(key):
		config = fightdungeon_map.get(key);
		if not config:
			return
		return Fightdungeon(key)


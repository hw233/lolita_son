# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


cards_dungeon_map = {};
cards_dungeon_map[1] = {"lv":1,"min":6,"max":16,"equip_group":"1,2","equip_min":2,"equip_max":3,"spell_group":"7.0","spell_min":1,"spell_max":3,"trap_group":"8.0","trap_min":1,"trap_max":2,"monster_group":"3,4,5,6",};


class Cards_dungeon:
	def __init__(self, key):
		config = cards_dungeon_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Cards_dungeon(key):
		config = cards_dungeon_map.get(key);
		if not config:
			return
		return Cards_dungeon(key)


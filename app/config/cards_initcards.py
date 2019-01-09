# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


cards_initcards_map = {};
cards_initcards_map[1] = {"lv":1,"count":5,"equip_group":"1,2","equip_min":1,"equip_max":4,"spell_group":"7.0",};


class Cards_initcards:
	def __init__(self, key):
		config = cards_initcards_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Cards_initcards(key):
		config = cards_initcards_map.get(key);
		if not config:
			return
		return Cards_initcards(key)


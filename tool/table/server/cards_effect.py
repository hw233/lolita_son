# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


cards_effect_map = {};
cards_effect_map[101] = {"id":101,"type":"addhp","desc":"加血(与攻击无关，按填值增加)",};
cards_effect_map[102] = {"id":102,"type":"subhp","desc":"减血(与攻击无关，按填值减少)",};
cards_effect_map[103] = {"id":103,"type":"addstamina","desc":"增加体力",};
cards_effect_map[104] = {"id":104,"type":"substamina","desc":"减少体力",};
cards_effect_map[105] = {"id":105,"type":"charm","desc":"魅惑",};
cards_effect_map[106] = {"id":106,"type":"vanish","desc":"盖住所有牌",};
cards_effect_map[107] = {"id":107,"type":"scout","desc":"翻开所有牌",};
cards_effect_map[108] = {"id":108,"type":"berserk","desc":"狂暴,数值为已减血量",};
cards_effect_map[109] = {"id":109,"type":"addarmor","desc":"加甲",};
cards_effect_map[110] = {"id":110,"type":"subarmor","desc":"减甲",};
cards_effect_map[199] = {"id":199,"type":"next","desc":"进入下一关",};


class Cards_effect:
	def __init__(self, key):
		config = cards_effect_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Cards_effect(key):
		config = cards_effect_map.get(key);
		if not config:
			return
		return Cards_effect(key)


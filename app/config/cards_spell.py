# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


cards_spell_map = {};
cards_spell_map[10001] = {"id":10001,"effect":"101.0","dst":"0.0","data":"5.0","desc":"加血",};
cards_spell_map[10002] = {"id":10002,"effect":"102.0","dst":"0.0","data":"1.0","desc":"陷阱减血",};
cards_spell_map[10003] = {"id":10003,"effect":"103.0","dst":"0.0","data":"99.0","desc":"增加体力",};
cards_spell_map[10004] = {"id":10004,"effect":"104.0","dst":"0.0","data":"1.0","desc":"陷阱减少体力",};
cards_spell_map[10005] = {"id":10005,"effect":"101,102.0","dst":"0,1","data":"2,2","desc":"吸血",};
cards_spell_map[10006] = {"id":10006,"effect":"105.0","dst":"1.0","desc":"魅惑",};
cards_spell_map[10007] = {"id":10007,"effect":"106.0","desc":"盖住所有牌",};
cards_spell_map[10008] = {"id":10008,"effect":"107.0","desc":"打开所有牌",};
cards_spell_map[10009] = {"id":10009,"effect":"101.0","dst":"2.0","data":"99.0","desc":"恐惧",};
cards_spell_map[10010] = {"id":10010,"effect":"101,104.0","dst":"0,0","data":"99,99","desc":"休息",};
cards_spell_map[10011] = {"id":10011,"effect":"108.0","dst":"2.0","desc":"狂暴",};
cards_spell_map[19999] = {"id":19999,"effect":"199,103.0","dst":"0,0.0","data":"0,1","desc":"进入下一关",};


class Cards_spell:
	def __init__(self, key):
		config = cards_spell_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Cards_spell(key):
		config = cards_spell_map.get(key);
		if not config:
			return
		return Cards_spell(key)


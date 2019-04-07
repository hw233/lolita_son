# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightbuff_map = {};
fightbuff_map[1001] = {"id":1001,"name":"强壮","type":"增益","refresh":1,"count":3,"data":[{"prop":"气血增加","value":"1000.0",},],};
fightbuff_map[1002] = {"id":1002,"name":"强力","type":"增益","refresh":1,"count":1,"data":[{"prop":"攻击增加","value":"100.0",},],};


class Fightbuff:
	def __init__(self, key):
		config = fightbuff_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightbuff(key):
		config = fightbuff_map.get(key);
		if not config:
			return
		return Fightbuff(key)


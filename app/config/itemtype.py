# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


itemtype_map = {};
itemtype_map[1] = {"id":1,"tp":"装备","d1":"位置","d2":"攻击","d3":"防御","d4":"血量","d5":"速度","d6":"","d7":"","d8":"",};
itemtype_map[2] = {"id":2,"tp":"经验","d1":"数值","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
itemtype_map[3] = {"id":3,"tp":"金币","d1":"数值","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};


class Itemtype:
	def __init__(self, key):
		config = itemtype_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Itemtype(key):
		config = itemtype_map.get(key);
		if not config:
			return
		return Itemtype(key)


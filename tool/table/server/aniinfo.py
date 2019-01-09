# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


aniinfo_map = {};
aniinfo_map[1001] = {"id":1001,"w":512,"h":512,"path":"xiannv/xiannv2.atlas","total":16,"speed":30,"prefix":"xiannv2/",};


class Aniinfo:
	def __init__(self, key):
		config = aniinfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Aniinfo(key):
		config = aniinfo_map.get(key);
		if not config:
			return
		return Aniinfo(key)


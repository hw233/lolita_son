# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


skininfo_map = {};
skininfo_map[1] = {"id":1,"aid":201,};
skininfo_map[2] = {"id":2,"aid":211,};
skininfo_map[3] = {"id":3,"aid":221,};
skininfo_map[4] = {"id":4,"aid":231,};
skininfo_map[5] = {"id":5,"aid":241,};


class Skininfo:
	def __init__(self, key):
		config = skininfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Skininfo(key):
		config = skininfo_map.get(key);
		if not config:
			return
		return Skininfo(key)


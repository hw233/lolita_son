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
skininfo_map[6] = {"id":6,"aid":251,};
skininfo_map[7] = {"id":7,"aid":261,};
skininfo_map[8] = {"id":8,"aid":271,};
skininfo_map[9] = {"id":9,"aid":281,};
skininfo_map[10] = {"id":10,"aid":291,};
skininfo_map[11] = {"id":11,"aid":301,};
skininfo_map[12] = {"id":12,"aid":311,};
skininfo_map[13] = {"id":13,"aid":321,};
skininfo_map[14] = {"id":14,"aid":331,};
skininfo_map[15] = {"id":15,"aid":341,};
skininfo_map[16] = {"id":16,"aid":351,};
skininfo_map[17] = {"id":17,"aid":361,};
skininfo_map[18] = {"id":18,"aid":371,};
skininfo_map[19] = {"id":19,"aid":381,};
skininfo_map[20] = {"id":20,"aid":391,};


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


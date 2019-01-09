# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


itemmerge_map = {};
itemmerge_map[1002] = {"shape":1002,"src1":1001,"src2":1001,};
itemmerge_map[1003] = {"shape":1003,"src1":1002,"src2":1002,};
itemmerge_map[1004] = {"shape":1004,"src1":1003,"src2":1003,};
itemmerge_map[1005] = {"shape":1005,"src1":1004,"src2":1004,};
itemmerge_map[1006] = {"shape":1006,"src1":1005,"src2":1005,};
itemmerge_map[1007] = {"shape":1007,"src1":1006,"src2":1006,};
itemmerge_map[1008] = {"shape":1008,"src1":1007,"src2":1007,};
itemmerge_map[1009] = {"shape":1009,"src1":1008,"src2":1008,};
itemmerge_map[1010] = {"shape":1010,"src1":1009,"src2":1009,};
itemmerge_map[1011] = {"shape":1011,"src1":1010,"src2":1010,};
itemmerge_map[1012] = {"shape":1012,"src1":1011,"src2":1011,};


class Itemmerge:
	def __init__(self, key):
		config = itemmerge_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Itemmerge(key):
		config = itemmerge_map.get(key);
		if not config:
			return
		return Itemmerge(key)


# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


buffinfo_map = {};
buffinfo_map[1] = {"id":1,"aid":30003,"icon":0,};
buffinfo_map[201] = {"id":201,"aid":30001,"icon":201,};
buffinfo_map[202] = {"id":202,"aid":30002,"icon":202,};
buffinfo_map[1001] = {"id":1001,"aid":30004,"icon":1001,};
buffinfo_map[1002] = {"id":1002,"aid":30005,"icon":1002,};


class Buffinfo:
	def __init__(self, key):
		config = buffinfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Buffinfo(key):
		config = buffinfo_map.get(key);
		if not config:
			return
		return Buffinfo(key)


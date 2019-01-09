# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


buffinfo_map = {};
buffinfo_map[1] = {"id":1,"aid":30003,"icon":0,};
buffinfo_map[101] = {"id":101,"aid":30001,"icon":1001,};
buffinfo_map[102] = {"id":102,"aid":30002,"icon":1002,};


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


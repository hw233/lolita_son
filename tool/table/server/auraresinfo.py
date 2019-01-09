# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


auraresinfo_map = {};
auraresinfo_map[1] = {"id":1,"aid":10001,};
auraresinfo_map[2] = {"id":2,"aid":10002,};
auraresinfo_map[3] = {"id":3,"aid":10003,};
auraresinfo_map[4] = {"id":4,"aid":10004,};
auraresinfo_map[5] = {"id":5,"aid":10005,};
auraresinfo_map[6] = {"id":6,"aid":10006,};
auraresinfo_map[7] = {"id":7,"aid":10007,};
auraresinfo_map[8] = {"id":8,"aid":10008,};
auraresinfo_map[9] = {"id":9,"aid":10009,};
auraresinfo_map[10] = {"id":10,"aid":10010,};
auraresinfo_map[11] = {"id":11,"aid":10011,};
auraresinfo_map[12] = {"id":12,"aid":10012,};
auraresinfo_map[13] = {"id":13,"aid":10013,};
auraresinfo_map[14] = {"id":14,"aid":10014,};
auraresinfo_map[15] = {"id":15,"aid":10015,};
auraresinfo_map[64] = {"id":64,"aid":10001,};
auraresinfo_map[65] = {"id":65,"aid":10002,};
auraresinfo_map[66] = {"id":66,"aid":10003,};
auraresinfo_map[67] = {"id":67,"aid":10004,};
auraresinfo_map[68] = {"id":68,"aid":10005,};
auraresinfo_map[69] = {"id":69,"aid":10006,};
auraresinfo_map[70] = {"id":70,"aid":10007,};
auraresinfo_map[71] = {"id":71,"aid":10008,};
auraresinfo_map[72] = {"id":72,"aid":10009,};
auraresinfo_map[73] = {"id":73,"aid":10010,};
auraresinfo_map[74] = {"id":74,"aid":10011,};
auraresinfo_map[75] = {"id":75,"aid":10012,};
auraresinfo_map[76] = {"id":76,"aid":10013,};
auraresinfo_map[77] = {"id":77,"aid":10014,};
auraresinfo_map[78] = {"id":78,"aid":10015,};


class Auraresinfo:
	def __init__(self, key):
		config = auraresinfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Auraresinfo(key):
		config = auraresinfo_map.get(key);
		if not config:
			return
		return Auraresinfo(key)


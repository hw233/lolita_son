# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


winginfo_map = {};
winginfo_map[1] = {"id":1,"aid":40001,};
winginfo_map[2] = {"id":2,"aid":40002,};
winginfo_map[3] = {"id":3,"aid":40003,};
winginfo_map[4] = {"id":4,"aid":40004,};
winginfo_map[5] = {"id":5,"aid":40005,};
winginfo_map[6] = {"id":6,"aid":40006,};
winginfo_map[7] = {"id":7,"aid":40007,};
winginfo_map[8] = {"id":8,"aid":40008,};
winginfo_map[9] = {"id":9,"aid":40009,};
winginfo_map[10] = {"id":10,"aid":40010,};
winginfo_map[11] = {"id":11,"aid":40011,};
winginfo_map[12] = {"id":12,"aid":40012,};
winginfo_map[13] = {"id":13,"aid":40013,};
winginfo_map[14] = {"id":14,"aid":40014,};
winginfo_map[15] = {"id":15,"aid":40015,};
winginfo_map[16] = {"id":16,"aid":40002,};
winginfo_map[17] = {"id":17,"aid":40003,};
winginfo_map[18] = {"id":18,"aid":40004,};
winginfo_map[19] = {"id":19,"aid":40005,};
winginfo_map[20] = {"id":20,"aid":40006,};
winginfo_map[128] = {"id":128,"aid":40016,};
winginfo_map[129] = {"id":129,"aid":40017,};
winginfo_map[130] = {"id":130,"aid":40018,};
winginfo_map[131] = {"id":131,"aid":40019,};
winginfo_map[132] = {"id":132,"aid":40021,};
winginfo_map[133] = {"id":133,"aid":40022,};
winginfo_map[134] = {"id":134,"aid":40020,};
winginfo_map[135] = {"id":135,"aid":40023,};
winginfo_map[136] = {"id":136,"aid":40024,};
winginfo_map[137] = {"id":137,"aid":40025,};
winginfo_map[138] = {"id":138,"aid":40026,};
winginfo_map[139] = {"id":139,"aid":40027,};
winginfo_map[140] = {"id":140,"aid":40028,};


class Winginfo:
	def __init__(self, key):
		config = winginfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Winginfo(key):
		config = winginfo_map.get(key);
		if not config:
			return
		return Winginfo(key)


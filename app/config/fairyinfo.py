# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fairyinfo_map = {};
fairyinfo_map[1] = {"id":1,"aid":50003,};
fairyinfo_map[2] = {"id":2,"aid":50001,};
fairyinfo_map[3] = {"id":3,"aid":50004,};
fairyinfo_map[4] = {"id":4,"aid":50008,};
fairyinfo_map[5] = {"id":5,"aid":50002,};
fairyinfo_map[6] = {"id":6,"aid":50009,};
fairyinfo_map[7] = {"id":7,"aid":50005,};
fairyinfo_map[8] = {"id":8,"aid":50006,};
fairyinfo_map[9] = {"id":9,"aid":50015,};
fairyinfo_map[10] = {"id":10,"aid":50011,};
fairyinfo_map[11] = {"id":11,"aid":50013,};
fairyinfo_map[12] = {"id":12,"aid":50014,};
fairyinfo_map[13] = {"id":13,"aid":50007,};
fairyinfo_map[14] = {"id":14,"aid":50012,};
fairyinfo_map[15] = {"id":15,"aid":50010,};
fairyinfo_map[16] = {"id":16,"aid":50011,};
fairyinfo_map[17] = {"id":17,"aid":50012,};
fairyinfo_map[18] = {"id":18,"aid":50013,};
fairyinfo_map[19] = {"id":19,"aid":50014,};
fairyinfo_map[20] = {"id":20,"aid":50015,};
fairyinfo_map[64] = {"id":64,"aid":50064,};
fairyinfo_map[65] = {"id":65,"aid":50065,};
fairyinfo_map[66] = {"id":66,"aid":50066,};
fairyinfo_map[67] = {"id":67,"aid":50067,};
fairyinfo_map[68] = {"id":68,"aid":50068,};
fairyinfo_map[69] = {"id":69,"aid":50069,};
fairyinfo_map[70] = {"id":70,"aid":50070,};
fairyinfo_map[71] = {"id":71,"aid":50071,};
fairyinfo_map[72] = {"id":72,"aid":50072,};
fairyinfo_map[73] = {"id":73,"aid":50073,};
fairyinfo_map[74] = {"id":74,"aid":50074,};
fairyinfo_map[75] = {"id":75,"aid":50075,};
fairyinfo_map[76] = {"id":76,"aid":50076,};
fairyinfo_map[77] = {"id":77,"aid":50077,};
fairyinfo_map[78] = {"id":78,"aid":50078,};
fairyinfo_map[79] = {"id":79,"aid":50074,};
fairyinfo_map[80] = {"id":80,"aid":50075,};
fairyinfo_map[81] = {"id":81,"aid":50076,};
fairyinfo_map[82] = {"id":82,"aid":50077,};
fairyinfo_map[83] = {"id":83,"aid":50078,};
fairyinfo_map[128] = {"id":128,"aid":50016,};
fairyinfo_map[129] = {"id":129,"aid":50017,};
fairyinfo_map[130] = {"id":130,"aid":50018,};
fairyinfo_map[131] = {"id":131,"aid":50019,};
fairyinfo_map[132] = {"id":132,"aid":50016,};
fairyinfo_map[133] = {"id":133,"aid":50016,};


class Fairyinfo:
	def __init__(self, key):
		config = fairyinfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fairyinfo(key):
		config = fairyinfo_map.get(key);
		if not config:
			return
		return Fairyinfo(key)


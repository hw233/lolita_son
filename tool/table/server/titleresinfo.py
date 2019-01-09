# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


titleresinfo_map = {};
titleresinfo_map[1] = {"id":1,"aid":20001,};
titleresinfo_map[2] = {"id":2,"aid":20002,};
titleresinfo_map[3] = {"id":3,"aid":20003,};
titleresinfo_map[4] = {"id":4,"aid":20004,};
titleresinfo_map[5] = {"id":5,"aid":20005,};
titleresinfo_map[6] = {"id":6,"aid":20006,};
titleresinfo_map[7] = {"id":7,"aid":20007,};
titleresinfo_map[8] = {"id":8,"aid":20008,};
titleresinfo_map[9] = {"id":9,"aid":20009,};
titleresinfo_map[10] = {"id":10,"aid":20010,};
titleresinfo_map[11] = {"id":11,"aid":20011,};
titleresinfo_map[12] = {"id":12,"aid":20012,};
titleresinfo_map[13] = {"id":13,"aid":20013,};
titleresinfo_map[14] = {"id":14,"aid":20014,};
titleresinfo_map[15] = {"id":15,"aid":20015,};
titleresinfo_map[16] = {"id":16,"aid":20011,};
titleresinfo_map[17] = {"id":17,"aid":20012,};
titleresinfo_map[18] = {"id":18,"aid":20013,};
titleresinfo_map[19] = {"id":19,"aid":20014,};
titleresinfo_map[20] = {"id":20,"aid":20015,};
titleresinfo_map[64] = {"id":64,"aid":20017,};
titleresinfo_map[65] = {"id":65,"aid":20016,};
titleresinfo_map[66] = {"id":66,"aid":20018,};
titleresinfo_map[67] = {"id":67,"aid":20019,};
titleresinfo_map[68] = {"id":68,"aid":20020,};
titleresinfo_map[69] = {"id":69,"aid":20021,};
titleresinfo_map[70] = {"id":70,"aid":20022,};
titleresinfo_map[71] = {"id":71,"aid":20023,};
titleresinfo_map[72] = {"id":72,"aid":20024,};
titleresinfo_map[73] = {"id":73,"aid":20025,};
titleresinfo_map[74] = {"id":74,"aid":20026,};
titleresinfo_map[75] = {"id":75,"aid":20027,};
titleresinfo_map[76] = {"id":76,"aid":20028,};
titleresinfo_map[77] = {"id":77,"aid":20029,};
titleresinfo_map[78] = {"id":78,"aid":20030,};
titleresinfo_map[79] = {"id":79,"aid":20031,};
titleresinfo_map[80] = {"id":80,"aid":20032,};
titleresinfo_map[81] = {"id":81,"aid":20033,};
titleresinfo_map[160] = {"id":160,"aid":20060,};
titleresinfo_map[161] = {"id":161,"aid":20061,};
titleresinfo_map[162] = {"id":162,"aid":20062,};
titleresinfo_map[163] = {"id":163,"aid":20063,};
titleresinfo_map[164] = {"id":164,"aid":20064,};
titleresinfo_map[165] = {"id":165,"aid":20065,};
titleresinfo_map[166] = {"id":166,"aid":20066,};
titleresinfo_map[167] = {"id":167,"aid":20067,};
titleresinfo_map[168] = {"id":168,"aid":20068,};
titleresinfo_map[169] = {"id":169,"aid":20069,};
titleresinfo_map[170] = {"id":170,"aid":20070,};
titleresinfo_map[171] = {"id":171,"aid":20071,};
titleresinfo_map[172] = {"id":172,"aid":20072,};
titleresinfo_map[173] = {"id":173,"aid":20073,};
titleresinfo_map[174] = {"id":174,"aid":20074,};


class Titleresinfo:
	def __init__(self, key):
		config = titleresinfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Titleresinfo(key):
		config = titleresinfo_map.get(key);
		if not config:
			return
		return Titleresinfo(key)


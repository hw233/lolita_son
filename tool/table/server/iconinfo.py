# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


iconinfo_map = {};
iconinfo_map["item"] = {"type":"item","data":[{"file":"res/atlas/icon/item/1.atlas","prefix":"icon/item/1/","start":0,"end":9999,},{"file":"res/atlas/icon/item/2.atlas","prefix":"icon/item/2/","start":10000,"end":10049,},{"file":"res/atlas/icon/item/3.atlas","prefix":"icon/item/3/","start":10050,"end":10099,},{"file":"res/atlas/icon/item/4.atlas","prefix":"icon/item/4/","start":10100,"end":10999,},{"file":"res/atlas/icon/item/5.atlas","prefix":"icon/item/5/","start":11000,"end":13999,},{"file":"res/atlas/icon/item/6.atlas","prefix":"icon/item/6/","start":14000,"end":49999,},{"file":"res/atlas/icon/item/7.atlas","prefix":"icon/item/7/","start":50000,"end":50039,},{"file":"res/atlas/icon/item/8.atlas","prefix":"icon/item/8/","start":50040,"end":50079,},{"file":"res/atlas/icon/item/9.atlas","prefix":"icon/item/9/","start":50080,"end":50999,},{"file":"res/atlas/icon/item/10.atlas","prefix":"icon/item/10/","start":51000,"end":51039,},{"file":"res/atlas/icon/item/11.atlas","prefix":"icon/item/11/","start":51040,"end":51079,},{"file":"res/atlas/icon/item/12.atlas","prefix":"icon/item/12/","start":51080,"end":51999,},{"file":"res/atlas/icon/item/13.atlas","prefix":"icon/item/13/","start":52000,"end":52999,},],};
iconinfo_map["head"] = {"type":"head","data":[{"file":"res/atlas/icon/head/1.atlas","prefix":"icon/head/1/","start":0,"end":1022,},{"file":"res/atlas/icon/head/2.atlas","prefix":"icon/head/2/","start":1023,"end":99999,},],};
iconinfo_map["buff"] = {"type":"buff","data":[{"file":"res/atlas/icon/buff.atlas","prefix":"icon/buff/","start":0,"end":99999,},],};
iconinfo_map["skill"] = {"type":"skill","data":[{"file":"res/atlas/icon/skill/1.atlas","prefix":"icon/skill/1/","start":0,"end":1999,},{"file":"res/atlas/icon/skill/2.atlas","prefix":"icon/skill/2/","start":2000,"end":2999,},{"file":"res/atlas/icon/skill/3.atlas","prefix":"icon/skill/3/","start":3000,"end":3999,},{"file":"res/atlas/icon/skill/4.atlas","prefix":"icon/skill/4/","start":4000,"end":99999,},],};
iconinfo_map["other"] = {"type":"other","data":[{"file":"res/atlas/icon/other.atlas","prefix":"icon/other/","start":0,"end":99999,},],};


class Iconinfo:
	def __init__(self, key):
		config = iconinfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Iconinfo(key):
		config = iconinfo_map.get(key);
		if not config:
			return
		return Iconinfo(key)


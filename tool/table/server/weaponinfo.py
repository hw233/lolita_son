# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


weaponinfo_map = {};
weaponinfo_map[1] = {"id":1,"aid":10001,};
weaponinfo_map[2] = {"id":2,"aid":10002,};
weaponinfo_map[3] = {"id":3,"aid":10003,};
weaponinfo_map[4] = {"id":4,"aid":10004,};
weaponinfo_map[5] = {"id":5,"aid":10005,};
weaponinfo_map[6] = {"id":6,"aid":10006,};
weaponinfo_map[7] = {"id":7,"aid":10007,};
weaponinfo_map[8] = {"id":8,"aid":10008,};
weaponinfo_map[9] = {"id":9,"aid":10009,};
weaponinfo_map[10] = {"id":10,"aid":10010,};
weaponinfo_map[11] = {"id":11,"aid":10011,};
weaponinfo_map[12] = {"id":12,"aid":10012,};
weaponinfo_map[13] = {"id":13,"aid":10013,};
weaponinfo_map[14] = {"id":14,"aid":10014,};
weaponinfo_map[15] = {"id":15,"aid":10015,};
weaponinfo_map[16] = {"id":16,"aid":10016,};
weaponinfo_map[17] = {"id":17,"aid":10001,};
weaponinfo_map[18] = {"id":18,"aid":10001,};
weaponinfo_map[19] = {"id":19,"aid":10001,};
weaponinfo_map[20] = {"id":20,"aid":10001,};
weaponinfo_map[21] = {"id":21,"aid":10001,};
weaponinfo_map[128] = {"id":128,"aid":10017,};
weaponinfo_map[129] = {"id":129,"aid":10018,};
weaponinfo_map[130] = {"id":130,"aid":10019,};
weaponinfo_map[131] = {"id":131,"aid":10020,};
weaponinfo_map[132] = {"id":132,"aid":10020,};
weaponinfo_map[133] = {"id":133,"aid":10020,};


class Weaponinfo:
	def __init__(self, key):
		config = weaponinfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Weaponinfo(key):
		config = weaponinfo_map.get(key);
		if not config:
			return
		return Weaponinfo(key)


# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


rideinfo_map = {};
rideinfo_map[1] = {"id":1,"faid":20001,"baid":30001,};
rideinfo_map[2] = {"id":2,"faid":20002,"baid":30002,};
rideinfo_map[3] = {"id":3,"faid":20003,"baid":30003,};
rideinfo_map[4] = {"id":4,"faid":20004,"baid":30004,};
rideinfo_map[5] = {"id":5,"faid":20005,"baid":30005,};
rideinfo_map[6] = {"id":6,"faid":20006,"baid":30006,};
rideinfo_map[7] = {"id":7,"faid":20007,"baid":30007,};
rideinfo_map[8] = {"id":8,"faid":20008,"baid":30008,};
rideinfo_map[9] = {"id":9,"faid":20009,"baid":30009,};
rideinfo_map[10] = {"id":10,"faid":20010,"baid":30010,};
rideinfo_map[11] = {"id":11,"faid":20011,"baid":30011,};
rideinfo_map[12] = {"id":12,"faid":20012,"baid":30012,};
rideinfo_map[13] = {"id":13,"faid":20013,"baid":30013,};
rideinfo_map[14] = {"id":14,"faid":20014,"baid":30014,};
rideinfo_map[15] = {"id":15,"faid":20015,"baid":30015,};
rideinfo_map[16] = {"id":16,"faid":20004,"baid":30004,};
rideinfo_map[17] = {"id":17,"faid":20005,"baid":30005,};
rideinfo_map[18] = {"id":18,"faid":20006,"baid":30006,};
rideinfo_map[19] = {"id":19,"faid":20001,"baid":30001,};
rideinfo_map[20] = {"id":20,"faid":20002,"baid":30002,};
rideinfo_map[128] = {"id":128,"faid":20016,"baid":30016,};
rideinfo_map[129] = {"id":129,"faid":20017,"baid":30017,};
rideinfo_map[130] = {"id":130,"faid":20018,"baid":30018,};
rideinfo_map[131] = {"id":131,"faid":20019,"baid":30019,};
rideinfo_map[132] = {"id":132,"faid":20020,"baid":30020,};
rideinfo_map[133] = {"id":133,"faid":20021,"baid":30021,};
rideinfo_map[134] = {"id":134,"faid":20021,"baid":30021,};


class Rideinfo:
	def __init__(self, key):
		config = rideinfo_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Rideinfo(key):
		config = rideinfo_map.get(key);
		if not config:
			return
		return Rideinfo(key)


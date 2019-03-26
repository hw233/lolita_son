# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightgroup_map = {};
fightgroup_map[1000] = {"id":1000,"data":[{"main":1000,"mainnum":1,"sub":1000,"subnum":2,"small":1000,"smallnum":3,"other":1000,"othernum":4,"array":0,},],};
fightgroup_map[1001] = {"id":1001,"data":[{"main":5036,"mainnum":1,"sub":5090,"subnum":2,"small":0,"smallnum":0,"other":0,"othernum":0,"array":0,},],};
fightgroup_map[1002] = {"id":1002,"data":[{"main":5028,"mainnum":1,"sub":5027,"subnum":2,"small":0,"smallnum":0,"other":0,"othernum":0,"array":0,},],};
fightgroup_map[1003] = {"id":1003,"data":[{"main":5142,"mainnum":2,"sub":0,"subnum":0,"small":0,"smallnum":0,"other":0,"othernum":0,"array":0,},{"main":5143,"mainnum":0,"sub":0,"subnum":0,"small":0,"smallnum":0,"other":0,"othernum":0,"array":0,},],};
fightgroup_map[1004] = {"id":1004,"data":[{"main":5065,"mainnum":1,"sub":5145,"subnum":2,"small":0,"smallnum":0,"other":0,"othernum":0,"array":0,},],};
fightgroup_map[1005] = {"id":1005,"data":[{"main":6143,"mainnum":1,"sub":6152,"subnum":102,"small":6162,"smallnum":202,"other":0,"othernum":0,"array":0,},],};


class Fightgroup:
	def __init__(self, key):
		config = fightgroup_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightgroup(key):
		config = fightgroup_map.get(key);
		if not config:
			return
		return Fightgroup(key)


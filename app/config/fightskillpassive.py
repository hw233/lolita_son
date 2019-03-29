# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightskillpassive_map = {};
fightskillpassive_map[101] = {"id":101,"name":"连击","type":"普通","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"连击预处理","efftime":"出招","effrate":45,"effdst":"1.0","effvalue":"1,0",},{"efftype":"连击","efftime":"命中","effrate":100,"effdst":"","effvalue":"",},{"efftype":"连击","efftime":"未命中","effrate":100,"effdst":"","effvalue":"",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"连击预处理","efftime":"出招","effrate":55,"effdst":"1.0","effvalue":"1,0",},{"efftype":"连击","efftime":"命中","effrate":100,"effdst":"","effvalue":"",},{"efftype":"连击","efftime":"未命中","effrate":100,"effdst":"","effvalue":"",},],},],},],};
fightskillpassive_map[102] = {"id":102,"name":"法连","type":"法术","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"连击预处理","efftime":"出招","effrate":25,"effdst":"1.0","effvalue":"1,0,(406,441,442,407,447,456,459,463,9032,9042,465,466,469,472,473,474,476,477,6953,6954,479,)",},{"efftype":"连击","efftime":"命中","effrate":100,"effdst":"","effvalue":"500",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"连击预处理","efftime":"出招","effrate":35,"effdst":"1.0","effvalue":"1,0,(406,441,442,407,447,456,459,463,9032,9042,465,466,469,472,473,474,476,477,6953,6954,479,)",},{"efftype":"连击","efftime":"命中","effrate":100,"effdst":"","effvalue":"400",},],},],},],};
fightskillpassive_map[103] = {"id":103,"name":"反击","type":"物理类","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"反击","efftime":"受伤","effrate":30,"effdst":"","effvalue":"40",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"反击","efftime":"受伤","effrate":30,"effdst":"","effvalue":"80",},],},],},],};
fightskillpassive_map[104] = {"id":104,"name":"反震","type":"物理类","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"反震","efftime":"受击","effrate":30,"effdst":"","effvalue":"25",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"反震","efftime":"受击","effrate":30,"effdst":"","effvalue":"50",},],},],},],};
fightskillpassive_map[105] = {"id":105,"name":"反射","type":"物理类","cryout":0,"data":[{"lv":1,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"反射","efftime":"受击","effrate":30,"effdst":"","effvalue":"446,1",},],},],},{"lv":2,"propdata":[{"prop":"无","pvalue":0,"ptime":"","prate":0,"effdata":[{"efftype":"反射","efftime":"受击","effrate":30,"effdst":"","effvalue":"457,1",},],},],},],};


class Fightskillpassive:
	def __init__(self, key):
		config = fightskillpassive_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightskillpassive(key):
		config = fightskillpassive_map.get(key);
		if not config:
			return
		return Fightskillpassive(key)


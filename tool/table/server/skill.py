# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


skill_map = {};
skill_map[1001] = {"id":1001,"skilldata":[{"lv":1,"stype":0,"targetmin":1,"targetmax":1,"effect":"actor['atk']*=1.2","group":1,"addbuff":"1001,300,3;1003,500,4","clrbuff":"1002,300","addbuffself":"1002,300,5;1004,300,6","clrbuffself":"1001,300",},{"lv":2,"stype":0,"targetmin":1,"targetmax":1,"effect":"actor['atk']*=1.3","group":1,"addbuff":"1001,300,3;1003,500,4","clrbuff":"1002,300","addbuffself":"1002,300,5;1004,300,6","clrbuffself":"1001,300",},{"lv":3,"stype":0,"targetmin":1,"targetmax":1,"effect":"actor['atk']*=1.4","group":1,"addbuff":"1001,300,3;1003,500,4","clrbuff":"1002,300","addbuffself":"1002,300,5;1004,300,6","clrbuffself":"1001,300",},],};
skill_map[1002] = {"id":1002,"skilldata":[{"lv":1,"stype":2,"targetmin":1,"targetmax":3,"effect":"actor['spd']+=20","group":1,"addbuff":"1001,300,3;1003,500,4","clrbuff":"1002,300","addbuffself":"1002,300,5;1004,300,6","clrbuffself":"1001,300",},{"lv":2,"stype":2,"targetmin":1,"targetmax":4,"effect":"actor['spd']+=30","group":1,"addbuff":"1001,300,3;1003,500,4","clrbuff":"1002,300","addbuffself":"1002,300,5;1004,300,6","clrbuffself":"1001,300",},],};


class Skill:
	def __init__(self, key):
		config = skill_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Skill(key):
		config = skill_map.get(key);
		if not config:
			return
		return Skill(key)


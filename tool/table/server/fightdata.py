# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightdata_map = {};
fightdata_map[1000] = {"id":1000,"name":"新手怪","shape":1002,"color":0,"hair":0,"weapon":0,"wcolor":0,"wing":0,"wingcolor":0,"name":"可爱的野猪","lv":1,"fight":1000,"ai":0,"quit":0,"adjust":0,};
fightdata_map[1001] = {"id":1001,"name":"追捕血怪","shape":1040,"color":0,"hair":0,"weapon":0,"wcolor":0,"wing":0,"wingcolor":0,"name":"","lv":0,"fight":1001,"ai":0,"quit":0,"adjust":0,};
fightdata_map[1002] = {"id":1002,"name":"追捕法抗怪","shape":1023,"color":0,"hair":0,"weapon":0,"wcolor":0,"wing":0,"wingcolor":0,"name":"","lv":0,"fight":1002,"ai":0,"quit":0,"adjust":0,};
fightdata_map[1003] = {"id":1003,"name":"追捕物抗怪","shape":1041,"color":0,"hair":0,"weapon":0,"wcolor":0,"wing":0,"wingcolor":0,"name":"","lv":0,"fight":1003,"ai":0,"quit":0,"adjust":0,};
fightdata_map[1004] = {"id":1004,"name":"追捕双抗怪","shape":1022,"color":0,"hair":0,"weapon":0,"wcolor":0,"wing":0,"wingcolor":0,"name":"","lv":0,"fight":1004,"ai":0,"quit":0,"adjust":0,};
fightdata_map[1005] = {"id":1005,"name":"追捕全能怪","shape":1034,"color":0,"hair":0,"weapon":0,"wcolor":0,"wing":0,"wingcolor":0,"name":"","lv":0,"fight":1005,"ai":0,"quit":0,"adjust":0,};


class Fightdata:
	def __init__(self, key):
		config = fightdata_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightdata(key):
		config = fightdata_map.get(key);
		if not config:
			return
		return Fightdata(key)


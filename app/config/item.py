# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


item_map = {};
item_map[1001] = {"shape":1001,"price":100,"goldspd":100,"icon":1001,"name":"金鱼1","desc":"金鱼1",};
item_map[1002] = {"shape":1002,"price":200,"goldspd":200,"icon":1002,"name":"金鱼2","desc":"金鱼2",};
item_map[1003] = {"shape":1003,"price":400,"goldspd":300,"icon":1003,"name":"金鱼3","desc":"金鱼3",};
item_map[1004] = {"shape":1004,"price":800,"goldspd":400,"icon":1004,"name":"金鱼4","desc":"金鱼4",};
item_map[1005] = {"shape":1005,"price":1600,"goldspd":500,"icon":1005,"name":"金鱼5","desc":"金鱼5",};
item_map[1006] = {"shape":1006,"price":3200,"goldspd":600,"icon":1006,"name":"金鱼6","desc":"金鱼6",};
item_map[1007] = {"shape":1007,"price":6400,"goldspd":700,"icon":1007,"name":"金鱼7","desc":"金鱼7",};
item_map[1008] = {"shape":1008,"price":12800,"goldspd":800,"icon":1008,"name":"金鱼8","desc":"金鱼8",};
item_map[1009] = {"shape":1009,"price":25600,"goldspd":900,"icon":1009,"name":"金鱼9","desc":"金鱼9",};
item_map[1010] = {"shape":1010,"price":51200,"goldspd":1000,"icon":1010,"name":"金鱼10","desc":"金鱼10",};
item_map[1011] = {"shape":1011,"price":102400,"goldspd":1100,"icon":1011,"name":"金鱼11","desc":"金鱼11",};
item_map[1012] = {"shape":1012,"price":204800,"goldspd":1200,"icon":1012,"name":"金鱼12","desc":"金鱼12",};


class Item:
	def __init__(self, key):
		config = item_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Item(key):
		config = item_map.get(key);
		if not config:
			return
		return Item(key)


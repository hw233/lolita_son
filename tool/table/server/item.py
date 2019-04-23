# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


item_map = {};
item_map[1001] = {"shape":1001,"price":100,"icon":1001,"name":"金鱼1","desc":"金鱼1","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1002] = {"shape":1002,"price":200,"icon":1002,"name":"金鱼2","desc":"金鱼2","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1003] = {"shape":1003,"price":400,"icon":1003,"name":"金鱼3","desc":"金鱼3","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1004] = {"shape":1004,"price":800,"icon":1004,"name":"金鱼4","desc":"金鱼4","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1005] = {"shape":1005,"price":1600,"icon":1005,"name":"金鱼5","desc":"金鱼5","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1006] = {"shape":1006,"price":3200,"icon":1006,"name":"金鱼6","desc":"金鱼6","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1007] = {"shape":1007,"price":6400,"icon":1007,"name":"金鱼7","desc":"金鱼7","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1008] = {"shape":1008,"price":12800,"icon":1008,"name":"金鱼8","desc":"金鱼8","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1009] = {"shape":1009,"price":25600,"icon":1009,"name":"金鱼9","desc":"金鱼9","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1010] = {"shape":1010,"price":51200,"icon":1010,"name":"金鱼10","desc":"金鱼10","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1011] = {"shape":1011,"price":102400,"icon":1011,"name":"金鱼11","desc":"金鱼11","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[1012] = {"shape":1012,"price":204800,"icon":1012,"name":"金鱼12","desc":"金鱼12","reqlv":0,"tp":"","d1":"","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[10000] = {"shape":10000,"price":0,"icon":10000,"name":"木剑","desc":"木剑","reqlv":0,"tp":"装备","d1":"1.0","d2":"100.0","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[20000] = {"shape":20000,"price":1000,"icon":20000,"name":"经验丹","desc":"经验丹","reqlv":0,"tp":"经验","d1":"100000.0","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};
item_map[20001] = {"shape":20001,"price":0,"icon":20001,"name":"金砖","desc":"金砖","reqlv":0,"tp":"金币","d1":"1000000.0","d2":"","d3":"","d4":"","d5":"","d6":"","d7":"","d8":"",};


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


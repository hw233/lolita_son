# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


assist_info_map = {};
assist_info_map["召唤兽"] = {"type":"召唤兽","item_data":[{"id":0,"title":"获取途径","desc":"#C16&灵兽#D&可以在以下途径获取","icon_path":"icon/head/1902.cia","func_data":[{"func_type":"灵兽商行","func_name":"灵兽商行","func_data1":1002,"func_data2":5024,},{"func_type":"前往场景","func_name":"前往捕捉","func_data1":1101,},],},{"id":1,"title":"获取途径","desc":"#C16&野猪#D&可以在以下途径获取","func_data":[{"func_type":"灵兽商行","func_name":"灵兽商行","func_data1":1002,"func_data2":5024,},{"func_type":"前往场景","func_name":"前往捕捉","func_data1":1101,},],},],};
assist_info_map["道具"] = {"type":"道具","item_data":[{"id":0,"title":"获取途径","desc":"#C16&道具#D&可以在以下途径获取","icon_path":"icon/item/small/10030.cia","func_data":[{"func_type":"集市购买","func_name":"集市购买","func_data1":1002,"func_data2":5383,},],},{"id":77003,"title":"获取途径","desc":"#C16&洗髓丹#D&可以在以下途径获取","icon_path":"ui/huodong/玩法指引/icon/普通.cia","func_data":[{"func_type":"NPC对话","func_name":"副本任务","func_data1":1002,"func_data2":8998,},{"func_type":"商店购买","func_name":"商店购买","func_data1":1002,"func_data2":2073,},],},],};
assist_info_map["任务"] = {"type":"任务","item_data":[{"id":0,"title":"寻求帮助","desc":"#C16&任务#D&可以在以下途径完成","func_data":[{"func_type":"帮贡完成","func_name":"帮贡完成","func_data1":20,},{"func_type":"帮派求助","func_name":"帮派求助",},{"func_type":"雇佣帮手","func_name":"雇佣帮手",},],},{"id":1004,"title":"寻求帮助","desc":"#C16&战斗环任务#D&可以在以下途径完成","func_data":[{"func_type":"帮派求助","func_name":"帮派求助","func_data1":1004,},],},],};
assist_info_map["道具类"] = {"type":"道具类","item_data":[{"id":0,"title":"获取途径","desc":"#C16&道具类#D&可以在以下途径获取","icon_path":"icon/item/small/10030.cia","func_data":[{"func_type":"商店购买","func_name":"商店购买","func_data1":1002,"func_data2":5384,},],},{"id":1413,"title":"获取途径","desc":"#C16&兽诀#D&可以在以下途径获取","icon_path":"ui/huodong/玩法指引/icon/普通.cia","func_data":[{"func_type":"洛阳商会","func_name":"商会购买","func_data1":1002,"func_data2":2087,"func_data3":6,},{"func_type":"NPC对话","func_name":"副本任务","func_data1":1002,"func_data2":3064,},],},],};


class Assist_info:
	def __init__(self, key):
		config = assist_info_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Assist_info(key):
		config = assist_info_map.get(key);
		if not config:
			return
		return Assist_info(key)


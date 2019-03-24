# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


combat_skip_cfg_map = {};
combat_skip_cfg_map[2] = {"war_type":2,"war_name":"竞技场","vip":1,"lv":1,"pass_round":3,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[3] = {"war_type":3,"war_name":"上古秘宝","vip":1,"lv":1,"pass_round":1,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[4] = {"war_type":4,"war_name":"天庭降妖","vip":1,"lv":1,"pass_round":2,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[5] = {"war_type":5,"war_name":"大雁神塔","vip":1,"lv":1,"pass_round":2,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[6] = {"war_type":6,"war_name":"天下第一","vip":1,"lv":1,"pass_round":1,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[7] = {"war_type":7,"war_name":"全民BOSS","vip":1,"lv":1,"pass_round":1,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[9] = {"war_type":9,"war_name":"每日押镖-劫镖","vip":1,"lv":1,"pass_round":1,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[10] = {"war_type":10,"war_name":"每日押镖-复仇","vip":1,"lv":1,"pass_round":1,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[16] = {"war_type":16,"war_name":"野外BOSS挑战玩家","vip":1,"lv":1,"pass_round":1,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[17] = {"war_type":17,"war_name":"野外BOSS挑战BOSS","vip":1,"lv":1,"pass_round":3,"tips":"1级或VIP1开启跳过",};
combat_skip_cfg_map[22] = {"war_type":22,"war_name":"武林盟主","vip":1,"lv":1,"pass_round":3,"tips":"1级或VIP1开启跳过",};


class Combat_skip_cfg:
	def __init__(self, key):
		config = combat_skip_cfg_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Combat_skip_cfg(key):
		config = combat_skip_cfg_map.get(key);
		if not config:
			return
		return Combat_skip_cfg(key)


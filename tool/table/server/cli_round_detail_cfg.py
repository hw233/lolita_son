# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


cli_round_detail_cfg_map = {};
cli_round_detail_cfg_map[2] = {"war_subType":2,"descType":1,"title":"竞技场","desc":"奖励：功勋、银子、经验",};
cli_round_detail_cfg_map[3] = {"war_subType":3,"descType":2,"title":"上古秘宝","desc":"通关奖励：进阶装备、宠物升级丹、银子、经验",};
cli_round_detail_cfg_map[4] = {"war_subType":4,"descType":1,"title":"天庭降妖","desc":"通关奖励：进阶装备、宠物升级丹、银子、经验",};
cli_round_detail_cfg_map[5] = {"war_subType":5,"descType":1,"title":"大雁神塔","desc":"通关奖励：进阶装备、宠物升级丹、银子、经验",};
cli_round_detail_cfg_map[7] = {"war_subType":7,"descType":1,"title":"全民BOSS","desc":"通关奖励：装备、绑元、经验",};
cli_round_detail_cfg_map[9] = {"war_subType":9,"descType":1,"title":"劫镖","desc":"通关奖励：银子、宠物升级丹",};
cli_round_detail_cfg_map[10] = {"war_subType":10,"descType":1,"title":"复仇","desc":"通关奖励：银子、绑元",};
cli_round_detail_cfg_map[11] = {"war_subType":11,"descType":1,"title":"野外封妖","desc":"通关奖励：经验、银子",};
cli_round_detail_cfg_map[12] = {"war_subType":12,"descType":1,"title":"主线关卡","desc":"通关奖励：元宝、经验、银子、装备",};
cli_round_detail_cfg_map[13] = {"war_subType":13,"descType":1,"title":"材料副本","desc":"通关奖励：银子、绑元、进阶丹、锻炼石、精炼石、宝石",};
cli_round_detail_cfg_map[14] = {"war_subType":14,"descType":1,"title":"个人BOSS","desc":"通关奖励：蓝色装备、紫色装备、橙色装备",};
cli_round_detail_cfg_map[15] = {"war_subType":15,"descType":1,"title":"平定妖王","desc":"通关奖励：经验、银子、绑元、宠物升级丹、装备",};
cli_round_detail_cfg_map[16] = {"war_subType":16,"descType":1,"title":"野外BOSS","desc":"通关奖励：银子、绑元、装备",};
cli_round_detail_cfg_map[17] = {"war_subType":17,"descType":1,"title":"野外BOSS","desc":"通关奖励：银子、绑元、装备",};
cli_round_detail_cfg_map[18] = {"war_subType":18,"descType":1,"title":"帮派BOSS","desc":"通关奖励：元宝、银子、绑元",};
cli_round_detail_cfg_map[19] = {"war_subType":19,"descType":1,"title":"帮派副本","desc":"通关奖励：绑元、帮贡",};
cli_round_detail_cfg_map[20] = {"war_subType":20,"descType":1,"title":"跨服抓鬼","desc":"通关奖励：经验、银子、坐骑装备、羽翼装备",};
cli_round_detail_cfg_map[21] = {"war_subType":21,"descType":1,"title":"主线协助","desc":"通关奖励：经验、银子",};


class Cli_round_detail_cfg:
	def __init__(self, key):
		config = cli_round_detail_cfg_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Cli_round_detail_cfg(key):
		config = cli_round_detail_cfg_map.get(key);
		if not config:
			return
		return Cli_round_detail_cfg(key)


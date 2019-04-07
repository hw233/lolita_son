# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightprop_map = {};
fightprop_map[1] = {"id":1,"name":"气血增加","key":"hpmax",};
fightprop_map[2] = {"id":2,"name":"魔法增加","key":"mpmax",};
fightprop_map[3] = {"id":3,"name":"攻击增加","key":"m_Attack",};
fightprop_map[4] = {"id":4,"name":"防御按等级增加","key":"m_DefenseLv",};
fightprop_map[5] = {"id":5,"name":"感知","key":"m_Sense",};
fightprop_map[6] = {"id":6,"name":"物理封印","key":"m_Seal",};
fightprop_map[7] = {"id":7,"name":"法术封印","key":"m_MgcSeal",};


class Fightprop:
	def __init__(self, key):
		config = fightprop_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightprop(key):
		config = fightprop_map.get(key);
		if not config:
			return
		return Fightprop(key)


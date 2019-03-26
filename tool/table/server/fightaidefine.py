# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fightaidefine_map = {};
fightaidefine_map[101] = {"id":101,"name":"随机使用",};
fightaidefine_map[103] = {"id":103,"name":"召唤怪物",};
fightaidefine_map[104] = {"id":104,"name":"HP释放",};
fightaidefine_map[105] = {"id":105,"name":"回合技能",};
fightaidefine_map[106] = {"id":106,"name":"回合召唤",};
fightaidefine_map[107] = {"id":107,"name":"回合逃跑",};
fightaidefine_map[108] = {"id":108,"name":"逃跑",};
fightaidefine_map[109] = {"id":109,"name":"血量换ai",};
fightaidefine_map[110] = {"id":110,"name":"血量换技能",};
fightaidefine_map[111] = {"id":111,"name":"点名攻击",};
fightaidefine_map[112] = {"id":112,"name":"主怪死亡逃跑",};
fightaidefine_map[113] = {"id":113,"name":"回合使用技能",};
fightaidefine_map[114] = {"id":114,"name":"有怪加buff",};
fightaidefine_map[115] = {"id":115,"name":"友方数量技能",};
fightaidefine_map[116] = {"id":116,"name":"对boss技能",};
fightaidefine_map[117] = {"id":117,"name":"血量召唤",};
fightaidefine_map[118] = {"id":118,"name":"召唤怪物属性提升",};
fightaidefine_map[201] = {"id":201,"name":"对白配置",};
fightaidefine_map[202] = {"id":202,"name":"HP对白",};
fightaidefine_map[203] = {"id":203,"name":"回合召唤喊话",};
fightaidefine_map[204] = {"id":204,"name":"喊话BUFF",};
fightaidefine_map[205] = {"id":205,"name":"指定回合结束战斗",};
fightaidefine_map[206] = {"id":206,"name":"死亡其他对应怪物逃跑",};
fightaidefine_map[207] = {"id":207,"name":"复活同类怪",};
fightaidefine_map[209] = {"id":209,"name":"分身",};
fightaidefine_map[210] = {"id":210,"name":"对倒地怪使用技能",};
fightaidefine_map[211] = {"id":211,"name":"回合对BOSS使用技能",};
fightaidefine_map[212] = {"id":212,"name":"指定攻击某怪",};
fightaidefine_map[213] = {"id":213,"name":"随机对玩家使用对白",};
fightaidefine_map[214] = {"id":214,"name":"对玩家随机使用",};
fightaidefine_map[215] = {"id":215,"name":"血量召唤2",};
fightaidefine_map[216] = {"id":216,"name":"回合技能2",};
fightaidefine_map[217] = {"id":217,"name":"HP释放2",};
fightaidefine_map[218] = {"id":218,"name":"回合召唤喊话2",};
fightaidefine_map[219] = {"id":219,"name":"战斗有对应职业逃跑",};
fightaidefine_map[220] = {"id":220,"name":"任意死亡该怪逃跑",};
fightaidefine_map[221] = {"id":221,"name":"存在回合逃跑",};
fightaidefine_map[222] = {"id":222,"name":"受伤变技能",};
fightaidefine_map[223] = {"id":223,"name":"封印逃跑",};
fightaidefine_map[225] = {"id":225,"name":"五一小怪专用",};
fightaidefine_map[228] = {"id":228,"name":"自动释放冰心",};


class Fightaidefine:
	def __init__(self, key):
		config = fightaidefine_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fightaidefine(key):
		config = fightaidefine_map.get(key);
		if not config:
			return
		return Fightaidefine(key)


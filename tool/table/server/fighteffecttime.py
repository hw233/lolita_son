# -*- coding: utf-8 -*-

'''
Author: Hannibal
Data: 
Desc: local data config
NOTE: Don't modify this file, it's build by xml-to-python!!!
'''


fighteffecttime_map = {};
fighteffecttime_map[1] = {"id":1,"name":"进入战斗","desc":"进入战斗（战斗开始入场，中途召唤入场）",};
fighteffecttime_map[2] = {"id":2,"name":"回合开始","desc":"",};
fighteffecttime_map[3] = {"id":3,"name":"使用技能","desc":"出手开始（针对整个出招）",};
fighteffecttime_map[4] = {"id":4,"name":"伤害","desc":"攻击开始（针对单个打击，主要用在群攻中的单次攻击，如果是只打一个的群攻，则在出手开始后立刻进入攻击开始阶段，然后是攻击结束，最后是出手结束）",};
fighteffecttime_map[5] = {"id":5,"name":"命中","desc":"攻击有效（特殊结算时机，还不好确定，目前能想到的就是封印技能概率命中时触发）",};
fighteffecttime_map[6] = {"id":6,"name":"未命中","desc":"攻击失效（类似上一个，目前能确定的时封印技能概率未命中时触发，但是被抗封效果抵挡是否也算在内？是否要引入针对性效果计算？）",};
fighteffecttime_map[7] = {"id":7,"name":"被命中","desc":"被攻击时，主要用在反击反射",};
fighteffecttime_map[8] = {"id":8,"name":"伤害结束","desc":"攻击结束",};
fighteffecttime_map[9] = {"id":9,"name":"击杀","desc":"击飞（包括被收回）",};
fighteffecttime_map[10] = {"id":10,"name":"死亡","desc":"死亡（击倒可复活）",};
fighteffecttime_map[11] = {"id":11,"name":"使用完毕","desc":"出手结束（针对整个出招）",};
fighteffecttime_map[12] = {"id":12,"name":"回合结束","desc":"",};
fighteffecttime_map[13] = {"id":13,"name":"退出战斗","desc":"",};


class Fighteffecttime:
	def __init__(self, key):
		config = fighteffecttime_map.get(key);
		for k, v in config.items():
			setattr(self, k, v);
		return

def create_Fighteffecttime(key):
		config = fighteffecttime_map.get(key);
		if not config:
			return
		return Fighteffecttime(key)


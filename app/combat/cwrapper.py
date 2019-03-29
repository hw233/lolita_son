#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
class cwrapperbase(object):
	def __init__(self,inst,value,rate,dst,triger,bout = 0):
		self.inst = inst;#cbuff or boutbuff
		self.value = value;
		self.rate = rate;#如果为0等于100
		self.dst = dst;#0为自己，1为敌人
		self.triger = triger;
		self.bout = bout;
		self.spd = 0;
		self.actor = None;
		self.enemy_list = [];
		self.done = False;
		return
	def get_triger_state(self):
		return self.triger.get_id();
	def gen_spd(self,actor_spd):
		self.spd = self.inst.gen_spd(actor_spd);
		return
	def set_actor(self,actor):
		self.actor = actor;
		return
	def set_enemy_list(self,e_list):
		self.enemy_list = e_list;
		return
	def do(self):
		return
class combatwrapper(cwrapperbase):
	def __init__(self,inst,value,rate,dst,triger,bout = 0):
		super(combatwrapper,self).__init__(inst,value,rate,dst,triger,bout)
		return
	def do(self):
		return
class combatbuffwrapper(object):
	def __init__(self,inst,value,rate,dst,triger,bout):
		super(combatbuffwrapper,self).__init__(inst,value,rate,dst,triger,bout)
		return
	def do(self):
		return



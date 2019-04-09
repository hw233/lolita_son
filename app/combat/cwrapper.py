#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import random
import buff
import cbuff

g_wrapper_id_start = 0;
class cwrapperbase(object):
	def __init__(self,inst,value,rate,dst,triger,bout = 0):
		self.inst = inst;#cproperty or ceffect 
		self.value = value;
		self.rate = rate;#如果为0等于100
		self.dst = dst;#1为自己，0为敌人
		self.triger = triger;
		self.bout = bout;
		self.spd = 0;
		self.actor = None;
		self.enemy_list = [];
		self.id = self._gen_id();
		return
	def _gen_id(self):
		global g_wrapper_id_start;
		g_wrapper_id_start = g_wrapper_id_start + 1;
		return g_wrapper_id_start
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
	def do(self,combat_ins,b_minus = False):
		#if self.actor.has_wrapper(self.id) == False:
		#	self.actor.use_wrapper(self.id);
		return
	def clear(self,combat_ins,b_minus = False):
		#if self.actor.has_wrapper(self.id) == False:
		#	self.actor.use_wrapper(self.id);
		return
class combatwrapper(cwrapperbase):
	def __init__(self,inst,value,rate,dst,triger,bout = 0):
		super(combatwrapper,self).__init__(inst,value,rate,dst,triger,bout)
		return
	def do(self,combat_ins,b_minus = False):
		if self.rate > 0 and self.rate < 100:
			if self.rate < random.randint(0,100):
				return
		
		if self.dst == 1:
			b_done = False;
			if self.actor.has_wrapper(self.id) == False:
				self.actor.use_wrapper(self.id);
			else:
				b_done = True;
			self.inst.do(self.actor,combat_ins,self.value,b_done,b_minus,True);
		else:
			for i in self.enemy_list:
				b_done = False;
				if i.has_wrapper(self.id) == False:
					i.use_wrapper(self.id);
				else:
					b_done = True;
				self.inst.do(i,combat_ins,self.value,b_done,b_minus,False);
		return
	def clear(self,combat_ins,b_minus = False):
		if self.dst == 1:
			if self.actor.has_wrapper(self.id):
				self.actor.clear_wrapper(self.id);
				self.inst.clear(self.actor,combat_ins,self.value,True,b_minus);
		else:
			for i in self.enemy_list:
				if i.has_wrapper(self.id):
					i.clear_wrapper(self.id);
					self.inst.do(i,combat_ins,self.value,True,b_minus);
		return
class combatbuffwrapper(cwrapperbase):#用来添加BUFF
	def __init__(self,inst,value,rate,dst,triger,bout):#inst maybe is cbuffeff or buffcfg
		super(combatbuffwrapper,self).__init__(inst,value,rate,dst,triger,bout)
		return
	def do(self,combat_ins,b_minus = False):
		bhit = False;
		bhit_rate = random.randint(0,100);
		if self.rate >= 100:
			bhit = True;
		else:
			if self.rate >= bhit_rate:
				bhit = True;
		print "combatbuffwrapper do %s %s %s %s"%(self.rate,bhit_rate,self.dst,len(self.enemy_list));
		if not bhit:
			return
		add_list = [];
		if self.dst == 1:
			add_list.append(self.actor);
		else:
			for i in self.enemy_list:
				add_list.append(i);
		bid = self.inst.bid;
		refresh = self.inst.refresh;
		overlapmax = self.inst.overlap;
		addcd = self.bout;
		buffvalue = self.value;
		for i in add_list:
			old_buff = i.has_buff(bid);
			if old_buff == None:
				addbuff = buff.boutbuff(bid,addcd);
				addbuff.bcfg = self.inst;
				addbuff.value = buffvalue;
				i.add_buff(addbuff);
				combat_ins.gen_s2c_warrior_addbuff(i,addbuff,0,0);
				addbuff.do(i,combat_ins);
			else:
				bAdd = False;
				if old_buff.count <= overlapmax:
					old_buff.count += 1;
					bAdd = True;
				brefresh_cd = False;
				if refresh == 1:
					old_buff.cd = addcd;
					brefresh_cd = True;
				if bAdd or brefresh_cd:
					combat_ins.gen_s2c_warrior_addbuff(i,old_buff,0,0);
				if bAdd:
					old_buff.do(i,combat_ins);
		return



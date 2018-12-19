#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import copy
import random
import combatbase
import skill
import buff
import skillpassive
class warrior(combatbase.combatbase):
	def __init__(self,wid,pos):
		super(warrior,self).__init__();
		self.m_id = wid;
		self['id'] = wid;
		self.init_data();
		self['pos'] = pos;
		if pos <= 12:
			self['group'] = 0;
		else:
			self['group'] = 1;
		return
	def reset_orgprop(self):
		self['hpmax'] = self['orghpmax'];
		self['spd'] = self['orgspd'];
		self['atk'] = self['orgatk'];
		self['def'] = self['orgdef'];
		self['hit'] = self['orghit'];
		self['dodge'] = self['orgdodge'];
		self['crk'] = self['orgcrk'];
		self['crkdef'] = self['orgcrkdef'];
		return
	def set_data(self,data_dict):
		super(warrior,self).set_data(data_dict);
		self.gen_orgprop();
		return
	def gen_orgprop(self):
		self['orghpmax'] = self['hpmax'];
		self['orgspd'] = self['spd'];
		self['orgatk'] = self['atk'];
		self['orgdef'] = self['def'];
		self['orghit'] = self['hit'];
		self['orgdodge'] = self['dodge'];
		self['orgcrk'] = self['crk'];
		self['orgcrkdef'] = self['crkdef'];
		return
	def get_restoreprop(self):
		return copy.deepcopy(self);
	def init_data(self):
		self['hp'] = 100;
		self['hpmax'] = 100;
		self['spd'] = 100;
		self['atk'] = 100;
		self['def'] = 0;
		self['hit'] = 0;
		self['dodge'] = 0;
		self['crk'] = 0;
		self['crkdef'] = 0;
		self['skill'] = {};
		self['buff'] = {};
		self['pet'] = {};
		self['passive'] = {};
		self['dead'] = False;
		self['group'] = 0;
		self['pos'] = 0;
		self['autodel'] = False;
		self.gen_orgprop();
		return
	def gen_testdata(self):
		ret = {};
		ret['hp'] = 10000;
		ret['hpmax'] = 10000;
		ret['spd'] = random.randint(0,100);
		ret['atk'] = random.randint(0,1000);
		ret['def'] = random.randint(0,200);
		ret['hit'] = random.randint(0,100);
		ret['dodge'] = random.randint(0,100);
		ret['crk'] = random.randint(0,100);
		ret['crkdef'] = random.randint(0,100);
		ret['skill'] = {1001:skill.skill(1001,1),1002:skill.skill(1002,1)};
		ret['buff'] = {1:buff.buff(1001,3),2:buff.buff(1002,3),3:buff.buff(1003,3)};
		ret['passive'] = {2001:skillpassive.skillpassive(2001,1),2002:skillpassive.skillpassive(2002,1),2003:skillpassive.skillpassive(2003,1)};
		return ret;
	def add_buff(self,buf_id,cd,inst_id):
		ret = buff.buff(buf_id,cd);
		ret.id = inst_id;
		self['buff'][inst_id] = ret;
		return ret
	def del_buff(self,buf_id):
		ret = None
		for k,v in self['buff'].items():
			if v.bid == buf_id:
				if ret == None:
					ret = buff.buff(buf_id);
				del self['buff'][k];
		return ret

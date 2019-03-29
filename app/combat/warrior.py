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
import skillpassive as skillpassive
class warrior(combatbase.combatbase):
	def __init__(self,wid,pos,cid):
		super(warrior,self).__init__();
		self.m_id = wid;
		self['cid'] = cid;
		self['id'] = wid;
		self['hp'] = 100;
		self['hpmax'] = 100;
		self['spd'] = 100;
		self['sp'] = 100;
		self['enegy'] = 100;
		self['mp'] = 100;
		self['atk'] = 100;
		self['def'] = 0;
		self['hit'] = 0;
		self['dodge'] = 0;
		self['crk'] = 0;
		self['crkdef'] = 0;
		self['crkdmgrate'] = 100;#暴击伤害，基础100%
		self['crkdmgdefrate'] = 0;
		self['dmgrate'] = 0;#伤害加深百分比,基础0%
		self['dmgdefrate'] = 0;
		self['absdmg'] = 0;#伤害加深绝对值
		self['absdmgdef'] = 0;#无视伤害加深绝对值
		self['ignoredef'] = 0;#无视防御绝对值
		self['ignoredefdef'] = 0;#无视无视防御（无视减免)绝对值
		self['skill'] = {};#sid:sid+slv
		self['buff'] = [];
		self['passive'] = {};#sid:sid+slv
		self['pet'] = {};
		self['dead'] = False;
		self['group'] = 0;
		self['pos'] = 0;
		self['cankickout'] = False;
		self['kickout'] = False;
		
		self['pos'] = pos;
		if pos <= 12:
			self['group'] = 0;
		else:
			self['group'] = 1;
		self['shape'] = 101;
		self['name'] = str(self.m_id);

		self.gen_orgprop();
		return
	def get_skill(self,sid):
		if self['skill'].has_key(sid):
			return self['skill'][sid]
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
		self['crkdmgrate'] = self['orgcrkdmgrate'];
		self['crkdmgdefrate'] = self['orgcrkdmgdefrate'];
		self['dmgrate'] = self['orgdmgrate'];
		self['dmgdefrate'] = self['orgdmgdefrate'];
		self['absdmg'] = self['orgabsdmg'];
		self['absdmgdef'] = self['orgabsdmgdef'];
		self['ignoredef'] = self['orgignoredef'];
		self['ignoredefdef'] = self['orgignoredefdef'];
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
		self['orgcrkdmgrate'] = self['crkdmgrate'];
		self['orgcrkdmgdefrate'] = self['crkdmgdefrate'];
		self['orgdmgrate'] = self['dmgrate'];
		self['orgdmgdefrate'] = self['dmgdefrate'];
		self['orgabsdmg'] = self['absdmg'];
		self['orgabsdmgdef'] = self['absdmgdef'];
		self['orgignoredef'] = self['ignoredef'];
		self['orgignoredefdef'] = self['ignoredefdef'];
		return
	def get_restoreprop(self):
		return copy.deepcopy(self);

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
	

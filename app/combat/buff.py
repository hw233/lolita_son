#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.buff as buffconfig
class buff(object):
	def __init__(self,bid,cd = 0,inst_id = 0):
		self.bid = bid;
		self.id = inst_id;
		self.cd = cd;
		self.btype = 0;
		self.effect = "";
		self.groupid = 0;
		self.init();
		return
	def init(self):
		bufdata = buffconfig.create_Buff(self.bid);
		self.effect = bufdata.effect;
		self.groupid = bufdata.group;
		self.btype = bufdata.btype;
		return
	def is_immediate(self):
		return self.btype == 0;
	def get_effect(self):
		return self.effect;
	def get_group(self):
		return self.groupid;

def get_bufflist_bygroup(groupid):
	ret = [];
	for k,v in buffconfig.buff_map.items():
		if v["group"] == groupid:
			ret.append(buff(k));
	return ret;
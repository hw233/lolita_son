#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.simplebuff as buffconfig
import app.config.fightbuff as fightbuff
import ctriger
import cproperty
import cbuff
import ceffect
import cwrapper

class buff(cbuff.buffbase):
	def __init__(self,bid,cd = 0):
		super(buff,self).__init__(bid,cd);
		return
	def init(self):
		bufdata = buffconfig.create_Simplebuff(self.bid);
		self.effect = bufdata.effect;
		self.groupid = bufdata.group;
		self.btype = bufdata.btype;
		return
	

def get_bufflist_bygroup(groupid):
	ret = [];
	for k,v in buffconfig.buff_map.items():
		if v["group"] == groupid:
			ret.append(buff(k));
	return ret;

class boutbuffcfg(object):
	def __init__(self,bid):
		self.bid = bid;
		self.name = "";
		self.tp = "";
		self.refresh = 0;
		self.overlap = 1;
		self.proplist = [];#cprop,value,ctriger,rate
		return

g_buffcfg_map = {};
g_buff_name_2_id = {};
g_buff_id_2_name = {};

def get_buffname_byid(bid):
	global g_buff_id_2_name
	global g_buff_name_2_id
	if not g_buff_id_2_name.has_key(bid):
		if fightbuff.fightbuff_map.has_key(bid):
			g_buff_id_2_name[bid] = fightbuff.fightbuff_map[bid]["name"];
			g_buff_name_2_id[g_buff_id_2_name[bid]] = bid;
		else:
			g_buff_id_2_name[bid] = "unknown buff";
	return g_buff_id_2_name[bid];
def get_buffbid_byname(name):
	global g_buff_id_2_name
	global g_buff_name_2_id
	if not g_buff_name_2_id.has_key(name):
		bfound = False;
		for k,v in fightbuff.fightbuff_map.items():
			if v["name"] == name:
				g_buff_name_2_id[name] = k;
				g_buff_id_2_name[k] = name;
				bfound = True;
				break;
		if not bfound:
			g_buff_name_2_id[name] = 0;
	return g_buff_name_2_id[name];
def get_buffcfg(bid):
	global g_buffcfg_map
	if g_buffcfg_map.has_key(bid) == False:
		cfg = fightbuff.create_Fightbuff(bid);
		if cfg:
			ret = boutbuffcfg(bid);
			ret.tp = cfg.type;
			ret.name = cfg.name;
			ret.refresh = cfg.refresh;
			ret.overlap = cfg.count;
			for i in cfg.data:
				prop = i["prop"]
				v = i["value"]
				tm = ctriger.COMBAT_TRIGER_NOW;
				rate = 0;
				dst = 0;
				pins = None;
				if not pins and ceffect.have_effect_by_name(prop):
					pins = ceffect.get_effect_by_name(prop);
				if not pins and cproperty.have_cprop_by_name(prop):
					pins = cproperty.get_cprop_by_name(prop);
				wrapper_ins = cwrapper.combatwrapper(pins,v,rate,dst,ctriger.get_triger_by_id(tm));
				ret.proplist.append(wrapper_ins);
			g_buffcfg_map[bid] = ret;
		else:
			g_buffcfg_map[bid] = boutbuffcfg(0);
	return g_buffcfg_map[bid];
def have_buff_byname(name):
	bid = get_buffbid_byname(name);
	return bid != 0;
class boutbuff(cbuff.buffbase):
	def __init__(self,bid,cd = 0):
		super(boutbuff,self).__init__(bid,cd);
		self.bcfg = None;
		self.b_buffeff = cbuff.have_cbuffeff_by_bid(bid);
		print "boutbuff __init__ %s %s"%(bid,self.b_buffeff);
		return
	def is_immediate(self):
		return True;
	def get_effect(self):
		return "";
	def get_group(self):
		return 0;
	def do(self,actor,combat_ins):
		if self.b_buffeff:
			self.bcfg.do(actor,combat_ins,self.value,self.done);
		else:
			for i in self.bcfg.proplist:#wrapp_ins
				i.set_actor(actor);
				b_minus = (int(self.value) < 0);
				i.do(combat_ins,b_minus);
		self.done = True;
		return
	def clear(self,actor,combat_ins):
		if self.b_buffeff:
			self.bcfg.clear(actor,combat_ins,self.value,self.done);
		else:
			for i in self.bcfg.proplist:#wrapp_ins
				i.set_actor(actor);
				b_minus = (int(self.value) < 0);
				i.clear(combat_ins,b_minus);
		self.done = False;
		return

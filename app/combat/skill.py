#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import app.config.skill as skillconfig
import buff
class skill(object):
	def __init__(self,sid,slv):
		self.sid = sid;
		self.slv = slv;
		self.stype = 0;#0 攻击 1 回复 2 辅助
		self.min_dstcnt = 1;
		self.max_dstcnt = 1;
		self.effect = "";
		self.groupid = 0;
		self.dst_buff_list = [];#buff:rate
		self.clr_dst_buff_list = [];#buff:rate
		self.src_buff_list = [];#buff:rate
		self.clr_src_buff_list = [];#buff:rate
		self.init();
		return
	def is_attacktype(self):
		return self.stype == 0;
	def _parse_bufflist(self,buff_str,b_add = False):
		ret = [];
		if buff_str != None and len(buff_str) > 0:
			blist = buff_str.split(';');
			for i in blist:
				bdlist = i.split(',');
				bid = int(float(bdlist[0]));
				brate = int(float(bdlist[1]));
				bcd = 0;
				if b_add:
					bcd = int(float(bdlist[2]));
				if bid >= 100:
					ret.append([buff.buff(bid,bcd),brate]);
				else:
					bgrouplist = buff.get_bufflist_bygroup(bid);
					for j in bgrouplist:
						j.cd = bcd;
						ret.append([j,brate]);
		return ret
	def init(self):
		skilldata = skillconfig.create_Skill(self.sid);
		for i in skilldata.skilldata:
			if i['lv'] == self.slv:
				self.min_dstcnt = i['targetmin'];
				self.max_dstcnt = i['targetmax'];
				self.effect = i['effect'];
				self.groupid = i['group'];
				self.stype = i['stype'];
				addbuff = i['addbuff'];
				self.dst_buff_list = self._parse_bufflist(addbuff,True)
				clrbuff = i['clrbuff'];
				self.clr_dst_buff_list = self._parse_bufflist(clrbuff);
				addbuffself = i['addbuffself'];
				self.src_buff_list = self._parse_bufflist(addbuffself,True);
				clrbuffself = i['clrbuffself'];
				self.clr_src_buff_list = self._parse_bufflist(clrbuffself);
				return;
		return
	def get_effect(self):
		return self.effect;
g_skill_config = {};
def create_skill(sid,slv):
	key = sid*1000+slv;
	if g_skill_config.has_key(key) == False:
		print 'init skill %s %s'%(sid,slv);
		g_skill_config[key] = skill(sid,slv);
	return g_skill_config[key];
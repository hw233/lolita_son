# -*- coding: utf-8 -*-

import cards_game

import config.cards as cards_cfg

class cards_mgr:
	def __init__(self):
		self.inst_dict = {};
		self.cardscfg_bygroup = {};
		for k,v in cards_cfg.cards_map.items():
			g = v.group
			if not self.cardscfg_bygroup.has_key(g):
				self.cardscfg_bygroup[g] = [];
			self.cardscfg_bygroup[g].push(k);

		cards_game.init_effect_map();
		return
	def get_inst(self,cid,c_data,dlv):
		if self.inst_dict.has_key(cid):
			if self.inst_dict[cid].b_end:
				self.del_inst(cid);
				return
			return self.inst_dict[cid];
		return
	def new_inst(self,cid,c_data,dlv):
		if not self.inst_dict.has_key(cid):
			self.inst_dict = cards_game.cards_game(cid,c_data,dlv,self.cardscfg_bygroup);
		return self.inst_dict[cid];
	def del_inst(self,cid):
		if self.inst_dict.has_key(cid):
			self.inst_dict[cid].dispose();
			del self.inst_dict[cid];
		return
	def req_enter(self,cid,c_data,dlv):
		return
	def req_quit(self,cid):
		return
	def req_click_card(self,cid,dst):
		return
	def req_use_card(self,cid,src,dst):
		return
	def req_quit(self,cid):
		return
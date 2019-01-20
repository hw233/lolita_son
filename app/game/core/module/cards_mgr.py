# -*- coding: utf-8 -*-

import app.base.game_module_mgr
from app.game.core.game_event_def import *
from app.protocol.ProtocolDesc import *
import app.protocol.netutil as netutil
from twisted.python import log
import app.util.helper as helper
import app.util.lang_config as lang_config
import app.game.memmode as memmode
from firefly.server.globalobject import GlobalObject
import app.game.core.game_module_def as game_module_def

import card.cards_game as cards_game

import app.config.cards as cards_cfg

class cards_mgr(app.base.game_module_mgr.game_module):
	def __init__(self):
		super(cards_mgr,self).__init__();
		self.inst_dict = {};
		self.cardscfg_bygroup = {};
		for k,v in cards_cfg.cards_map.items():
			g = v["group"]
			if not self.cardscfg_bygroup.has_key(g):
				self.cardscfg_bygroup[g] = [];
			self.cardscfg_bygroup[g].append(k);

		cards_game.init_effect_map();
		return
	def start(self):
		super(cards_mgr,self).start();
		self.register_net_event(C2S_CARDS_START,self.req_start_game)
		self.register_net_event(C2S_CARDS_FLIP,self.req_flip_card)
		self.register_net_event(C2S_CARDS_CLICK,self.req_click_card)
		self.register_net_event(C2S_CARDS_USE,self.req_use_card)
		self.register_net_event(C2S_CARDS_DEL,self.req_del_hand)
		self.register_net_event(C2S_CARDS_QUIT,self.req_quit)
		return
	def dispose(self):
		for k,v in self.inst_dict.items():
			v.dispose();
		self.inst_dict = {};
		super(cards_mgr,self).dispose();
		return
	def get_inst(self,cid):
		if self.inst_dict.has_key(cid):
			if self.inst_dict[cid].b_end:
				self.del_inst(cid);
				return
			return self.inst_dict[cid];
		return
	def new_inst(self,cid,c_data,dlv):
		if not self.inst_dict.has_key(cid):
			self.inst_dict[cid] = cards_game.cards_game(cid,c_data,dlv,self.cardscfg_bygroup,self);
		return self.inst_dict[cid];
	def del_inst(self,cid):
		if self.inst_dict.has_key(cid):
			self.inst_dict[cid].dispose();
			del self.inst_dict[cid];
		return
	#####
	def req_start_game(self,ud):
		did = ud["dId"];
		cid = ud["cId"];
		data = ud["data"];
		return
	def req_flip_card(self,ud):
		did = ud["dId"];
		cid = ud["cId"];
		data = ud["data"];
		src = data["id"];
		ins = self.get_inst(cid);
		if ins:
			ins.req_flip_card(src);
		return
	def req_click_card(self,ud):
		did = ud["dId"];
		cid = ud["cId"];
		data = ud["data"];
		src = data["id"];
		ins = self.get_inst(cid);
		if ins:
			ins.req_click_card(src);
		return
	def req_use_card(self,ud):
		did = ud["dId"];
		cid = ud["cId"];
		data = ud["data"];
		src = data["srcid"];
		dst = data["dstid"];
		ins = self.get_inst(cid);
		if ins:
			ins.req_use_card(src,dst);
		return
	def req_del_hand(self,ud):
		did = ud["dId"];
		cid = ud["cId"];
		data = ud["data"];
		dst = data["id"];
		ins = self.get_inst(cid);
		if ins:
			ins.req_del_hand(dst);
		return
	def req_quit(self,ud):
		did = ud["dId"];
		cid = ud["cId"];
		data = ud["data"];
		ins = self.get_inst(cid);
		if ins:
			ins.req_quit();
		return
	def send_cards_2c(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARDS_ARR,cid,send_data]);
		return
	def send_hands_2c(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARD_HANDS,cid,send_data]);
		return
	def send_pinfo_2c(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARDS_PLAYERINFO,cid,send_data]);
		return
	def send_start_2c(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[C2S_CARDS_START,cid,send_data]);
		return
	def send_turn_start(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARDS_TURNSTART,cid,send_data]);
		return
	def send_turn_end(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARDS_TURNEND,cid,send_data]);
		return
	def send_enter_dlv(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARDS_ENTERDLV,cid,send_data]);
		return
	def send_end_2c(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CADS_END,cid,send_data]);
		return
	def send_del_card(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARDS_DEL,cid,send_data]);
		return
	def send_del_handcard(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARDS_DELHAND,cid,send_data]);
		return
	def send_card_changed(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARDS_CHANGED,cid,send_data]);
		return
	def send_open_card(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARS_OPEN,cid,send_data]);
		return
	def send_atk_2c(self,cid,send_data):
		self.fire_event(EVENT_SEND2CLIENTBYCID,[S2C_CARDS_ATK,cid,send_data]);
		return
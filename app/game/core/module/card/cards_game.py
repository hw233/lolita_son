# -*- coding: utf-8 -*-

import app.config.cards as cards_cfg
import app.config.cards_dungeon as cards_dungeon
import app.config.cards_effect as cards_effect
import app.config.cards_initcards as cards_initcards
import app.config.cards_spell as cards_spell
import app.config.cards_exp as cards_exp
import random

CARD_TYPE_SWORD = 1
CARD_TYPE_MONSTER = 0
CARD_TYPE_ARMOR = 4
CARD_TYPE_SPELL = 2
CARD_TYPE_TRAP = 3

class card_effect(object):
	def __init__(self):
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		return True
class card_effect_berserk(card_effect):
	def __init__(self):
		super(card_effect_berserk,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		global CARD_TYPE_MONSTER
		hp = game_ins.hp;
		hp_max = game_ins.hp_max;
		if hp < hp_max:
			atk = hp_max - hp;
			for i in xrange(0,len(game_ins.cards_arr)):
				card = game_ins.cards_arr[i];
				if card.b_cover == False and card.cfg.type == CARD_TYPE_MONSTER:
					id = card.id;
					card.hp -= atk;
					game_ins.send_atk_2c(0,id,atk);
					if card.hp <= 0:
						game_ins.send_del_card(id);
						game_ins.del_card(id);
		return True
class card_effect_charm(card_effect):
	def __init__(self):
		super(card_effect_charm,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		if dst_card == None or dst_card.shape == 0 or dst_card.b_cover:
			return False
		global CARD_TYPE_MONSTER;
		if dst_card.cfg.type != CARD_TYPE_MONSTER:
			return False
		id = dst_card.id;
		shape = dst_card.shape;
		if game_ins.add_hand_card(shape):
			game_ins.send_del_card(id);
			game_ins.del_card(id);
			game_ins.send_hands_2c();
		else:
			return False
		return True
class card_effect_scout(card_effect):
	def __init__(self):
		super(card_effect_scout,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.scout_all();
		game_ins.send_cards_2c();
		return True

class card_effect_vanish(card_effect):
	def __init__(self):
		super(card_effect_vanish,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.vanish_all();
		game_ins.send_cards_2c();
		return True
class card_effect_exit(card_effect):
	def __init__(self):
		super(card_effect_exit,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.add_playerstamania(1);
		game_ins.add_playerhp(1);
		game_ins.add_playerexp(100);
		game_ins.send_pinfo_2c();
		game_ins.enter_next();
		return True
class card_effect_addhp(card_effect):
	def __init__(self):
		super(card_effect_addhp,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		if dst == 0:
			game_ins.add_playerhp(data);
			game_ins.send_pinfo_2c();
		return True
class card_effect_subhp(card_effect):
	def __init__(self):
		super(card_effect_subhp,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		if dst == 0:
			game_ins.sub_playerhp(data);
			game_ins.send_pinfo_2c();
		return True
class card_effect_addstamania(card_effect):
	def __init__(self):
		super(card_effect_addstamania,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.add_playerstamania(data);
		game_ins.send_pinfo_2c();
		return True
class card_effect_substamania(card_effect):
	def __init__(self):
		super(card_effect_substamania,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.sub_playerstamania(data);
		game_ins.send_pinfo_2c();
		return True
class card_effect_addarmor(card_effect):
	def __init__(self):
		super(card_effect_addarmor,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.add_playerarmor(data);
		game_ins.send_pinfo_2c();
		return True
class card_effect_subarmor(card_effect):
	def __init__(self):
		super(card_effect_subarmor,self).__init__();
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.sub_playerarmor(data);
		game_ins.send_pinfo_2c();
		return True
g_effect_map = {};
g_default_effect = card_effect();
def init_effect_map():
	global g_effect_map;
	g_effect_map[101] = card_effect_addhp();
	g_effect_map[102] = card_effect_subhp();
	g_effect_map[103] = card_effect_addstamania();
	g_effect_map[104] = card_effect_substamania();
	g_effect_map[109] = card_effect_addarmor();
	g_effect_map[110] = card_effect_subarmor();
	g_effect_map[199] = card_effect_exit();
	g_effect_map[105] = card_effect_charm();
	g_effect_map[106] = card_effect_vanish();
	g_effect_map[107] = card_effect_scout();
	g_effect_map[108] = card_effect_berserk();
	return
def get_effect_inst(id):
	global g_effect_map;
	global g_default_effect;
	if g_effect_map.has_key(id):
		return g_effect_map[id];
	return g_default_effect;
class card_spell_triger:
	def __init__(self,id):
		self.id = id;
		self.cfg = cards_spell.create_Cards_spell(self.id);
		self.efflist = [];
		self.dstlist = [];
		self.datalist = [];
		if self.cfg:
			eff = self.cfg.effect;
			dst = self.cfg.dst;
			data = self.cfg.data;
			if eff and len(eff) > 0:
				tmp = eff.split(',');
				for i in tmp:
					eid = int(float(i));
					self.efflist.append(eid);
					self.dstlist.append(0);
					self.datalist.append(0);
			if dst and len(dst) > 0:
				tmp = dst.split(',');
				idx = 0;
				for i in tmp:
					did = int(float(i));
					if idx < len(self.dstlist):
						self.dstlist[idx] = did;
					idx += 1;
			if data and len(data) > 0:
				tmp = dst.split(',');
				idx = 0;
				for i in tmp:
					did = int(float(i));
					if idx < len(self.datalist):
						self.datalist[idx] = did;
					idx += 1;
		return
	def run(self,src_card,dst_card,game_ins):
		ret = True;
		if self.cfg:
			for i in xrange(0,len(self.efflist)):
				eid = self.efflist[i];
				edst = self.dstlist[i];
				edata = self.datalist[i];
				e = get_effect_inst(eid);
				ret = ret and e.run(src_card,dst_card,game_ins,edst,edata);
		return ret
g_spell_map = {};
def get_spell_inst(spell_id):
	global g_spell_map;
	if not g_spell_map.has_key(spell_id):
		g_spell_map[spell_id] = card_spell_triger(spell_id);
	return g_spell_map[spell_id];
class card_base(object):
	def __init__(self,card_obj):
		self.card_obj = card_obj;
		return
	def click(self):
		
		return
	def use(self,dst_card):
		return
class card_equip(card_base):
	def __init__(self,card_obj):
		super(card_equip,self).__init__(card_obj);
		return
	def click(self):
		if self.card_obj.b_cover:
			self.card_obj.b_cover = False;
			self.card_obj.game_ins.send_open_card(self.card_obj.id,self.card_obj.shape);
			return
		else:
			id = self.card_obj.id;
			shape = self.card_obj.shape;
			
			if self.card_obj.game_ins.add_hand_card(shape):
				self.card_obj.game_ins.send_del_card(id);
				self.card_obj.game_ins.del_card(id);
				self.card_obj.game_ins.send_hands_2c();
		return
	def use(self,dst_card):
		global CARD_TYPE_SWORD
		global CARD_TYPE_ARMOR
		global CARD_TYPE_MONSTER
		if self.card_obj.cfg.type == CARD_TYPE_ARMOR:
			id = self.card_obj.id;
			self.card_obj.game_ins.add_playerarmor(self.card_obj.hp);
			self.card_obj.game_ins.send_pinfo_2c();
			self.card_obj.game_ins.send_del_handcard(id);
			self.card_obj.game_ins.del_handcard(id);
		elif self.card_obj.cfg.type == CARD_TYPE_SWORD:
			id = self.card_obj.id;
			atk = self.card_obj.atk;
			duration = self.card_obj.duration;
			dst = dst_card.id;
			if dst_card != None and dst_card.shape != 0 and dst_card.cfg.type == CARD_TYPE_MONSTER:
				dst_atk = dst_card.atk;
				self.card_obj.game_ins.sub_playerhp(dst_atk);
				self.card_obj.game_ins.send_pinfo_2c();
				self.card_obj.game_ins.send_atk_2c(id,dst,atk);
				self.card_obj.game_ins.send_atk_2c(dst,0,atk);
				duration -= 1;
				
				dst_card.hp -= atk;
				if dst_card.hp <= 0:
					exp = dst_card.extra;
					self.card_obj.game_ins.add_playerexp(exp);
					self.card_obj.game_ins.send_pinfo_2c();
					self.card_obj.game_ins.send_del_card(dst);
					self.card_obj.game_ins.del_card(dst);
				else:
					self.card_obj.game_ins.send_card_changed(dst,dst_card.shape,dst_card.atk,dst_card.hp,dst_card.duration);
				if duration <= 0:
					self.card_obj.game_ins.send_del_handcard(id);
					self.card_obj.game_ins.del_handcard(id);
				else:
					self.card_obj.duration = duration;
					self.card_obj.game_ins.send_card_changed(id,self.card_obj.shape,dst_card.atk,dst_card.hp,self.card_obj.duration);
		return
class card_spell(card_base):
	def __init__(self,card_obj):
		super(card_spell,self).__init__(card_obj);
		return
	def click(self):
		if self.card_obj.b_cover:
			self.card_obj.b_cover = False;
			self.card_obj.game_ins.send_open_card(self.card_obj.id,self.card_obj.shape);
		else:
			id = self.card_obj.id;
			shape = self.card_obj.shape;
			
			if self.card_obj.game_ins.add_hand_card(shape):
				self.card_obj.game_ins.send_del_card(id);
				self.card_obj.game_ins.del_card(id);
				self.card_obj.game_ins.send_hands_2c();
		return
	def use(self,dst_card):
		spell_id = self.card_obj.cfg.extra;
		ret = self.card_obj.game_ins.use_spell(spell_id,self.card_obj,dst_card);
		if ret != False:
			id = self.card_obj.id;
			self.card_obj.game_ins.send_del_handcard(id);
			self.card_obj.game_ins.del_handcard(id);
		return
class card_monster(card_base):
	def __init__(self,card_obj):
		super(card_monster,self).__init__(card_obj);
		return
	def click(self):
		if self.card_obj.b_cover:
			self.card_obj.b_cover = False;
			self.card_obj.game_ins.send_open_card(self.card_obj.id,self.card_obj.shape);
			return
		else:
			id = self.card_obj.id;
			exp = self.card_obj.cfg.extra;
			attack = self.card_obj.atk;
			playeratk = self.card_obj.game_ins.attack;
			self.card_obj.hp -= playeratk;
			if self.card_obj.hp <= 0:
				self.card_obj.game_ins.send_del_card(id);
				self.card_obj.game_ins.del_card(id);
			self.card_obj.game_ins.sub_playerhp(attack);
			self.card_obj.game_ins.add_playerexp(exp);
			self.card_obj.game_ins.send_pinfo_2c();
		return
	def use(self,dst_card):
		global CARD_TYPE_MONSTER
		id = self.card_obj.id;
		atk = self.card_obj.atk;
		hp = self.card_obj.hp;
		dst = dst_card.id;
		if dst_card != None and dst_card.shape != 0 and dst_card.cfg.type == CARD_TYPE_MONSTER:
			dst_atk = dst_card.atk;
			self.card_obj.hp -= dst_atk;
			dst_card.hp -= atk;
			self.card_obj.game_ins.send_atk_2c(id,dst,atk);
			self.card_obj.game_ins.send_atk_2c(dst,id,dst_atk);

			if dst_card.hp <= 0:
				exp = self.card_obj.cfg.extra;
				self.card_obj.game_ins.add_playerexp(exp);
				self.card_obj.game_ins.send_pinfo_2c();
				self.card_obj.game_ins.send_del_card(dst);
				self.card_obj.game_ins.del_card(dst);
			if self.card_obj.hp <= 0:
				self.card_obj.game_ins.send_del_handcard(id);
				self.card_obj.game_ins.del_handcard(id);
			
		
		return
class card_trap(card_base):
	def __init__(self,card_obj):
		super(card_trap,self).__init__(card_obj);
		return
	def click(self):
		if self.card_obj.b_cover:
			self.card_obj.b_cover = False;
			self.card_obj.game_ins.send_open_card(self.card_obj.id,self.card_obj.shape);
			if self.card_obj.cfg.react == 1:
				spell_id = self.card_obj.cfg.extra;
				ret = self.card_obj.game_ins.use_spell(spell_id,self.card_obj,None);
				if ret != False:
					id = self.card_obj.id;
					self.card_obj.game_ins.send_del_card(id);
					self.card_obj.game_ins.del_card(id);
		else:
			if self.card_obj.cfg.react == 2 or self.card_obj.cfg.react == 0:
				spell_id = self.card_obj.cfg.extra;
				ret = self.card_obj.game_ins.use_spell(spell_id,self.card_obj,None);
				if ret != False:
					id = self.card_obj.id;
					self.card_obj.game_ins.send_del_card(id);
					self.card_obj.game_ins.del_card(id);
				
		return
class card:
	def __init__(self,id,game_ins):
		self.shape = 0;
		self.cfg = None;
		self.id = id;
		self.b_cover = True;
		self.game_ins = game_ins;
		self.card_logic = None;
		self.duration = 0;
		self.hp = 0;
		self.atk = 0;
		return
	def dispose(self):
		return
	def _get_card_logic(self,tp):
		global CARD_TYPE_SWORD
		global CARD_TYPE_MONSTER
		global CARD_TYPE_ARMOR
		global CARD_TYPE_SPELL
		global CARD_TYPE_TRAP
		if tp == CARD_TYPE_SWORD or tp == CARD_TYPE_ARMOR:
			return card_equip(self);
		elif tp == CARD_TYPE_SPELL:
			return card_spell(self);
		elif tp == CARD_TYPE_TRAP:
			return card_trap(self);
		return card_monster(self);
	def re_init(self,shape):
		self.shape = shape;
		self.cfg = None;
		self.card_logic = None;
		self.duration = 0;
		self.hp = 0;
		self.atk = 0;
		self.extra = 0;
		if shape != 0:
			self.cfg = cards_cfg.create_Cards(self.shape);
			self.card_logic = self._get_card_logic(self.cfg.type);
			self.duration = self.cfg.duration;
			self.hp = self.cfg.hp;
			self.atk = self.cfg.attack;
			self.extra = self.cfg.extra;
		self.b_cover = True;
		return
	def click(self):
		if self.shape == 0:
			return;
		self.card_logic.click();
		return
	def use(self,dst_card):
		if self.shape == 0:
			return;
		self.card_logic.use(dst_card);
		return
class cards_game:
	def __init__(self,cid,c_data,dlv,cardscfg_bygroup,parent):
		self.parent = parent
		self.b_end = False;
		self.cid = cid;
		self.c_data = c_data;
		self.clv = 1;
		if c_data.has_key('lv'):
			self.clv = c_data['lv'];#角色等级

		self.hp = 10;
		self.hp_max = 10;
		self.stamania = 10;
		self.exp = 0;
		self.stamania_max = 10;
		self.base_atk = 1;
		self.exp_max = 100;
		self.armor = 0;
		self.extra_atk = 0;
		self.attack = 1;

		clv_expcfg = cards_exp.create_Cards_exp(self.clv);
		if clv_expcfg != None:
			self.hp_max = clv_expcfg.hpmax;
			self.stamania_max = clv_expcfg.stamaniamax;
			self.base_atk = clv_expcfg.atk;
			self.exp_max = clv_expcfg.exp;

		if c_data.has_key('hp'):
			self.hp = c_data['hp'];
		if c_data.has_key('stamania'):
			self.stamania = c_data['stamania'];
		if c_data.has_key('exp'):
			self.exp = c_data['exp'];
		
		if c_data.has_key('atk'):
			self.extra_atk = c_data['atk'];

		self.attack = self.base_atk + self.extra_atk;
		if c_data.has_key('armor'):
			self.armor = c_data['armor'];

		self.dlv = dlv;#
		self.b_enter_next = False;

		self.card_id_start = 0;
		self.cardscfg_bygroup = cardscfg_bygroup;
		self.cards_arr = [];
		self.cards_map = {};

		self.hand_cards_arr = [];
		self.hand_cards_map = {};

		self.hand_cur_max = 5;
		
		return
	def _gen_cardid(self):
		self.card_id_start += 1;
		return self.card_id_start;
	def _new_card_ins(self):
		return card(self._gen_cardid(),self);
	def _del_card_ins(self,c):
		c.dispose();
		return
	def dispose(self):
		return
	def _reset_arr(self):
		for i in self.cards_arr:
			self._del_card_ins(i);
		self.cards_arr = [];
		self.cards_map = {};
		return
	def _reset_hand_arr(self):
		for i in self.hand_cards_arr:
			self._del_card_ins(i);
		self.hand_cards_arr = [];
		self.hand_cards_map = {};
		return
	def _get_randomcardid_bygroup(self,g):
		if self.cardscfg_bygroup.has_key(g):
			cards_list = self.cardscfg_bygroup[g];
			count = len(cards_list);
			if count > 0:
				idx = random.randint(0,count-1);
				return cards_list[idx];
		return 0;
	def start(self):
		self.init_cards();
		self.init_handscards();

		self.send_start_2c();
		self.send_pinfo_2c();
		self.send_enter_dlv(self.dlv):
		self.send_cards_2c();
		self.send_hands_2c();
		self.send_turn_start();

		return
	def init_cards(self):
		self._reset_arr();
		
		dungeon_cfg = cards_dungeon.create_Cards_dungeon(self.dlv);
		if dungeon_cfg == None:
			dungeon_cfg = cards_dungeon.create_Cards_dungeon(1);
		cards_min = dungeon_cfg.min;
		cards_max = dungeon_cfg.max;
		
		tmp_group_str = dungeon_cfg.equip_group;
		equiplist = [];
		if tmp_group_str != None and len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				equiplist.append(int(float(i)));
		equip_min = dungeon_cfg.equip_min;
		equip_max = dungeon_cfg.equip_max;

		equip_num = random.randint(equip_min,equip_max);

		tmp_group_str = dungeon_cfg.spell_group;
		spelllist = [];
		if tmp_group_str != None and len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				spelllist.append(int(float(i)));
		spell_min = dungeon_cfg.spell_min;
		spell_max = dungeon_cfg.spell_max;

		spell_num = random.randint(spell_min,spell_max);

		tmp_group_str = dungeon_cfg.trap_group;
		traplist = [];
		if tmp_group_str != None and len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				traplist.append(int(float(i)));
		trap_min = dungeon_cfg.trap_min;
		trap_max = dungeon_cfg.trap_max;

		trap_num = random.randint(trap_min,trap_max);

		tmp_group_str = dungeon_cfg.monster_group;
		monsterlist = [];
		if tmp_group_str != None and len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				monsterlist.append(int(float(i)));


		tmp_cardid_list = [];
		tmp_cardid_list.append(9999)#exit
		equip_group_num = len(equiplist);
		if equip_group_num > 0:
			for i in xrange(0,equip_num):
				group_idx = random.randint(0,equip_group_num - 1);
				card_shape = self._get_randomcardid_bygroup(equiplist[group_idx]);
				tmp_cardid_list.append(card_shape);

		spell_group_num = len(spelllist);
		if spell_group_num > 0:
			for i in xrange(0,spell_num):
				group_idx = random.randint(0,spell_group_num - 1);
				card_shape = self._get_randomcardid_bygroup(spelllist[group_idx]);
				tmp_cardid_list.append(card_shape);

		trap_group_num = len(traplist);
		if trap_group_num > 0:
			for i in xrange(0,trap_num):
				group_idx = random.randint(0,trap_group_num - 1);
				card_shape = self._get_randomcardid_bygroup(traplist[group_idx]);
				tmp_cardid_list.append(card_shape);
		cur_num = len(tmp_cardid_list);
		if cur_num < cards_min:
			monster_group_num = len(monsterlist);
			if monster_group_num > 0:
				for i in xrange(0,cards_min - cur_num):
					group_idx = random.randint(0,monster_group_num - 1);
					card_shape = self._get_randomcardid_bygroup(monsterlist[group_idx]);
					tmp_cardid_list.append(card_shape);

		random.shuffle(tmp_cardid_list);
		count = 0;
		for i in tmp_cardid_list:
			if count >= cards_max:
				break;
			c = self._new_card_ins();
			c.re_init(i);
			self.cards_arr.append(c);
			self.cards_map[c.id] = c;
		return
	def print_cards(self):
		print "print_cards %d"%(len(self.cards_arr));
		for i in xrange(0,len(self.cards_arr)):
			c = self.cards_arr[i];
			print c.id,c.shape,c.b_cover
		return
	def init_handscards(self):
		self._reset_hand_arr();

		initcards_cfg = cards_initcards.create_Cards_initcards(self.clv);
		if initcards_cfg == None:
			initcards_cfg = initcards_cfg.create_Cards_initcards(1);
		cards_max = initcards_cfg.count;
		self.hand_cur_max = cards_max;
		tmp_group_str = initcards_cfg.equip_group;
		equiplist = [];
		if tmp_group_str != None and len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				equiplist.append(int(float(i)));
		equip_min = initcards_cfg.equip_min;
		equip_max = initcards_cfg.equip_max;

		equip_num = random.randint(equip_min,equip_max);

		tmp_group_str = initcards_cfg.spell_group;
		spelllist = [];
		if tmp_group_str != None and len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				spelllist.append(int(float(i)));

		tmp_cardid_list = [];
		equip_group_num = len(equiplist);
		if equip_group_num > 0:
			for i in xrange(0,equip_num):
				group_idx = random.randint(0,equip_group_num - 1);
				card_shape = self._get_randomcardid_bygroup(equiplist[group_idx]);
				tmp_cardid_list.append(card_shape);

		cur_num = len(tmp_cardid_list);
		if cur_num < cards_max:
			spell_group_num = len(spelllist);
			if spell_group_num > 0:
				for i in xrange(0,cards_max - cur_num):
					group_idx = random.randint(0,spell_group_num - 1);
					card_shape = self._get_randomcardid_bygroup(spelllist[group_idx]);
					tmp_cardid_list.append(card_shape);
		random.shuffle(tmp_cardid_list);
		count = 0;
		for i in tmp_cardid_list:
			if count >= self.hand_cur_max:
				break;
			c = self._new_card_ins();
			c.re_init(i);
			c.b_cover = False;
			self.hand_cards_arr.append(c);
			self.hand_cards_map[c.id] = c;
			count += 1;
			
		return
	def print_handcards(self):
		print "print_handcards %d"%(len(self.hand_cards_arr))
		for i in xrange(0,len(self.hand_cards_arr)):
			c = self.hand_cards_arr[i];
			print c.id,c.shape
		return
	
	#get client request end
	###
	def scout_all(self):
		for i in self.cards_arr:
			i.b_cover = False;
		return
	def vanish_all(self):
		for i in self.cards_arr:
			i.b_cover = True;
		return
	def enter_next(self):
		print "card enter_next"
		self.b_enter_next = True;
		return

	def add_hand_card(self,shape):
		if len(self.hand_cards_arr) >= self.hand_cur_max:
			print "hands is full"
			return False;
		c = self._new_card_ins();
		c.re_init(shape);
		c.b_cover = False;
		self.hand_cards_arr.append(c);
		self.hand_cards_map[c.id] = c;
		return True
	def add_playerarmor(self,v):
		self.armor += v;
		return
	def sub_playerarmor(self,v):
		self.armor -= v;
		return
	def add_playerstamania(self,v):
		self.stamania += v;
		return
	def sub_playerstamania(self,v):
		self.stamania -= v;
		return
	def add_playerhp(self,v):
		self.hp += v;
		return
	def sub_playerhp(self,v):
		if self.armor > 0:
			last_v = v - self.armor;
			self.armor -= v;
			v = last_v;
		if v > 0:
			self.hp -= v;
		return
	def add_playerexp(self,exp):
		self.exp += exp;
		#todo 升级的变化，增加的属性
		if self.exp >= self.exp_max:
			clv_expcfg = cards_exp.create_Cards_exp(self.clv+1);
			if clv_expcfg != None:
				self.hp_max = clv_expcfg.hpmax;
				self.stamania_max = clv_expcfg.stamaniamax;
				self.base_atk = clv_expcfg.atk;
				self.attack = self.base_atk + self.extra_atk;
				self.clv += 1;
				self.exp = 0;
				self.hp = self.hp_max;
				self.stamania = self.stamania_max;
		return
	def use_spell(self,spell_id,src_card,dst_card):
		print "card use_spell %d"%(spell_id);
		spell_inst = get_spell_inst(spell_id);
		return spell_inst.run(src_card,dst_card,self);
		
	def del_card(self,dst):
		for i in self.cards_arr:
			if i.id == dst:
				self._del_card_ins(i);
				self.cards_arr.remove(i);
				del self.cards_map[i.id];
				return
		return
	def del_handcard(self,dst):
		for i in self.hand_cards_arr:
			if i.id == dst:
				self._del_card_ins(i);
				self.hand_cards_arr.remove(i);
				del self.hand_cards_map[i.id];
				return
		return
	###
	#get client request begin
	def req_flip_card(self,src):
		if self.cards_map.has_key(src) == False:
			return
		use_card = self.cards_map[src];
		
		if use_card.shape == 0 or use_card.b_cover == False:
			return
		self.send_turn_end();
		#先扣体力，看是否需要扣血 todo
		self.stamania -= 1;
		if self.stamania < 0:
			self.stamania = 0;
			self.hp -= 1;
			#
		#怪物先行动，避免刚翻开的怪物直接造成伤害
		global CARD_TYPE_MONSTER
		for i in xrange(0,len(self.cards_arr)):
			card = self.cards_arr[i];
			if card.b_cover == False and card.cfg.type == CARD_TYPE_MONSTER:
				id = card.id;
				atk = card.atk;
				self.sub_playerhp(atk);
				self.send_atk_2c(id,0,atk);
				self.send_pinfo_2c();
		use_card.click();

		#结算血量，看游戏是否结束 todo
		if self.hp <= 0:
			self.b_end = True;
			self.send_turn_start();
			self.send_end_2c();
			return
		#修正数值
		if self.armor < 0:
			self.armor = 0;
		if self.hp > self.hp_max:
			self.hp = self.hp_max;
		if self.stamania > self.stamania_max:
			self.stamania = self.stamania_max;
		self.send_pinfo_2c();
		self.send_turn_start();
		return
	def req_click_card(self,src):
		if self.cards_map.has_key(src) == False:
			return
		use_card = self.cards_map[src];
		if use_card.shape == 0 or use_card.b_cover == True:
			return
		self.send_turn_end();
		#先扣体力，看是否需要扣血 todo
		self.stamania -= 1;
		if self.stamania < 0:
			self.stamania = 0;
			self.hp -= 1;
		#
		use_card.click();
		
		#结算血量，看游戏是否结束 todo
		if self.hp <= 0:
			self.b_end = True;
			self.send_turn_start();
			self.send_end_2c();
			return
		#怪物行动
		global CARD_TYPE_MONSTER
		for i in xrange(0,len(self.cards_arr)):
			card = self.cards_arr[i];
			if card.b_cover == False and card.cfg.type == CARD_TYPE_MONSTER:
				id = card.id;
				atk = card.atk;
				self.sub_playerhp(atk);
				self.send_atk_2c(id,0,atk);
				self.send_pinfo_2c();
		#再次结算血量，看游戏是否结束 todo
		if self.hp <= 0:
			self.b_end = True;
			self.send_turn_start();
			self.send_end_2c();
			return
		if self.armor < 0:
			self.armor = 0;
		if self.hp > self.hp_max:
			self.hp = self.hp_max;
		if self.stamania > self.stamania_max:
			self.stamania = self.stamania_max;
		#判断是否进入下一关
		if self.b_enter_next:
			self.b_enter_next = False;
			self.dlv += 1;
			self.init_cards();
			self.send_enter_dlv(self.dlv):
			self.send_cards_2c();
		self.send_pinfo_2c();
		self.send_turn_start();
		return
	def req_use_card(self,src,dst):
		if self.hand_cards_map.has_key(src) == False:
			return
		src_card = self.hand_cards_map[src];
		if src_card.shape == 0:
			return
		if src_card.b_cover:
			return
		dst_card = None;
		if dst != 0:
			if self.cards_map.has_key(dst) == False:
				return
			dst_card = self.cards_map[dst]
			if dst_card.b_cover:
				return
		self.send_turn_end();
		src_card.use(dst_card);
		#结算血量，看游戏是否结束 todo
		#
		if self.hp <= 0:
			self.b_end = True;
			self.send_end_2c();
		if self.armor < 0:
			self.armor = 0;
		if self.hp > self.hp_max:
			self.hp = self.hp_max;
		if self.stamania > self.stamania_max:
			self.stamania = self.stamania_max;
		#判断是否进入下一关
		if self.b_enter_next:
			self.b_enter_next = False;
			self.dlv += 1;
			self.init_cards();
			self.send_enter_dlv(self.dlv):
			self.send_cards_2c();
		self.send_pinfo_2c();
		self.send_turn_start();
		return
	def req_del_hand(self,dst):
		self.del_handcard(dst);
		self.send_hands_2c();
		return
	def req_quit(self):
		self.b_end = True;
		self.send_end_2c();
		return
	#send packet func begin
	def send_cards_2c(self):
		print "send_cards_2c";

		send_data = {};
		send_data['idlist'] = [];
		send_data['shapelist'] = [];
		send_data['atklist'] = [];
		send_data['hplist'] = [];
		send_data['durationlist'] = [];

		idx = 0;
		for i in self.cards_arr:
			sendshape = 0;
			sendhp = 0;
			sendatk = 0;
			senddura = 0;
			if i.b_cover != False:
				sendshape = i.shape;
				sendhp = i.hp;
				sendatk = i.atk;
				senddura = i.duration;
			print "idx:%d %d %d %d %d %d"%(idx,i.id,sendshape,i.shape,i.hp,i.atk,i.duration);
			idx += 1;
			send_data['idlist'].append(i.id);
			send_data['shapelist'].append(sendshape);
			send_data['atklist'].append(sendhp);
			send_data['hplist'].append(sendatk);
			send_data['durationlist'].append(senddura);
		if self.parent:
			self.parent.send_cards_2c(self.cid,send_data);
		return
	def send_hands_2c(self):
		print "send_hands_2c";
		send_data = {};
		send_data['idlist'] = [];
		send_data['shapelist'] = [];
		send_data['atklist'] = [];
		send_data['hplist'] = [];
		send_data['durationlist'] = [];

		idx = 0;
		for i in self.hand_cards_arr:
			print "idx:%d %d %d %d %d %d"%(idx,i.id,i.shape,i.hp,i.atk,i.duration);
			send_data['idlist'].append(i.id);
			send_data['shapelist'].append(i.shape);
			send_data['atklist'].append(i.atk);
			send_data['hplist'].append(i.hp);
			send_data['durationlist'].append(i.duration);
			idx += 1;


		if self.parent:
			self.parent.send_hands_2c(self.cid,send_data);
		return
	def send_pinfo_2c(self):
		print "send_pinfo_2c %d %d %d %d %d %d %d %d %d"%(self.hp,self.armor,self.attack,self.exp,self.dlv,self.clv,self.hp_max,self.stamania_max,self.stamania);
		send_data = {};
		if self.parent:
			send_data["hp"] = self.hp;
			send_data["stamina"] = self.stamania;
			send_data["armor"] = self.armor;
			send_data["atk"] = self.attack;
			send_data["exp"] = self.exp;
			send_data["dlv"] = self.dlv;
			send_data["clv"] = self.clv;
			send_data["hpmax"] = self.hp_max;
			send_data["staminamax"] = self.stamania_max;

			self.parent.send_pinfo_2c(self.cid,send_data);
		return
	def send_start_2c(self):
		print "send_start_2c";

		send_data = {};
		if self.parent:
			self.parent.send_start_2c(self.cid,send_data);
		return
	def send_turn_start(self):
		print "send_turn_start";

		send_data = {};
		if self.parent:
			self.parent.send_turn_start(self.cid,send_data);
		return
	def send_turn_end(self):
		print "send_turn_end";

		send_data = {};
		if self.parent:
			self.parent.send_turn_end(self.cid,send_data);
		return
	def send_enter_dlv(self,dlv):
		print "send_enter_dlv %s"%(dlv);

		send_data = {};
		send_data["lv"] = dlv;
		if self.parent:
			self.parent.send_enter_dlv(self.cid,send_data);
		return
	def send_end_2c(self):
		print "send_end_2c";

		send_data = {};
		if self.parent:
			self.parent.send_end_2c(self.cid,send_data);
		return
	def send_del_card(self,dst):
		print "send_del_card %s"%(dst);

		send_data = {};
		send_data["id"] = dst;
		if self.parent:
			self.parent.send_del_card(self.cid,send_data);
		return
	def send_del_handcard(self,dst):
		print "send_del_handcard %s"%(dst);

		send_data = {};
		send_data["id"] = dst;
		if self.parent:
			self.parent.send_del_handcard(self.cid,send_data);
		return
	def send_card_changed(self,dst,shape,atk,hp,duration):
		print "send_card_changed %s %s %s %s %s"%(dst,shape,atk,hp,duration);

		send_data = {};
		send_data["id"] = dst;
		send_data["shape"] = shape;
		send_data["atk"] = atk;
		send_data["hp"] = hp;
		send_data["duration"] = duration;
		if self.parent:
			self.parent.send_card_changed(self.cid,send_data);
		return
	def send_open_card(self,dst,card_shape):
		print "send_open_card %s,%s"%(dst,card_shape);

		send_data = {};
		send_data["id"] = dst;
		send_data["shape"] = card_shape;
		if self.parent:
			self.parent.send_open_card(self.cid,send_data);
		return
	def send_atk_2c(self,src,dst,v):
		print "send_atk_2c %s,%s,%s"%(src,dst,v);

		send_data = {};
		send_data["srcid"] = src;
		send_data["dstid"] = dst;
		send_data["value"] = v;
		if self.parent:
			self.parent.send_atk_2c(self.cid,send_data);
		return
	#send packet func end
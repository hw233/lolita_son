# -*- coding: utf-8 -*-

import config.cards as cards_cfg
import config.cards_dungeon as cards_dungeon
import config.cards_effect as cards_effect
import config.cards_initcards as cards_initcards
import config.cards_spell as cards_spell
import random

CARD_TYPE_SWORD = 1
CARD_TYPE_MONSTER = 0
CARD_TYPE_ARMOR = 4
CARD_TYPE_SPELL = 2
CARD_TYPE_TRAP = 3

class card_effect:
	def __init__(self):
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		return
class card_effect_exit(card_effect):
	def __init__(self):
		super(card_effect_exit,self).__init__(self);
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.enter_next();
		return
class card_effect_addhp(card_effect):
	def __init__(self):
		super(card_effect_addhp,self).__init__(self);
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		if dst == 0:
			game_ins.add_playerhp(data);
			game_ins.send_pinfo_2c();
		return
class card_effect_subhp(card_effect):
	def __init__(self):
		super(card_effect_subhp,self).__init__(self);
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		if dst == 0:
			game_ins.sub_playerhp(data);
			game_ins.send_pinfo_2c();
		return
class card_effect_addstamania(card_effect):
	def __init__(self):
		super(card_effect_addstamania,self).__init__(self);
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.add_playerstamania(data);
		game_ins.send_pinfo_2c();
		return
class card_effect_substamania(card_effect):
	def __init__(self):
		super(card_effect_substamania,self).__init__(self);
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.sub_playerstamania(data);
		game_ins.send_pinfo_2c();
		return
class card_effect_addarmor(card_effect):
	def __init__(self):
		super(card_effect_addarmor,self).__init__(self);
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.add_playerarmor(data);
		game_ins.send_pinfo_2c();
		return
class card_effect_subarmor(card_effect):
	def __init__(self):
		super(card_effect_subarmor,self).__init__(self);
		return
	def run(self,src_card,dst_card,game_ins,dst,data):
		game_ins.sub_playerarmor(data);
		game_ins.send_pinfo_2c();
		return
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
	return
def get_effect_inst(id):
	global g_effect_map;
	global g_default_effect;
	if g_effect_map.has_key(id):
		return g_effect_map[id];
	return g_default_effect;
class card_spell:
	def __init__(self,id):
		self.id = id;
		self.cfg = cards_spell.create_Cards_spell(self.id);
		self.efflist = [];
		self.dstlist = [];
		self.datalist = [];
		if self.cfg:
			eff = cfg.effect;
			dst = cfg.dst;
			data = cfg.data;
			if eff and len(eff) > 0:
				tmp = eff.split(',');
				for i in tmp:
					eid = int(float(i));
					self.efflist.push(eid);
					self.dstlist.push(0);
					self.datalist.push(0);
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
		if self.cfg:
			for i in xrange(0,len(self.efflist)):
				eid = self.efflist[i];
				edst = self.dstlist[i];
				edata = self.datalist[i];
				e = get_effect_inst(eid);
				e.run(src_card,dst_card,game_ins,edst,edata);
		return
g_spell_map = {};
def get_spell_inst(spell_id):
	global g_spell_map;
	if not g_spell_map.has_key(spell_id):
		g_spell_map[spell_id] = card_spell(spell_id);
	return g_spell_map[spell_id];
class card_base:
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
			self.card_obj.game_ins.send_del_card(id);
			self.card_obj.game_ins.del_card(id);
			if self.card_obj.game_ins.add_hand_card(shape):
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
			self.card_obj.game_ins.send_del_card(id);
			self.card_obj.game_ins.del_card(id);
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
					self.card_obj.game_ins.send_del_card(id);
					self.card_obj.game_ins.del_card(id);
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
			return
		else:
			id = self.card_obj.id;
			shape = self.card_obj.shape;
			self.card_obj.game_ins.send_del_card(id);
			self.card_obj.game_ins.del_card(id);
			if self.card_obj.game_ins.add_hand_card(shape):
				self.card_obj.game_ins.send_hands_2c();
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
				self.card_obj.game_ins.send_del_card(id);
				self.card_obj.game_ins.del_card(id);
			
		
		return
class card_trap(card_base):
	def __init__(self,card_obj):
		super(card_trap,self).__init__(card_obj);
		return
	def click(self):
		if self.card_obj.b_cover:
			self.card_obj.b_cover = False;
			self.card_obj.game_ins.send_open_card(self.card_obj.id,self.card_obj.shape);
			if self.card_obj.cfg.react != 0:
				spell_id = self.card_obj.cfg.extra;
				self.card_obj.game_ins.use_spell(spell_id,self.card_obj,None);
				id = self.card_obj.id;
				self.card_obj.game_ins.send_del_card(id);
				self.card_obj.game_ins.del_card(id);
		else:
			if self.card_obj.cfg.react == 0:
				spell_id = self.card_obj.cfg.extra;
				self.card_obj.game_ins.use_spell(spell_id,self.card_obj,None);
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
		if shape != 0:
			self.cfg = cards_cfg.create_Cards(self.shape);
			self.card_logic = self._get_card_logic(self.cfg.type);
			self.duration = self.cfg.duration;
			self.hp = self.cfg.hp;
			self.atk = self.cfg.attack;
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
	def __init__(self,cid,c_data,dlv,cardscfg_bygroup):
		self.b_end = False;
		self.cid = cid;
		self.c_data = c_data;

		self.clv = c_data['lv'];#角色等级
		self.hp = c_data['hp'];
		self.stamaina = c_data['stamania'];
		self.exp = c_data['exp'];
		self.glv = c_data['glv'];#当前游戏里角色等级
		self.attack = c_data['atk'];
		self.armor = c_data['armor'];

		self.dlv = dlv;#
		self.b_enter_next = False;

		self.hp_max = 10;

		self.max_num = 100;
		self.card_id_start = 0;

		self.cardscfg_bygroup = cardscfg_bygroup;
		self.cards_arr = [];
		for i in xrange(0,self.max_num):
			c = card(self.card_id_start+i,self);
			self.cards_arr.push(c);

		self.hand_cards_arr = [];
		self.hand_max_num = 10;
		self.hand_cur_max = 5;
		self.hand_id_start = 1000;
		for i in xrange(0,self.hand_max_num):
			c = card(self.hand_id_start+i,self);
			self.hand_cards_arr.push(c);
		return
	def dispose(self):
		return
	def _reset_arr(self):
		for i in xrange(0,self.max_num):
			self.cards_arr[i][j].re_init(0);
		return
	def _reset_hand_arr(self):
		for i in xrange(0,self.hand_max_num):
			self.hand_cards_arr[i].re_init(0);
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
		return
	def init_cards(self):
		self._reset_arr();
		
		dungeon_cfg = cards_dungeon.create_Cards_dungeon(self.dlv);
		if dungeon_cfg == None:
			dungeon_cfg = cards_dungeon.create_Cards_dungeon(1);
		cards_min = dungeon_cfg.min;
		cards_max = dungeon_cfg.max;
		if cards_max >= self.max_num:
			cards_max = self.max_num;
		
		tmp_group_str = dungeon_cfg.equip_group;
		equiplist = [];
		if tmp_group_str != None && len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				equiplist.push(int(float(i)));
		equip_min = dungeon_cfg.equip_min;
		equip_max = dungeon_cfg.equip_max;

		equip_num = random.randint(equip_min,equip_max);

		tmp_group_str = dungeon_cfg.spell_group;
		spelllist = [];
		if tmp_group_str != None && len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				spelllist.push(int(float(i)));
		spell_min = dungeon_cfg.spell_min;
		spell_max = dungeon_cfg.spell_max;

		spell_num = random.randint(spell_min,spell_max);

		tmp_group_str = dungeon_cfg.trap_group;
		traplist = [];
		if tmp_group_str != None && len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				traplist.push(int(float(i)));
		trap_min = dungeon_cfg.trap_min;
		trap_max = dungeon_cfg.trap_max;

		trap_num = random.randint(trap_min,trap_max);

		tmp_group_str = dungeon_cfg.monster_group;
		monsterlist = [];
		if tmp_group_str != None && len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				monsterlist.push(int(float(i)));


		tmp_cardid_list = [];
		tmp_cardid_list.push(9999)#exit
		equip_group_num = len(equiplist);
		if equip_group_num > 0:
			for i in xrange(0,equip_num):
				group_idx = random.randint(0,equip_group_num - 1);
				card_shape = self._get_randomcardid_bygroup(equiplist[group_idx]);
				tmp_cardid_list.push(card_shape);

		spell_group_num = len(spelllist);
		if spell_group_num > 0:
			for i in xrange(0,spell_num):
				group_idx = random.randint(0,spell_group_num - 1);
				card_shape = self._get_randomcardid_bygroup(spelllist[group_idx]);
				tmp_cardid_list.push(card_shape);

		trap_group_num = len(traplist);
		if trap_group_num > 0:
			for i in xrange(0,trap_num):
				group_idx = random.randint(0,trap_group_num - 1);
				card_shape = self._get_randomcardid_bygroup(traplist[group_idx]);
				tmp_cardid_list.push(card_shape);
		cur_num = len(tmp_cardid_list);
		if cur_num < cards_min:
			monster_group_num = len(monsterlist);
			if monster_group_num > 0:
				for i in xrange(0,cards_min - cur_num):
					group_idx = random.randint(0,monster_group_num - 1);
					card_shape = self._get_randomcardid_bygroup(monsterlist[group_idx]);
					tmp_cardid_list.push(card_shape);

		random.shuffle(tmp_cardid_list);
		count = 0;
		for i in xrange(0,cards_max):
			self.cards_arr[i].re_init(tmp_cardid_list[count]);
			count += 1;
			if count >= len(tmp_cardid_list):
				return
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
		if tmp_group_str != None && len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				equiplist.push(int(float(i)));
		equip_min = initcards_cfg.equip_min;
		equip_max = initcards_cfg.equip_max;

		equip_num = random.randint(equip_min,equip_max);

		tmp_group_str = initcards_cfg.spell_group;
		spelllist = [];
		if tmp_group_str != None && len(tmp_group_str) > 0:
			tmp = tmp_group_str.split(',');
			for i in tmp:
				spelllist.push(int(float(i)));

		tmp_cardid_list = [];
		equip_group_num = len(equiplist);
		if equip_group_num > 0:
			for i in xrange(0,equip_num):
				group_idx = random.randint(0,equip_group_num - 1);
				card_shape = self._get_randomcardid_bygroup(equiplist[group_idx]);
				tmp_cardid_list.push(card_shape);

		cur_num = len(tmp_cardid_list);
		if cur_num < cards_max:
			spell_group_num = len(spelllist);
			if spell_group_num > 0:
				for i in xrange(0,cards_max - cur_num):
					group_idx = random.randint(0,spell_group_num - 1);
					card_shape = self._get_randomcardid_bygroup(spelllist[group_idx]);
					tmp_cardid_list.push(card_shape);
		random.shuffle(tmp_cardid_list);
		count = 0;
		for i in tmp_cardid_list:
			self.hand_cards_arr[count].re_init(i);
			self.hand_cards_arr[count].b_cover = False;
			count += 1;
			if count >= self.hand_max_num:
				return
		return
	
	#get client request begin
	def req_click_card(self,src):
		if src < self.card_id_start:
			return
		src_pos = src - self.card_id_start;#trick
		if src_pos >= self.max_num:
			return
		use_card = self.cards_arr[src_pos];
		if use_card.shape == 0:
			return
		use_card.click();
		#先扣体力，看是否需要扣血 todo
		self.stamaina -= 1;
		if self.stamaina < 0:
			self.stamaina = 0;
			self.hp -= 1;
		#
		#结算血量，看游戏是否结束 todo
		if self.hp <= 0:
			self.b_end = True;
			self.send_end_2c();
			return
		#怪物行动，todo
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
			self.send_end_2c();
			return
		if self.armor < 0:
			self.armor = 0;

		#判断是否进入下一关
		if self.b_enter_next:
			self.b_enter_next = False;
			self.dlv += 1;
			self.init_cards();
			self.send_cards_2c();
		self.send_pinfo_2c();
		
		return
	def req_use_card(self,src,dst):
		if src < self.hand_id_start:
			return
		src_pos = src - self.hand_id_start;
		if src_pos >= self.hand_max_num:
			return
		src_card = self.hand_cards_arr[src_pos];
		if src_card.shape == 0:
			return
		if dst >= self.hand_id_start:
			dst_pos = dst - self.hand_id_start;
			if dst_pos >=self.hand_max_num:
				return;
			dst_card = self.hand_cards_arr[dst_pos]
			src_card.use(dst_card);
		elif dst >= self.card_id_start:
			dst_pos = dst - self.card_id_start;
			if dst_pos >=self.max_num:
				return;
			dst_card = self.cards_arr[dst_pos]
			src_card.use(dst_card);
		#结算血量，看游戏是否结束 todo
		#
		if self.hp <= 0:
			self.b_end = True;
			self.send_end_2c();
		return
	def req_quit(self):
		self.b_end = True;
		self.send_end_2c();
		return
	#get client request end
	###
	def enter_next(self):
		self.b_enter_next = True;
		return

	def add_hand_card(self,shape):
		count = 0;
		idx = -1;
		for i in xrange(0,len(self.hand_cards_arr)):
			c = self.hand_cards_arr[i];
			if c.shape == 0 && idx == -1:
				idx = i;
			if c.shape != 0:
				count += 1;
		if count >= self.hand_cur_max:
			print "hands is full"
			return False;
		if count >= self.hand_max_num:
			print "count >= self.hand_max_num";
			return False;
		self.hand_cards_arr[idx].re_init(shape);
		self.hand_cards_arr[idx].b_cover = False;
		return True
	def add_playerarmor(self,v):
		self.armor += v;
		return
	def sub_playerarmor(self,v):
		self.armor -= v;
		return
	def add_playerstamania(self,v):
		self.stamaina += v;
		return
	def sub_playerstamania(self,v):
		self.stamaina -= v;
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
		return
	def use_spell(self,spell_id,src_card,dst_card):
		spell_inst = get_spell_inst(spell_id);
		spell_inst.run(src_card,dst_card,self);
		return
	def del_card(self,dst):
		if dst >= self.card_id_start and dst < (self.card_id_start + self.max_num):
			del_pos = dst - self.card_id_start;
			self.cards_arr[del_pos].shape = 0;
			return
		if dst >= self.hand_id_start and dst < (self.hand_id_start + self.hand_max_num):
			del_pos = dst - self.hand_id_start;
			self.hand_cards_arr[del_pos].shape = 0;
		return
	###
	#send packet func begin
	def send_cards_2c(self):
		print "send_cards_2c";
		return
	def send_hands_2c(self):
		print "send_hands_2c";
		return
	def send_pinfo_2c(self):
		print "send_pinfo_2c %d %d %d %d %d %d"%(self.hp,self.armor,self.attack,self.exp,self.glv,self.dlv);
		return
	def send_start_2c(self):
		print "send_start_2c";
		return
	def send_end_2c(self):
		print "send_end_2c";
		return
	def send_del_card(self,dst):
		print "send_del_card %s"%(dst);
		return
	def send_card_changed(self,dst,shape,atk,hp,duration):
		print "send_card_changed %s %s %s"%(dst,shape,atk,hp,duration);
		return
	def send_close_card(self,dst):
		print "send_cover_card %s"%(dst);
		return
	def send_open_card(self,dst,card_shape):
		print "send_open_card %s,%s"%(dst,card_shape);
		return
	def send_atk_2c(self,src,dst,v):
		print "send_atk_2c %s,%s,%s"%(src,dst,v);
		return
	def send_getcard_2c(self,dst):
		print "send_getcard_2c %s"%(dst);
		return
	def send_spell_2c(self,src,dst_list,data_list):
		print "send_spell_2c %s,%s,%s"%(src,dst_list,data_list);
		return
	#send packet func end
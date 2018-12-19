#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import copy
import random
import skill

COMBAT_POS_MAP = {};
COMBAT_POS_MAP[0] = [1,2,3,4,5,6,7,8,9,10,11,12];
COMBAT_POS_MAP[1] = [20,21,22,23,24,25,26,27,28,29,30,31,32];

COMBATCMD_ATTACK = 1;
COMBATCMD_ADDWARRIOR = 2;
class combat(object):
	def __init__(self):
		super(combat,self).__init__();
		self.act_list = [];
		self.pas_list = [];
		self.fighters = {};
		self.order = [];
		self.buff_id_begin = 1;
		return
	###send s2c packet start
	def gen_s2c_combat_start(self):
		print "combat s2c start"
		return
	def gen_s2c_combat_end(self):
		print "combat s2c end"
		if self.is_side_alldead(True):
			print "challenger lose!"
		else:
			print "challenger is winner!"
		return
	def gen_s2c_turn_start(self):
		print "combat s2c turn start"
		return
	def gen_s2c_turn_end(self):
		print "combat s2c turn end"
		return
	def gen_s2c_addwarrior(self,actor):
		print "combat s2c addwarrior %s %s %s"%(actor['pos'],actor['group'],actor['hp'])
		return
	def gen_s2c_delwarrior(self,actor):
		print "combat s2c delwarrior %s %s"%(actor['pos'],actor['group'])
		return
	def gen_s2c_warrior_skillbegin(self,actor,skill_id,skill_lv,dst_list):
		print "combat s2c skillbegin %s %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv,dst_list)
		return
	def gen_s2c_warrior_skillend(self,actor,skill_id,skill_lv):
		print "combat s2c skillend %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv)
		return
	def gen_s2c_warrior_buffcd_change(self,actor,buffobj):
		print "combat s2c buffcd change %s %s %s %s %s"%(actor['pos'],actor['group'],buffobj.id,buffobj.bid,buffobj.cd)
		return
	def gen_s2c_warrior_propchg(self,old_prop,new_prop,actor,b_crack,skill_id,skill_lv):
		#todo
		#gen s2c netpacket
		print "combat s2c warrior propchg %s %s %s %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv,b_crack,old_prop,new_prop);
		print "newhp,oldhp,dead:%s %s %s"%(new_prop['hp'],old_prop['hp'],new_prop['dead'])
		return
	def gen_s2c_warrior_dodge(self,actor,skill_id,skill_lv):
		#todo
		#gen s2c netpacket
		print "combat s2c warrior dodge %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv)
		return
	def gen_s2c_warrior_addbuff(self,actor,buffobj,skill_id,skill_lv):
		#todo
		print "combat s2c warrior addbuff %s %s %s %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv,buffobj.id,buffobj.bid,buffobj.cd)
		#gen s2c netpacket
		return
	def gen_s2c_warrior_delbuff(self,actor,buffobj):
		#todo
		#gen s2c netpacket
		print "combat s2c warrior delbuff %s %s %s %s"%(actor['pos'],actor['group'],buffobj.id,buffobj.bid);
		return
	###send s2c packet end
	def gen_buff_id(self):
		self.buff_id_begin += 1;
		return self.buff_id_begin;
	def addwarrior(self,obj):
		if self.fighters.has_key(obj['id']):
			return 
		b_act = obj['group'] == 0;
		if b_act:
			self.act_list.append(obj);
		else:
			self.pas_list.append(obj);
		self.fighters[obj['pos']] = obj;
		self.gen_s2c_addwarrior(obj);
		return
	def start(self):
		self.gen_s2c_combat_start();
		return
	def end(self):
		self.gen_s2c_combat_end();
		return
	def init_order(self):
		self.order = sorted(self.fighters.keys(),reverse=True,key = lambda d:(self.fighters[d]['spd']*1000000-self.fighters[d].get('pos',0)))
		return
	def addwarriorcmd(self,id,cmd,cmd_data):
		if self.fighters.has_key(id):
			self.fighters[id]['cmd'] = cmd;
			self.fighters[id]['cmd_data'] = cmd_data;
		return
	def is_teammate(self,actor,enemy):
		return actor['group'] == enemy['group'];
	def is_warrior_dead(self,obj):
		return obj.get('dead',False)
	def is_warrior_autodel(self,obj):
		return obj.get('autodel',False)
	def is_side_alldead(self,b_act = True):
		all_dead = True;
		lst = self.act_list;
		if not b_act:
			lst = self.pas_list;
		for i in lst:
			if not self.is_warrior_dead(i):
				all_dead = False;
				break;
		return all_dead;
	def is_end(self):
		if self.is_side_alldead(True) or self.is_side_alldead(False):
			return True
		return False
	
	def calc_passive_effect(self,actor):
		#todo
		for i,j in actor['passive'].items():
			eff = j.get_effect();
			if eff and len(eff) > 0:
				restore_prop = actor.get_restoreprop();
				exec(eff);
				self.gen_s2c_warrior_propchg(restore_prop,actor.get_restoreprop(),actor,False,j.sid,j.slv);
		return
	def execute_fighter_buff(self,actor,buffobj,b_immed = False):
		if b_immed:
			if not buffobj.is_immediate():
				return
		else:
			if buffobj.is_immediate():
				return 
		eff = buffobj.get_effect();
		if eff and len(eff) > 0:
			restore_prop = actor.get_restoreprop();
			exec(eff);
			self.gen_s2c_warrior_propchg(restore_prop,actor.get_restoreprop(),actor,False,buffobj.bid,-1);
		return
	def reset_allfighter_extra_prop(self):
		for k,v in self.fighters.items():
			self.reset_fighter_extra_prop(v);
		return
	def calc_buff_extraprop(self,actor):
		for i,j in actor['buff'].items():
			self.execute_fighter_buff(actor,j,True);
		return
	def reset_fighter_extra_prop(self,actor):
		actor.reset_orgprop();
		self.calc_passive_effect(actor);
		self.calc_buff_extraprop(actor);
		return
	def execute_buff_turneffect(self):# only calc 
		#todo
		for k,v in self.fighters.items():
			actor = v;
			for i,j in actor['buff'].items():
				self.execute_fighter_buff(actor,j,False);
		return
	def process_buff_cd(self):
		for k,v in self.fighters.items():
			actor = v;
			for i,j in v['buff'].items():
				j.cd = j.cd - 1;
				if j.cd <= 0:
					self.gen_s2c_warrior_delbuff(actor,j);
					del v['buff'][i];
				else:
					self.gen_s2c_warrior_buffcd_change(actor,j);

		return
	def get_fighter(self,wid):
		return self.fighters[wid]
	def get_dst_list(self,actor,enemy,skill_obj):
		ret = [];
		if self.is_warrior_dead(enemy) and self.skill_obj.is_attacktype():
			for i in self.order:
				if self.fighters.has_key(i) == False:
					continue;
				tempplayer = self.fighters[i];
				if self.is_teammate(enemy,tempplayer) and not self.is_warrior_dead(tempplayer):
					enemy = tempplayer;
					break;
		ret.append(enemy['pos']);
		if skill_obj.max_dstcnt > 1:
			extracnt = skill_obj.max_dstcnt - 1;
			for j in self.order:
				if self.fighters.has_key(i) == False:
					continue;
				tempplayer = self.fighters[i];
				if tempplayer == enemy:
					continue;
				if not self.is_teammate(enemy,tempplayer):
					continue;
				if skill_obj.is_attacktype():
					if not self.is_warrior_dead(tempplayer):
						ret.append(tempplayer['pos']);
						extracnt -= 1;
						if extracnt <= 0:
							return ret;
				else:
					ret.append(tempplayer['pos']);
					extracnt -= 1;
					if extracnt <= 0:
						return ret;
		return ret;
	def warrior_doskill(self,actor,enemy,skill_obj,damage,revive):
		actor_prop = actor.get_restoreprop();
		enemy_prop = enemy.get_restoreprop();
		if revive != 0:
			if self.is_warrior_dead(enemy):
				enemy['dead'] = False;
		hp = enemy['hp']
		defend = enemy['def'];
		#min 0 max 10000
		basehit = 8000;
		hit = actor['hit'];
		dodge = enemy['dodge'];
		basehit = basehit + hit - dodge;
		if basehit <= 0:
			#dodge
			self.gen_s2c_warrior_dodge(enemy,skill_obj.sid,skill_obj.slv);
			return;
		if basehit < 10000:
			hitnum = random.randint(0,10000);
			if hitnum > basehit:
				self.gen_s2c_warrior_dodge(enemy,skill_obj.sid,skill_obj.slv);
				return
		if skill_obj.is_attacktype():
			damage = damage - defend;

		basecrk = 2000;
		crk = actor['crk'];
		crkdef = enemy['crkdef'];
		basecrk = basecrk + crk - crkdef;
		crknum = random.randint(0,10000);
		b_crack = False;
		if crknum <= basecrk:
			damage = damage*2;#twice damage;
			b_crack = True;
		damage = int(damage);
		if skill_obj.is_attacktype():
			hp = enemy['hp'];
			hp -= damage;
			if hp <= 0:
				enemy['hp'] = 0;
				enemy['dead'] = True;
			else:
				enemy['hp'] = hp;
		else:
			hp = enemy['hp'];
			hp += damage;
			hpmax = enemy['hpmax'];
			if hp > hpmax:
				hp = hpmax;
			enemy['hp'] = hp;
		self.gen_s2c_warrior_propchg(actor_prop,actor.get_restoreprop(),actor,False,skill_obj.sid,skill_obj.slv);
		self.gen_s2c_warrior_propchg(enemy_prop,enemy.get_restoreprop(),enemy,b_crack,skill_obj.sid,skill_obj.slv);
		b_recalc_buff_effect = False;
		for i in skill_obj.dst_buff_list:
			buffobj = i[0];
			rate = i[1];
			#
			temp = random.randint(0,10000);
			if temp <= rate:
				addbuffobj = enemy.add_buff(buffobj.bid,buffobj.cd,self.gen_buff_id());
				if addbuffobj:
					if addbuffobj.is_immediate():
						b_recalc_buff_effect = True;
					self.gen_s2c_warrior_addbuff(enemy,addbuffobj,skill_obj.sid,skill_obj.slv);

		for i in skill_obj.clr_dst_buff_list:
			buffobj = i[0];
			rate = i[1];
			#
			temp = random.randint(0,10000);
			if temp <= rate:
				delbuffobj = enemy.del_buff(buffobj.bid);
				if delbuffobj:
					if delbuffobj.is_immediate():
						b_recalc_buff_effect = True;
					self.gen_s2c_warrior_delbuff(enemy,delbuffobj);
		if b_recalc_buff_effect:
			self.reset_fighter_extra_prop(enemy);
		return
	def warrior_attack(self,obj,atk_data):
		#todo
		sid = atk_data['sid'];
		slv = atk_data['slv'];
		dst = atk_data['dst'];
		skill_obj = skill.create_skill(sid,slv);
		actor = obj;
		enemy = self.get_fighter(dst);
		dst_list = self.get_dst_list(actor,enemy,skill_obj);
		if len(dst_list) <= 0:
			return
		self.gen_s2c_warrior_skillbegin(actor,sid,slv,dst_list);
		damage = actor['atk'];
		damagerate = 1;
		revive = 0;

		eff = skill_obj.get_effect();
		exec(eff);

		for i in dst_list:
			if self.fighters.has_key(i) == False:
				continue
			enemy = self.fighters[i];
			self.warrior_doskill(actor,enemy,skill_obj,damage*damagerate,revive);
		b_recalc_buff_effect = False;
		for i in skill_obj.src_buff_list:
			buffobj = i[0];
			rate = i[1];
			#
			temp = random.randint(0,10000);
			if temp <= rate:
				addbuffobj = actor.add_buff(buffobj.bid,buffobj.cd,self.gen_buff_id());
				if addbuffobj:
					if addbuffobj.is_immediate():
						b_recalc_buff_effect = True;
					self.gen_s2c_warrior_addbuff(actor,addbuffobj,sid,slv);
		for i in skill_obj.clr_src_buff_list:
			buffobj = i[0];
			rate = i[1];
			#
			temp = random.randint(0,10000);
			if temp <= rate:
				delbuffobj = actor.del_buff(buffobj.bid);
				if delbuffobj:
					if delbuffobj.is_immediate():
						b_recalc_buff_effect = True;
					self.gen_s2c_warrior_delbuff(actor,delbuffobj);
		if b_recalc_buff_effect:
			self.reset_fighter_extra_prop(actor);
		self.gen_s2c_warrior_skillend(actor,sid,slv);
		return
	def warrior_addwarrior(self,actor,cmd_data):
		warrior_data = cmd_data;
		pos = warrior_data['pos'];
		if self.fighters.has_key(pos):
			self.delwarrior(pos);
		self.addwarrior(warrior_data);
		return
	def warrior_act(self,obj):
		cmd = obj.get('cmd',0);
		cmd_data = obj.get('cmd_data',None);
		if cmd == COMBATCMD_ATTACK:
			self.warrior_attack(obj,cmd_data);
		elif cmd == COMBATCMD_ADDWARRIOR:
			self.warrior_addwarrior(obj,cmd_data);
		obj['cmd'] = 0;
		return
	def do_allwarrior_cmd(self):
		for i in self.order:
			if self.fighters.has_key(i) == False:
				continue;
			actor = self.fighters[i];
			if self.is_warrior_dead(actor):
				continue;
			self.warrior_act(actor);
			self.check_autodel_warrior();
			if self.is_end():
				return;
		return
	def delwarrior(self,pos):
		if self.fighters.has_key(pos) == False:
			return
		delwarrior = self.fighters[pos];
		self.gen_s2c_delwarrior(delwarrior);
		del self.fighters[pos];
		for i in self.act_list:
			if i == delwarrior:
				self.act_list.remove(i);
				break;
		for i in self.pas_list:
			if i == delwarrior:
				self.pas_list.remove(i);
				break;
		return
	def check_autodel_warrior(self):
		for k,v in self.fighters.items():
			if self.is_warrior_dead(v) and self.is_warrior_autodel(v):
				self.delwarrior(k);
		return
	def on_turn_doing(self):
		return
	def on_turn(self):
		if self.is_end():
			return
		self.on_turn_doing();
		self.gen_s2c_turn_start();
		self.reset_allfighter_extra_prop();
		self.execute_buff_turneffect();
		self.check_autodel_warrior();
		self.init_order();
		if self.is_end():
			self.gen_s2c_turn_end();
			return
		self.do_allwarrior_cmd();
		self.process_buff_cd();
		self.gen_s2c_turn_end();
		return
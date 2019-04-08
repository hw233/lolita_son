#coding:utf8
'''
Created on 2018-1-26

@author: xiaomi
'''
import ctriger
import copy
import random
import skill

#（己方命中-敌方闪避）/（敌方等级*3+50）=命中概率
#（己方暴击-敌方暴抗）/（敌方等级*3+50）=暴击概率
#基础暴击伤害200%
#攻击计算
#（己方攻击+技能伤害-敌人防御）*（1 +（伤害加深百分比-伤害减少百分比）+（暴击伤害-暴击伤害减免）……）+（（无视防御-无视减免）+（伤害加深-伤害减少）……）
#时间点效果触发需要计算玩家速度，效果自身也可以自带速度和速率（后发携带了技能速率）
#所有属性，效果和buff默认自身ID用作先后顺序判断，除非自身额外增加速度或速率
#BUFF和被动技能是用来实时维护效果，BUFF，属性配置和实际数值的实体，不可将实际数值放到效果，BUFF，属性配置中
#主动技能也可以用来做为维护当前回合的效果和实际数值的实体
#进战斗时，速度乘以100+pos，方便排序
#H5进去之后当前速度*100*100%，回合则是95~105随机值
#最终结果是负数的时候回合战斗攻击方攻击*5%，H5则为1


COMBAT_POS_MAP = {};
COMBAT_POS_MAP[0] = [1,2,3,4,5,6,7,8,9,10,11,12];
COMBAT_POS_MAP[1] = [21,22,23,24,25,26,27,28,29,30,31,32];

COMBATCMD_ATTACK = 1;
COMBATCMD_SKILL = 2;
COMBATCMD_ADDWARRIOR = 3;


#status1
War_AttackedBehave_Normal = 0;
War_AttackedBehave_Hit = 1;
War_AttackedBehave_Defence = 2;
War_AttackedBehave_Dodge = 3;
#
War_AttackedBehave_BLOOD = 4;
#status2
War_AttackType_Crack = 1;
#status3
War_AttackedResult_Normal = 0;
War_AttackedResult_Dead = 1;
War_AttackedResult_FlyAway = 2;
War_AttackedResult_Revive = 4;
		
COMBAT_START_ID = 0;
class combat(object):
	def __init__(self):
		super(combat,self).__init__();
		self.act_list = [];
		self.pas_list = [];
		self.fighters = {};
		self.send_list = [];
		self.order = [];
		self.buff_id_begin = 1;
		self.parent = None;
		self.combat_id = self.gen_combat_id();
		self.combat_type = 0;
		self.combat_subtype = 0;
		self.playmode = 0;
		self.skip = 0;
		self.maxbout = 99;
		self.wait_cmd_maxtm = 30;#second
		self.wait_cmd_curtm = -1;
		self.b_is_end = False;
		self.curbout = 1;
		return
	def gen_combat_id(self):
		global COMBAT_START_ID
		COMBAT_START_ID = COMBAT_START_ID + 1;
		return COMBAT_START_ID
	
	###send s2c packet start
	def gen_s2c_combat_start(self):
		print "combat s2c start %s"%(self.parent);
		#S2C_WAR_START id type subtype lineup playmode skip maxbout
		if self.parent:
			for i in self.act_list:
				self.parent.gen_s2c_combat_start(i['cid'],self.combat_id,self.combat_type,self.combat_subtype,i['group'],self.playmode,self.skip,self.maxbout);
			for i in self.pas_list:
				self.parent.gen_s2c_combat_start(i['cid'],self.combat_id,self.combat_type,self.combat_subtype,i['group'],self.playmode,self.skip,self.maxbout);
		return
	def gen_s2c_combat_end(self):
		print "combat s2c end"
		if self.is_side_alldead(True):
			print "challenger lose!"
		else:
			print "challenger is winner!"
		#S2C_WAR_END force
		if self.parent:
			self.parent.gen_s2c_combat_end(self.send_list,0);
		return
	def gen_s2c_turn_start(self):
		print "combat s2c turn start"
		#S2C_WAR_NEXT bout
		if self.parent:
			self.parent.gen_s2c_turn_start(self.send_list,self.curbout);
		return
	def gen_s2c_turn_end(self):
		print "combat s2c turn end"
		#S2C_WAR_TURN
		if self.parent:
			self.parent.gen_s2c_turn_end(self.send_list);
		return
	def gen_s2c_addwarrior(self,actor):
		print "combat s2c addwarrior %s %s %s"%(actor['pos'],actor['group'],actor['hp'])
		#S2C_WAR_ADD warid type owner status shape desc grade classes name zoomlv
		if self.parent:
			w = actor;
			status = 0;#todo
			self.parent.gen_s2c_addwarrior(self.send_list,w['id'],0,0,status,w['shape'],'',0,0,w['name'],0);
		return
	def gen_s2c_delwarrior(self,actor):
		print "combat s2c delwarrior %s %s"%(actor['pos'],actor['group'])
		#S2C_WAR_LEAVE id
		if self.parent:
			w = actor;
			self.parent.gen_s2c_delwarrior(self.send_list,actor['id']);
		return
	def gen_s2c_warrior_skillbegin(self,actor,skill_id,skill_lv,dst_list):
		print "combat s2c skillbegin %s %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv,dst_list)
		#S2C_WAR_PERFORM att skillid lv round lsvic
		if self.parent:
			self.parent.gen_s2c_warrior_skillbegin(self.send_list,actor['id'],skill_id,skill_lv,0,dst_list);
		return
	def gen_s2c_warrior_skillend(self,actor,skill_id,skill_lv):
		print "combat s2c skillend %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv)
		#S2C_WAR_PERFORM_END
		if self.parent:
			self.parent.gen_s2c_warrior_skillend(self.send_list,actor['id']);
		#
		return
	def gen_s2c_warrior_attackbegin(self,actor,dst):
		#todo need code
		print "combat s2c attackbegin %s %s %s"%(actor['pos'],actor['group'],dst);
		#S2C_WAR_ATTACK_NORMAL att vic
		if self.parent:
			self.parent.gen_s2c_warrior_attackbegin(self.send_list,actor['id'],dst);
		return
	def gen_s2c_warrior_attackend(self,actor):
		#todo need code
		print "combat s2c attackend %s %s"%(actor['pos'],actor['group']);
		#S2C_WAR_ATTACK_END
		if self.parent:
			self.parent.gen_s2c_warrior_attackend(self.send_list,actor['id']);
		return
	def gen_s2c_warrior_buffcd_change(self,actor,buffobj):
		print "combat s2c buffcd change %s %s %s %s %s"%(actor['pos'],actor['group'],buffobj.id,buffobj.bid,buffobj.cd)
		return
	def gen_s2c_warrior_propchg(self,old_prop,new_prop,damage,actor,b_crack,skill_id,skill_lv,b_skill = False):
		#gen s2c netpacket
		print "combat s2c warrior propchg %s %s %s %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv,b_crack,old_prop,new_prop);
		print "newhp,oldhp,dead:%s %s %s"%(new_prop['hp'],old_prop['hp'],new_prop['dead'])
		if not b_skill and damage == 0:
			return;
		global War_AttackedBehave_Normal
		global War_AttackedBehave_Hit
		global War_AttackedBehave_Defence
		global War_AttackedBehave_Dodge
		global War_AttackedBehave_BLOOD
		global War_AttackType_Crack
		global War_AttackedResult_Normal
		global War_AttackedResult_Dead
		global War_AttackedResult_FlyAway
		global War_AttackedResult_Revive
		status = 0;
		if b_crack:
			status = status | (War_AttackType_Crack << 2);
		if old_prop and new_prop:
			if new_prop['kickout'] == True:
				if not old_prop['kickout']:
					status = status | (War_AttackedResult_FlyAway << 4);
			elif new_prop['dead'] == True:
				if not old_prop['dead']:
					status = status | (War_AttackedResult_Dead << 4);
			else:
				if old_prop['dead'] == True and not new_prop['dead']:
					status = status | (War_AttackedResult_Revive << 4);

		status = status | War_AttackedBehave_Hit;
		if self.parent:#todo
			self.parent.gen_s2c_warrior_propchg(self.send_list,actor['id'],status,damage);
		return
	def gen_s2c_warrior_dodge(self,actor,skill_id,skill_lv):
		#gen s2c netpacket
		#todo need code
		global War_AttackedBehave_Dodge
		status = 0;
		status = status | War_AttackedBehave_Dodge;
		print "combat s2c warrior dodge %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv)
		if self.parent:#todo
			self.parent.gen_s2c_warrior_propchg(self.send_list,actor['id'],status,0);
		return
	def gen_s2c_warrior_addbuff(self,actor,buffobj,skill_id,skill_lv):
		print "combat s2c warrior addbuff %s %s %s %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv,buffobj.id,buffobj.bid,buffobj.cd)
		#gen s2c netpacket
		#S2C_WAR_BUFF_ADD warid bid overlay bout datas
		if self.parent:
			self.parent.gen_s2c_warrior_addbuff(self.send_list,actor['id'],buffobj.bid,buffobj.count,buffobj.cd,[]);
		return
	def gen_s2c_warrior_delbuff(self,actor,bid):
		#gen s2c netpacket
		print "combat s2c warrior delbuff %s %s %s"%(actor['pos'],actor['group'],bid);
		#S2C_WAR_BUFF_DEL warid bid
		if self.parent:
			self.parent.gen_s2c_warrior_delbuff(self.send_list,actor['id'],bid);
		return
	def gen_s2c_warrior_status(self,actor):
		#todo need code
		print "combat s2c warrior status %s %s %s %s"%(actor['pos'],actor['group'], actor['hp'],actor['hpmax']);
		#S2C_WAR_STATUS id hprate
		if self.parent:
			self.parent.gen_s2c_warrior_status(self.send_list,actor['id'],actor['hp']*1000/actor['hpmax']);
		return
	def gen_s2c_warrior_partnerattack(self,actor,vic):
		#todo need code
		print "combat s2c warrior partnerattack %s %s %s"%(actor['pos'],actor['group'],vic);
		#S2C_WAR_PARTNER_ATTACK partner vic
		if self.parent:
			self.parent.gen_s2c_warrior_partnerattack(self.send_list,actor['id'],vic);
		return
	def gen_s2c_warrior_backattackbegin(self,actor,skill_id,skill_lv,dst_list):
		print "combat s2c backattackbegin %s %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv,dst_list)
		#S2C_WAR_BACKATTACK att skillid lv round lsvic
		if self.parent:
			self.parent.gen_s2c_warrior_backattackbegin(self.send_list,actor['id'],skill_id,skill_lv,0,dst_list);
		return
	def gen_s2c_warrior_backattackend(self,actor,skill_id,skill_lv):
		print "combat s2c backattackend %s %s %s %s"%(actor['pos'],actor['group'],skill_id,skill_lv)
		#S2C_WAR_BACKATTACK_END
		if self.parent:
			self.parend.gen_s2c_warrior_backattackend(self.send_list,actor['id']);
		return
	def gen_s2c_warrior_shake(self,actor,vic):
		#todo need code
		print "combat s2c warrior shake %s %s %s"%(actor['pos'],actor['group'],vic);
		#S2C_WAR_SHAKE att vic
		if self.parent:
			self.parent.gen_s2c_warrior_shake(self.send_list,actor['id'],vic);
		return
	def gen_s2c_warrior_protect(self,actor,vic):
		#todo need code
		print "combat s2c warrior protect %s %s %s"%(actor['pos'],actor['group'],vic);
		#S2C_WAR_PROTECT protector vic
		if self.parent:
			self.parent.gen_s2c_warrior_protect(self.send_list,actor['id'],vic);
		return
	###send s2c packet end
	def get_default_dst(self,actor):
		group = actor['group'];
		pos_map = None;
		global COMBAT_POS_MAP
		if group == 0:
			pos_map = COMBAT_POS_MAP[1];
		else:
			pos_map = COMBAT_POS_MAP[0];
		for i in pos_map:
			if self.fighters.has_key(i) and (not self.is_warrior_dead(self.fighters[i])):
				return i;
		return None;
	def addwarrior(self,obj):
		if self.fighters.has_key(obj['id']):
			return 
		b_act = obj['group'] == 0;
		if b_act:
			self.act_list.append(obj);
		else:
			self.pas_list.append(obj);
		if obj['cid'] not in self.send_list and obj['cid'] != 0:
			self.send_list.append(obj['cid']);

		self.fighters[obj['pos']] = obj;
		
		return
	def start(self):
		self.gen_s2c_combat_start();
		for i in self.act_list:
			self.gen_s2c_addwarrior(i);
			self.gen_s2c_warrior_status(i);
		for i in self.pas_list:
			self.gen_s2c_addwarrior(i);
			self.gen_s2c_warrior_status(i);
		self.on_start_state()#处理战斗开始时间点的效果
		return
	def end(self):
		self.gen_s2c_combat_end();
		return
	def _get_warrior_curbout_spd(self,v):
		return self._calc_warrior_spd_byskill(v,self._get_warrior_curbout_skill(v));
	def _calc_warrior_spd_byskill(self,v,skill_obj):
		if not skill_obj:
			return v['spd']
		return v['spd']*skill_obj.spd/100;
	def init_order(self):
		self.order = sorted(self.fighters.keys(),reverse=True,key = lambda d:(self._get_warrior_curbout_spd(self.fighters[d])*1000000-self.fighters[d].get('pos',0)))
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
	def is_warrior_kickout(self,obj):
		return obj.get('kickout',False)
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
	def check_end(self):
		if self.is_side_alldead(True) or self.is_side_alldead(False):
			return True
		return False
	def is_end(self):
		return self.b_is_end;
	
	def process_buff_cd(self):
		for k,v in self.fighters.items():
			actor = v;
			for i,j in v['buff'].items():
				j.cd = j.cd - 1;
				if j.cd <= 0:
					self.gen_s2c_warrior_delbuff(actor,i);
				else:
					self.gen_s2c_warrior_buffcd_change(actor,j);
			keys = list(v['buff'].keys());
			for i in keys:
				if v['buff'][i].cd <= 0:
					v['buff'][i].clear(v,self);
					del v['buff'][i];
		return
	def get_fighter(self,wid):
		return self.fighters[wid]
	def _is_dst_valid(self,actor,enemy,skill_obj):
		if skill_obj.dst_enemymonster and enemy.is_summon():
			return True;
		if skill_obj.dst_summon and enemy.is_summon() and self.is_teammate(actor,enemy):
			return True;

		if skill_obj.dst_self != 0 and enemy == actor:
			return True;
		if skill_obj.selfpet != 0 and enemy.is_pet() and enemy.get_owner() == actor.get_cid():
			return True;
		if skill_obj.dst_selffri != 0 and enemy.is_character() and self.is_teammate(actor,enemy):
			return True;
		if skill_obj.dst_selffripet != 0 and enemy.is_pet() and self.is_teammate(actor,enemy):
			return True;

		if skill_obj.dst_enemy != 0 and enemy.is_character() and not self.is_teammate(actor,enemy):
			return True;
		if skill_obj.dst_enemypet != 0 and enemy.is_pet() and not self.is_teammate(actor,enemy):
			return True;
		return False;


	def get_dst_list(self,actor,enemy,skill_obj):
		ret = [];
		max_cnt = skill_obj.max_dstcnt;
		if self.skill_obj.is_canrevive():
			if self.is_warrior_dead(enemy) and self._is_dst_valid(actor,enemy,skill_obj):
				ret.append(enemy['pos']);
				max_cnt -= 1;
			for i in self.order:
				if max_cnt <= 0:
					break;
				if self.fighters.has_key(i) == False:
					continue;
				if i == enemy['pos']:
					continue;
				tempplayer = self.fighters[i];
				if self.is_warrior_dead(tempplayer) and self._is_dst_valid(actor,tempplayer,skill_obj):
					ret.append(i);
					max_cnt -= 1;
			return ret;
		if not self.is_warrior_dead(enemy) and self._is_dst_valid(actor,enemy,skill_obj):
			ret.append(enemy['pos']);
			max_cnt -= 1;
		for i in self.order:
			if max_cnt <= 0:
				break;
			if self.fighters.has_key(i) == False:
				continue;
			if i == enemy['pos']:
				continue;
			tempplayer = self.fighters[i];
			if not self.is_warrior_dead(tempplayer) and self._is_dst_valid(actor,tempplayer,skill_obj):
				ret.append(i);
				max_cnt -= 1;
		return ret;
	def _calc_attack_damage(self,actor,enemy,b_crack,atkadd = 0,atkaddrate = 1.0,b_attack = True):
		satk = actor['atk'];
		satk = (satk + atkadd)*atkaddrate;

		edef = enemy['def'];
		dmgaddrate = actor['dmgrate'];
		dmgdefrate = enemy['dmgdefrate'];
		if b_crack:
			dmgaddrate = dmgaddrate + actor['crkdmgrate'];
			dmgdefrate = dmgdefrate + enemy['crkdmgdefrate'];

		absdmg = actor['absdmg'];
		absdmgdef = enemy['absdmgdef'];
		ignoredef = actor['ignoredef'];
		ignoredefdef = enemy['ignoredefdef'];

		absdmg = absdmg - absdmgdef +  ignoredef - ignoredefdef;

		if dmgaddrate < dmgdefrate:
			dmgaddrate = 0;
		else:
			dmgaddrate = dmgaddrate - dmgdefrate;
		damage = 0;
		if not b_attack:
			edef = 0;
			absdmg = 0;
		damage = (satk - edef)*(100 + dmgaddrate)/100 + absdmg;
		if damage <= 0:
			damage = 1;
		damage = int(damage);
		return damage;
	def warrior_attack(self,obj,dst):
		#todo
		actor = obj;
		enemy = self.get_fighter(dst);
		if enemy == None:
			dst = self.get_default_dst(obj);
			enemy = self.get_fighter(dst);
		if enemy == None:
			return
		actor_prop = actor.get_restoreprop();
		enemy_prop = enemy.get_restoreprop();
		sid = 1;
		slv = 1;
		self.gen_s2c_warrior_skillbegin(actor,sid,slv,[dst]);
		self.on_attack_start(actor,[dst]);
		shit = actor['hit'];
		edodge = enemy['dodge'];
		hitrate = (shit - edodge)/(enemy['lv']*3+50)*1000;
		if hitrate < random.randint(0,1000):
			self.on_attack_miss(actor,dst);
			self.gen_s2c_warrior_dodge(enemy,sid,slv);
			self.on_attack_end(actor,dst);
			self.gen_s2c_warrior_skillend(actor,sid,slv);
			return
		self.on_attack_hit(actor,dst);
		self.on_attack_hurt(actor,dst);
		scrk = actor['crk'];
		ecrkdef = enemy['crkdef'];
		crkrate = (scrk - ecrkdef)/(enemy['lv']*3+50)*1000;
		b_crack = False;
		if crkrate >= random.randint(0,1000):
			b_crack = True;
		damage = self._calc_attack_damage(actor,enemy,b_crack);
		hp = enemy['hp'];
		hp -= damage;
		value = damage;
		if hp <= 0:
			enemy['hp'] = 0;
			if enemy['cankickout']:
				enemy['kickout'] = True;
				self.on_attack_flyout(actor,dst);
			else:
				enemy['dead'] = True;
				self.on_attack_dead(actor,dst);
		else:
			enemy['hp'] = hp;
		self.gen_s2c_warrior_propchg(enemy_prop,enemy.get_restoreprop(),value,enemy,b_crack,sid,slv,False);
		self.gen_s2c_warrior_status(enemy);
		self.on_attack_end(actor,[dst]);
		self.gen_s2c_warrior_skillend(actor,sid,slv);
		if enemy['kickout']:
			self.delwarrior(dst);
		if actor['kickout']:
			self.delwarrior(actor['pos']);
		return
	def warrior_skill(self,obj,sid,dst):
		#todo
		skill_obj = obj.get_skill(sid);
		if skill_obj == None:
			return;
		actor = obj;
		enemy = self.get_fighter(dst);
		if enemy == None:
			dst = self.get_default_dst(actor);
			enemy = self.get_fighter(dst);

		dst_list = self.get_dst_list(actor,enemy,skill_obj);
		if len(dst_list) <= 0:
			return
		self.gen_s2c_warrior_skillbegin(actor,sid,slv,dst_list);
		self.on_attack_start(actor,dst_list,skill_obj);
		atkadd = skill_obj.damage;
		atkrate = 1.0;
		if skill_obj.damage_rate != 0:
			atkrate = skill_obj.damage_rate/100;

		skillhit = skill_obj.hit;

		for i in dst_list:
			enemy = self.get_fighter(i);
			if not enemy:
				continue;
			actor_prop = actor.get_restoreprop();
			enemy_prop = enemy.get_restoreprop();
			if skill_obj.is_candodge():
				shit = skillhit;#actor['hit'];
				edodge = enemy['dodge'];
				hitrate = (shit - edodge)/(enemy['lv']*3+50)*1000;
				if hitrate < random.randint(0,1000):
					self.on_attack_miss(actor,i,skill_obj);
					self.gen_s2c_warrior_dodge(enemy,sid,slv);
					continue;
			self.on_attack_hit(actor,i,skill_obj);
			self.on_attack_hurt(actor,i,skill_obj);
			scrk = actor['crk'];
			ecrkdef = enemy['crkdef'];
			crkrate = (scrk - ecrkdef)/(enemy['lv']*3+50)*1000;
			b_crack = False;
			if crkrate >= random.randint(0,1000):
				b_crack = True;
			damage = self._calc_attack_damage(actor,enemy,b_crack,atkadd,atkrate,skill_obj.is_attacktype());
			if skill_obj.is_attacktype():
				hp = enemy['hp'];
				hp -= damage;
				value = damage;
				if hp <= 0:
					enemy['hp'] = 0;
					if enemy['cankickout']:
						enemy['kickout'] = True;
						self.on_attack_flyout(actor,i,skill_obj);
					else:
						enemy['dead'] = True;
						self.on_attack_dead(actor,i,skill_obj);
				else:
					enemy['hp'] = hp;
			else:
				hp = enemy['hp'];
				hp += damage;
				value = 0-damage;
				hpmax = enemy['hpmax'];
				if hp > hpmax:
					hp = hpmax;
				enemy['hp'] = hp;
			self.gen_s2c_warrior_propchg(enemy_prop,enemy.get_restoreprop(),value,enemy,b_crack,sid,slv,True);
			self.gen_s2c_warrior_status(enemy);
		self.on_attack_end(actor,dst_list,skill_obj)
		
		self.gen_s2c_warrior_skillend(actor,sid,slv);
		for i in dst_list:
			enemy = self.fighters[i];
			if enemy['kickout']:
				self.delwarrior(i);
		if actor['kickout']:
			self.delwarrior(actor['pos']);
		return
	def warrior_addwarrior(self,actor,cmd_data):
		warrior_data = cmd_data;
		pos = warrior_data['pos'];
		if self.fighters.has_key(pos):
			self.delwarrior(pos);
		self.addwarrior(warrior_data);
		return
	def warrior_act(self,obj):
		cmd = obj.get('cmd',COMBATCMD_ATTACK);
		cmd_data = obj.get('cmd_data',None);
		if cmd == COMBATCMD_SKILL:
			dst = None;
			if cmd_data == None:
				dst = self.get_default_dst(obj);
				self.warrior_attack(obj,dst);
			else:
				sid = cmd_data["sid"];
				dst = cmd_data["dst"];
				self.warrior_skill(obj,sid,dst);
		elif cmd == COMBATCMD_ADDWARRIOR:
			self.warrior_addwarrior(obj,cmd_data);
		else:
			dst = None;
			if cmd_data == None:
				dst = self.get_default_dst(obj);
			else:
				dst = cmd_data["dst"];
			self.warrior_attack(obj,dst);
		obj['cmd'] = COMBATCMD_ATTACK;
		return
	def _get_warrior_curbout_skill(self,obj):
		cmd = obj.get('cmd',COMBATCMD_ATTACK);
		if cmd != COMBATCMD_SKILL:
			return
		cmd_data = obj.get('cmd_data',None);
		if cmd_data == None:
			return
		sid = cmd_data['sid'];
		slv = cmd_data['slv'];
		return obj.get_skill(sid);
	def _get_warrior_curbout_dst(self,obj):
		cmd = obj.get('cmd',COMBATCMD_ATTACK);
		cmd_data = obj.get('cmd_data',None);
		if cmd_data == None:
			return self.get_default_dst(obj)
		return cmd_data['dst'];
	def do_allwarrior_cmd(self):
		for i in self.order:
			if self.fighters.has_key(i) == False:
				continue;
			actor = self.fighters[i];
			if self.is_warrior_dead(actor):
				continue;
			self.warrior_act(actor);
			if self.check_end():
				return;
		return
	def delwarrior(self,pos):
		if self.fighters.has_key(pos) == False:
			return
		delw = self.fighters[pos];
		self.gen_s2c_delwarrior(delw);
		del self.fighters[pos];
		for i in self.act_list:
			if i == delw:
				self.act_list.remove(i);
				break;
		for i in self.pas_list:
			if i == delw:
				self.pas_list.remove(i);
				break;
		return
	
	def tick_1s(self):
		if self.wait_cmd_curtm >= 0:
			self.wait_cmd_curtm -= 1;
			if self.wait_cmd_curtm < 0:
				self.on_turn();
		return
	def on_turn_doing(self):
		return
	def on_turn(self):
		if self.check_end():
			if not self.b_is_end:
				self.b_is_end = True;
				self.end();
			return
		self.on_turn_doing();#处理各单位指令相关
		self.gen_s2c_turn_start();
		self.on_turn_start();#处理回合开始时间点效果
		if self.check_end():
			self.gen_s2c_turn_end();
			self.b_is_end = True;
			self.end();
			return
		self.init_order();
		self.do_allwarrior_cmd();
		
		self.on_turn_end();#处理回合结束时间点效果
		self.process_buff_cd();
		self.gen_s2c_turn_end();
		if self.check_end():
			self.b_is_end = True;
			self.end();
			return
		self.curbout = self.curbout + 1;
		return
	################
	def _get_warrior_alleffect(self,tm,actor,dst_list,skill_obj):
		############
		wrapper_list = [];
		enemy_list = [];
		for i in dst_list:
			enemy = self.get_fighter(i);
			if enemy:
				enemy_list.append(enemy);
		actor_spd = actor['spd'];
		if skill_obj:
			actor_spd = self._calc_warrior_spd_byskill(actor,skill_obj);
			cur_wrapper_list = skill_obj.get_wrapperlist_bystate(tm);
			for i in cur_wrapper_list:
				i.gen_spd(actor_spd);
				i.set_actor(actor);
				i.set_enemy_list(enemy_list);
				wrapper_list.append(i);
		for m,n in actor['passive'].items():
			cur_wrapper_list = n.get_wrapperlist_bystate(tm);
			for i in cur_wrapper_list:
				i.gen_spd(actor_spd);
				i.set_actor(actor);
				i.set_enemy_list(enemy_list);
				wrapper_list.append(i);
		return wrapper_list
	#战斗开始时间点，触发和计算所有玩家身上的组合BUFF和被动技能上的效果，属性等
	def on_start_state(self,tm = ctriger.COMBAT_TRIGER_ENTER):
		#玩家身上的被动技能和当前使用主动技能上的效果，属性
		wrapper_list = [];
		for k,v in self.fighters.items():
			cur_skill = self._get_warrior_curbout_skill(v);
			dst = self._get_warrior_curbout_dst(v);
			dst_list = [];
			if dst != None:
				dst_list.append(dst);
			if cur_skill:
				enemy = self.get_fighter(dst);
				if enemy == None:
					dst = self.get_default_dst(v);
					enemy = self.get_fighter(dst);
				dst_list = self.get_dst_list(v,enemy,cur_skill);
			sub_wrapper_list = self._get_warrior_alleffect(tm,v,dst_list,cur_skill);
			for i in sub_wrapper_list:
				wrapper_list.append(i);
		wrapper_list = sorted(wrapper_list, key=lambda x:x.spd);
		for i in wrapper_list:
			i.do();
		return
	#回合开始时间点,计算所有玩家
	def on_turn_start(self):
		self.on_start_state(ctriger.COMBAT_TRIGER_TURNSTART)
		#再是玩家身上的组合BUFF和BUFF计算
		for k,v in self.fighters.items():
			for bid,buff_ins in v["buff"].items():
				buff_ins.do(v,self);
		return
	
	#攻击开始时间点,针对单人出手,计算攻击发起者和所有受击者
	def on_attack_start(self,actor,dst_list,skill_obj = None,tm = ctriger.COMBAT_TRIGER_SKILLSTART):
		wrapper_list = [];
		wrapper_list = self._get_warrior_alleffect(tm,actor,dst_list,skill_obj);
		for i in dst_list:
			enemy = self.get_fighter(i);
			if enemy:
				cur_skill = self._get_warrior_curbout_skill(enemy);
				dst = self._get_warrior_curbout_dst(enemy);
				dst_list = [];
				if dst != None:
					dst_list.append(dst);
				if cur_skill:
					eenemy = self.get_fighter(dst);
					if eenemy == None:
						dst = self.get_default_dst(enemy);
						eenemy = self.get_fighter(dst);
					dst_list = self.get_dst_list(enemy,eenemy,cur_skill);
				sub_wrapper_list = self._get_warrior_alleffect(tm,enemy,dst_list,cur_skill);
				for i in sub_wrapper_list:
					wrapper_list.append(i);
		wrapper_list = sorted(wrapper_list, key=lambda x:x.spd);
		for i in wrapper_list:
			i.do();
		return
	#伤害开始时间点，针对单人出手，计算攻击发起者和当前受击者，用在吸血和反击？
	def on_attack_hurt(self,actor,dst,skill_obj = None,b_onlydst = False,tm = ctriger.COMBAT_TRIGER_ATK):
		wrapper_list = [];
		dst_list = [dst];
		if not b_onlydst:
			wrapper_list = self._get_warrior_alleffect(tm,actor,dst_list,skill_obj);
		############
		if dst != 0:
			enemy = self.get_fighter(dst);
			cur_skill = self._get_warrior_curbout_skill(enemy);
			edst = self._get_warrior_curbout_dst(enemy);
			dst_list = [];
			if edst != None:
				dst_list.append(edst);
			if cur_skill:
				eenemy = self.get_fighter(edst);
				if eenemy == None:
					edst = self.get_default_dst(eenemy);
					eenemy = self.get_fighter(edst);
				dst_list = self.get_dst_list(enemy,eenemy,cur_skill);
			sub_wrapper_list = self._get_warrior_alleffect(tm,enemy,dst_list,cur_skill);
			for i in sub_wrapper_list:
				wrapper_list.append(i);
		wrapper_list = sorted(wrapper_list, key=lambda x:x.spd);
		for i in wrapper_list:
			i.do();
		############
		return
	#攻击命中时，主要用在封印？
	def on_attack_hit(self,actor,dst,skill_obj = None,b_onlydst = False):
		self.on_attack_hurt(actor,dst,skill_obj,b_onlydst,ctriger.COMBAT_TRIGER_HIT);
		return

	#伤害被miss时,主要是闪避和封印未命中？
	def on_attack_miss(self,actor,dst,skill_obj = None,b_onlydst = False):
		self.on_attack_hurt(actor,dst,skill_obj,b_onlydst,ctriger.COMBAT_TRIGER_MISS);
		return
	#击倒时
	def on_attack_dead(self,actor,dst,skill_obj = None,b_onlydst = False):
		self.on_attack_hurt(actor,dst,skill_obj,b_onlydst,ctriger.COMBAT_TRIGER_DEAD);
		return
	#击飞出场时
	def on_attack_flyout(self,actor,dst,skill_obj = None,b_onlydst = False):
		self.on_attack_hurt(actor,dst,skill_obj,b_onlydst,ctriger.COMBAT_TRIGER_FLYOUT);
		return
	#攻击结束时间点，针对单人出手，计算攻击发起者和所有受击者
	def on_attack_end(self,actor,dst_list,skill_obj = None):
		self.on_attack_start(actor,dst_list,skill_obj,ctriger.COMBAT_TRIGER_SKILLEND);
		return
	#回合结束时间点，计算所有玩家
	def on_turn_end(self):
		self.on_start_state(ctriger.COMBAT_TRIGER_TURNEND)
		return
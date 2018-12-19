#coding:utf8
'''
Created on 2018-1-30

@author: xiaomi
'''

import combat
class autocombat(combat.combat):
    def __init__(self):
        super(autocombat,self).__init__();
        return
    def get_autoskill_dst(self,actor):
        group = actor['group'];
        pos_map = None;
        if group == 0:
            pos_map = combat.COMBAT_POS_MAP[1];
        else:
            pos_map = combat.COMBAT_POS_MAP[0];
        for i in pos_map:
            if self.fighters.has_key(i) and (not self.is_warrior_dead(self.fighters[i])):
                return i;
        return None;
    def on_turn_doing(self):
        for k,v in self.fighters.items():
            if self.is_warrior_dead(v):
                continue;
            dst = self.get_autoskill_dst(v);
            if dst == None:
                continue;
            skill_id = 1001;
            skill_lv = 1;
            skill_list = v['skill'].keys();
            if len(skill_list) > 0:
                last_id = v.get('lastskill',None);
                if last_id == None:
                    skill_id = skill_list[0];
                    skill_lv = v['skill'][skill_id].slv;
                else:
                    idx = 0;
                    for i in skill_list:
                        if i == last_id:
                            break;
                        idx += 1;
                    if idx >= (len(skill_list) - 1):
                        idx = 0;
                    else:
                        idx = idx + 1;
                    skill_id = skill_list[idx];
                    skill_lv = v['skill'][skill_id].slv;
            self.addwarriorcmd(k,combat.COMBATCMD_ATTACK,{'sid':skill_id,'slv':skill_lv,'dst':dst})
        return
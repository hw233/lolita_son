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
        return self.get_default_dst(actor);
    def on_turn_doing(self):
        for k,v in self.fighters.items():
            dst = self.get_autoskill_dst(v);
            if dst == None:
                continue;
            skill_id = 1;
            skill_lv = 1;
            last_id = v.get('lastskill',None);
            for k,v in v['skill'].items():
                if last_id == None:
                    skill_id = k;
                    skill_lv = v.slv;
                else:
                    if last_id == k:
                        skill_lv = v.slv;
            if skill_id == 1:
                self.addwarriorcmd(k,combat.COMBATCMD_ATTACK,{'sid':skill_id,'slv':skill_lv,'dst':dst})
            else:
                self.addwarriorcmd(k,combat.COMBATCMD_SKILL,{'sid':skill_id,'slv':skill_lv,'dst':dst})
        return
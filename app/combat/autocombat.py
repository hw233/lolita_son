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
            cur_skill = v.get_cur_skill(True);
            if cur_skill != None:
                skill_id = cur_skill.sid;
                skill_lv = cur_skill.slv;
            else:
                for k,v in v['skill'].items():
                    skill_id = k;
                    skill_lv = v.slv;
                    break;
            if skill_id == 1:
                self.addwarriorcmd(k,combat.COMBATCMD_ATTACK,{'sid':skill_id,'slv':skill_lv,'dst':dst})
            else:
                self.addwarriorcmd(k,combat.COMBATCMD_SKILL,{'sid':skill_id,'slv':skill_lv,'dst':dst})
        return
#coding:utf8
'''
Created on 2018-1-29

@author: xiaomi
'''
import ctriger
import cproperty
import ceffect
import cwrapper

import app.config.simpleskillpassive as skillpassiveconfig
import app.config.fightskillpassive as fightskillpassive
class skillpassive(object):
    def __init__(self,sid,slv):
        self.sid = sid;
        self.slv = slv;
        self.effect = "";
        self.groupid = 0;
        self.init();
        return
    def get_wrapperlist_bystate(self,state):
        return [];
    def init(self):
        skilldata = skillpassiveconfig.create_Simpleskillpassive(self.sid);
        for i in skilldata.skilldata:
            if i['lv'] == self.slv:
                self.effect = i['effect'];
                self.groupid = i['group'];
                return;
        return
    def get_effect(self):
        return self.effect;

class boutskillpassive(object):
    def __init__(self,sid,slv):
        self.sid = sid;
        self.slv = slv;
        self.effect = "";
        self.groupid = 0;
        self.name = "";
        self.tp = "";
        self.cryout = 0;
        self.prop_list = [];#[prop,triger,rate,dst,value]
        self.eff_list = [];#[prop,triger,rate,dst,value]

        self.wrapper_map = {};
        self.init();
        return
    def add_wrapper(self,wrapper):
        state = wrapper.get_triger_state();
        if not self.wrapper_map.has_key(state):
            self.wrapper_map[state] = [];
        self.wrapper_map[state].append(wrapper);
        return
    def get_wrapperlist_bystate(self,state):
        if self.wrapper_map.has_key(state):
            return self.wrapper_map[state];
        return [];
    def init(self):
        skilldata = fightskillpassive.create_Fightskillpassive(self.sid);
        if skilldata == None:
            return
        self.name = skilldata.name;
        self.tp = skilldata.type;
        self.cryout = skilldata.cryout;
        for i in skilldata.data:
            if i.get('lv',0) == self.slv:
                propdata = i.get("propdata",[]);
                self.prop_list = [];#[prop,triger,rate,dst,value]
                self.eff_list = [];#[prop,triger,rate,dst,value]
                for k in propdata:
                    prop = k["prop"];
                    ptriger = ctriger.COMBAT_TRIGER_ENTER;
                    prate = 0;
                    pdst = 0;
                    pvalue = k["pvalue"];
                    if prop != "无":
                        pins = None;
                        if not pins and ceffect.have_effect_by_name(prop):
                            pins = ceffect.get_effect_by_name(prop);
                        if not pins and cproperty.have_cprop_by_name(prop):
                            pins = cproperty.get_cprop_by_name(prop);
                        wrapper_ins = cwrapper.combatwrapper(pins,pvalue,prate,pdst,ctriger.get_triger_by_id(ptriger));
                        self.prop_list.append(wrapper_ins);
                        self.add_wrapper(wrapper_ins);
                    effdata = k["effdata"];
                    for j in effdata:
                        prop = j["efftype"];
                        ptriger = j["efftime"];
                        prate = j["effrate"];
                        pdst = j["effdst"];
                        pvalue = j["effvalue"];
                        if prop != "无":
                            pins = None;
                            if not pins and ceffect.have_effect_by_name(prop):
                                pins = ceffect.get_effect_by_name(prop);
                            if not pins and cproperty.have_cprop_by_name(prop):
                                pins = cproperty.get_cprop_by_name(prop);
                            wrapper_ins = cwrapper.combatwrapper(pins,pvalue,prate,pdst,ctriger.get_triger_by_name(ptriger));
                            self.eff_list.append(wrapper_ins);
                            self.add_wrapper(wrapper_ins);

        return
    def get_effect(self):
        return self.effect;

g_skillpassive_config = {};
def create_passiveskill(sid,slv):
    global g_skillpassive_config
    key = sid*1000+slv;
    if g_skillpassive_config.has_key(key) == False:
        g_skillpassive_config[key] = skillpassive(sid,slv);
    return g_skillpassive_config[key];

def has_skill(sid):
    skilldata = fightskillpassive.create_Fightskillpassive(sid);
    if skilldata == None:
        return False
    return True
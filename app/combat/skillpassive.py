#coding:utf8
'''
Created on 2018-1-29

@author: xiaomi
'''
import ctriger
import cproperty
import cbuff
import ceffect

import app.config.simpleskillpassive as skillpassiveconfig
import app.config.fightskillpassive
class skillpassive(object):
    def __init__(self,sid,slv):
        self.sid = sid;
        self.slv = slv;
        self.effect = "";
        self.groupid = 0;
        self.init();
        return
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
        self.init();
        return
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
                    ptriger = k["ptime"];
                    prate = k["prate"];
                    pdst = 0;
                    pvalue = k["pvalue"];
                    if prop != "无":
                        pins = None;
                        if not pins and cbuff.have_cbuffeff_by_name(prop):
                            pins = cbuff.get_cbuffeff_by_name(prop);
                        if not pins and ceffect.have_effect_by_name(prop):
                            pins = ceffect.get_effect_by_name(prop);
                        if not pins and cproperty.have_cprop_by_name(prop):
                            pins = cproperty.get_cprop_by_name(prop);
                        self.prop_list.append([pins,ctriger.get_triger_by_name(ptriger),prate,pdst,pvalue]);
                    effdata = k["effdata"];
                    for j in effdata:
                        prop = j["efftype"];
                        ptriger = j["efftime"];
                        prate = j["effrate"];
                        pdst = j["effdst"];
                        pvalue = j["effvalue"];
                        if prop != "无":
                            pins = None;
                            if not pins and cbuff.have_cbuffeff_by_name(prop):
                                pins = cbuff.get_cbuffeff_by_name(prop);
                            if not pins and ceffect.have_effect_by_name(prop):
                                pins = ceffect.get_effect_by_name(prop);
                            if not pins and cproperty.have_cprop_by_name(prop):
                                pins = cproperty.get_cprop_by_name(prop);
                            self.eff_list.append([pins,ctriger.get_triger_by_name(ptriger),prate,pdst,pvalue]);

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
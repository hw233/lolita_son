#coding:utf8
'''
Created on 2018-1-29

@author: xiaomi
'''
import app.config.skillpassive as skillpassiveconfig
class skillpassive(object):
    def __init__(self,sid,slv):
        self.sid = sid;
        self.slv = slv;
        self.effect = "";
        self.groupid = 0;
        self.init();
        return
    def init(self):
        skilldata = skillpassiveconfig.create_Skillpassive(self.sid);
        for i in skilldata.skilldata:
            if i['lv'] == self.slv:
                self.effect = i['effect'];
                self.groupid = i['group'];
                return;
        return
    def get_effect(self):
        return self.effect;
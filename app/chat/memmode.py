#-*-coding:utf8-*-
'''
Created on 2013-6-5

@author: lan
'''
from firefly.dbentrust.mmode import MAdmin

tb_character_admin = MAdmin('tb_character','id',incrkey='id')
tb_character_admin.insert()
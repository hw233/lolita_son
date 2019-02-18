#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
import memmode
from firefly.dbentrust.madminanager import MAdminManager

def load_config_data():
    """从数据库中读取配置信息
    """

    
def registe_madmin():
    """注册数据库与memcached对应
    """
    MAdminManager().registe( memmode.tb_character_admin)
    MAdminManager().registe( memmode.tb_item_admin)
    MAdminManager().registe( memmode.tb_itemopen_admin)
    
    
    
    
    
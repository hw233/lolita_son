#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from firefly.server.globalobject import GlobalObject,remoteserviceHandle
from twisted.python import log

@remoteserviceHandle('gate')
def pushObject(topicID,msg,sendList):
    GlobalObject().netfactory.pushObject(topicID, msg, sendList)

@remoteserviceHandle('gate')
def pushObjectOthers(topicID,msg,exclude_list):
    lis = GlobalObject().netfactory.connmanager._connections.keys()     #获取所有在线用户
    for i in exclude_list:
        if i in lis:
            lis.remove(i) 
    GlobalObject().netfactory.pushObject(topicID, msg, lis);


@remoteserviceHandle('gate')
def loseConnect(id):
    log.msg("net loseConnect ",id);
    GlobalObject().netfactory.loseConnection(id);
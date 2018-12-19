#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from firefly.server.globalobject import GlobalObject
from firefly.netconnect.datapack import DataPackProtoc


def callWhenConnLost(conn):
    dynamicId = conn.transport.sessionno
    GlobalObject().remote['gate'].callRemote("netconnlost",dynamicId)

GlobalObject().netfactory.doConnectionLost = callWhenConnLost
dataprotocl = DataPackProtoc(19,82,8,28,1,1)
GlobalObject().netfactory.setDataProtocl(dataprotocl)



def loadModule():
    import netapp
    import gatenodeapp
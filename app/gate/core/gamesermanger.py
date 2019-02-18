#coding:utf8
'''
Created on 2012-3-19
场景服务器管理者
@author: Administrator
'''
from firefly.utils.singleton import Singleton
from twisted.python import log
from firefly.server.globalobject import GlobalObject


UP = 4000#每个游戏服承载的角色上限

class  ServerObj:
    
    def __init__(self,svrId):
        self.id = svrId
        self._clients = set()
        
    def addClient(self,clientId):
        '''添加一个客户端到游戏服务器'''
        self._clients.add(clientId)
        
    def dropClient(self,clientId):
        '''移除一个客户端'''
        self._clients.remove(clientId)
        
    def getClientCnt(self):
        '''获取场景中的客户端数量'''
        return len(self._clients)

class GameSerManager:
    
    __metaclass__ = Singleton
    
    def __init__(self):
        '''初始化'''
        self._svr_map = {}
        self._svr_pre = "game";
        self.initSvrs()
        
    def initSvrs(self):
        for childname in GlobalObject().root.childsmanager._childs.keys():
            if self._svr_pre in childname:
                self.addSvr(childname)
        
    def addSvr(self,svrname):
        '''添加一个场景服务器'''
        svr_ins = ServerObj(svrname)
        self._svr_map[svr_ins.id] = svr_ins
        return svr_ins
        

    def getServerById(self,svrId):
        '''返回服务的实例'''
        svr_ins = self._svr_map.get(svrId)
        if not svr_ins:
            svr_ins = self.addSvr(svrId)
        return svr_ins
        
    def addClient(self,svrId,clientId):
        '''添加一个客户端'''
        svr_ins = self.getServerById(svrId)
        if not svr_ins:
            return False
        svr_ins.addClient(clientId)
        return True
    
    def dropClient(self,svrId,clientId):
        '''清除一个客户端'''
        svr_ins = self.getServerById(svrId)
        if svr_ins:
            try:
                svr_ins.dropClient(clientId)
            except Exception:
                msg = "serverId:%d-------clientId:%d"%(svrId,clientId)
                log.err(msg)
        
    def getAllClientCnt(self):
        '''获取公共场景中所有的客户端数量'''
        return sum([ser.getClientCnt() for ser in self._svr_map])
    
    def getAllSceId(self):
        return self._svr_map.keys();
    def getBsetSvrNodeId(self):
        '''获取最佳的game服务器
        '''
        serverlist = self._svr_map.values()
        slist = sorted(serverlist,reverse=False,key = lambda sser:sser.getClientCnt())
        if slist:
            return slist[0].id
        
        
#coding:utf8
'''
Created on 2011-3-23

@author: sean_lan
'''
from app.share.dbopear import dbuser

INITTOWN = 1700
from twisted.python import log

class User:
    '''用户类'''
    
    def __init__(self, name,password,dynamicId = -1):
        '''
        @param id: int 用户的id
        @param name: str用户的名称
        @param password: str 用户的密码 
        @param pid: int 邀请者的id
        @param dynamicId: str 登录时客户端的动态ID
        @param characterId: dict 用户的角色
        @param isEffective: bool 是否是有效的
        '''
        self.id = 0
        self.name = name
        self.password = password
        self.pid = 0
        self.dynamicId = dynamicId
        self.isEffective = True
        self.characterId = 0
        self.node = "";
        self.Ischaracterlocked = False;#only used when client disconnected
        self.characterInfo = {}
        self.initUser()
    
    def initUser(self):
        '''初始化用户类'''
        data = dbuser.getUserInfoByUsername(self.name,self.password)
        if not data:
            self.isEffective = False
            return
        if not data['enable']:
            self.isEffective = False
        self.id = data.get('id',0)
        self.pid = data.get('pid',0)
        self.characterId = data.get('characterId',0)
        
    def getNickName(self):
        '''获取账号名
        '''
        return self.name
    def isLoginCharacter(self):
        return len(self.node) > 0;
    def getNode(self):
        '''返回角色所在的节点服务ID'''
        return self.node
    
    def setNode(self,node):
        '''设置角色的节点服务ID
        @param node: int 节点的id
        '''
        self.node = node
    def isCharacterLocked(self):
        return self.Ischaracterlocked;
    def lockChar(self,f):
        self.Ischaracterlocked = f;
        return;
    def CheckEffective(self):
        '''检测账号是否有效'''
        return self.isEffective
    
    def checkClient(self,dynamicId):
        '''检测客户端ID是否匹配'''
        return self.dynamicId == dynamicId
    
    def getCharacterInfo(self):
        '''获取角色的信息'''
        if not self.characterInfo:
            self.characterInfo = dbuser.getUserCharacterTotalInfo(self.characterId)
            #log.msg('User getCharacterInfo ',self.characterId,self.characterInfo)
        return self.characterInfo
        
    def setDynamicId(self,dynamicId):
        '''设置动态ID
        @param dynamicId: int 客户端动态ID
        '''
        self.dynamicId = dynamicId
    
    def getDynamicId(self):
        '''获取用户动态ID'''
        return self.dynamicId
    
    def creatNewCharacter(self ,nickname ,profession,shape,tm):
        '''创建新角色
        '''
        if len(nickname)<2 or len(nickname)>20:
            return False
        if self.characterId:
            return False
        if not dbuser.checkCharacterName(nickname):
            return False
        characterId = dbuser.creatNewCharacter(nickname, profession,shape, self.id,1,tm)
        if characterId:
            self.characterId = characterId
            return True;
        return False;
    
            
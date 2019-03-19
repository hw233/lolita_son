#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from firefly.server.globalobject import rootserviceHandle,GlobalObject
from app.gate.gateservice import localservice
from app.gate.core.UserManager import UsersManager
from app.gate.core.gamesermanger import GameSerManager
from app.gate.core.scenesermanger import SceneSerManager
from twisted.python import log
from app.protocol.ProtocolDesc import *
#test
scene_protocol = [C2S_MAP_MOVE];
chat_protocol = [C2S_CHAT];
combat_protocol = [C2S_WAR_PLAYEND];
@rootserviceHandle
def forwarding(key,dynamicId,data):
    """
    """
    if localservice._targets.has_key(key):
        return localservice.callTarget(key,dynamicId,data)
    else:
        user = UsersManager().getUserByDynamicId(dynamicId)
        if not user:
            return
        if not user.isLoginCharacter():
            return;
        if user.isCharacterLocked():
            return;
        if not user.CheckEffective():
            return;
        global scene_protocol;
        if key in scene_protocol:
            scene = user.getSceneNode();
            if scene:
                GlobalObject().root.callChild(scene,3,key,dynamicId,user.characterId,data);
            return
        global chat_protocol;
        if key in chat_protocol:
            GlobalObject().root.callChild("chat",3,key,dynamicId,user.characterId,data);
            return
        global combat_protocol;
        if key in combat_protocol:
            GlobalObject().root.callChild("combat",3,key,dynamicId,user.characterId,data);
            return
        node = user.getNode();
        return GlobalObject().root.callChild(node,3,key,dynamicId,user.characterId,data)
    

@rootserviceHandle
def pushObject(cmd,msg,sendList):
    """
    """
    #print "gate netforwarding %s %s"%(cmd,sendList);
    GlobalObject().root.callChild("net","pushObject",cmd,msg,sendList)
@rootserviceHandle
def pushObjectOthers(cmd,msg,exclude_list):
    """
    """
    GlobalObject().root.callChild("net","pushObjectOthers",cmd,msg,exclude_list)
@rootserviceHandle
def broadcastObject(srcsvr,cmd,dynamicId, characterId,data):
    """
    """
    allsceids = GameSerManager().getAllSceId();
    log.msg("broadcastObject ",len(allsceids),allsceids);
    for i in allsceids:
        if i != srcsvr:
            GlobalObject().root.callChild(i,4,i,cmd,dynamicId, characterId,data);

@rootserviceHandle
def startCombat(dynamicId, characterId,data):
    GlobalObject().root.callChild("combat",5,dynamicId, characterId,data);
@rootserviceHandle
def endCombat(dynamicId, characterId,data):
    GlobalObject().root.callChild("combat",6,dynamicId, characterId,data);

def DropClient(dynamicId):
    u = UsersManager().getUserByDynamicId(dynamicId)
    if u:
        if u.isCharacterLocked():
            return;
        if u.isLoginCharacter():
            u.lockChar(True);
            ##
            GlobalObject().root.callChild("chat",2,dynamicId,u.characterId);
            GlobalObject().root.callChild("combat",2,dynamicId,u.characterId);

            scene = u.getSceneNode();
            if scene:
                GlobalObject().root.callChild(scene,2,dynamicId,u.characterId);
                SceneSerManager().dropClient(scene, dynamicId)

            node = u.getNode();
            if node:
                GlobalObject().root.callChild(node,2,dynamicId,u.characterId);
                GameSerManager().dropClient(node, dynamicId)
            ###
            u.lockChar(False)#释放角色锁定,其实这里没有对数据库直接操作，而是通知各个子服自己处理，所以角色锁定没啥意义
            UsersManager().dropUserByDynamicId(dynamicId)
    return
@rootserviceHandle
def loseConnect(id):
    """svr req disconnect
    """
    DropClient(id);#注意该函数里并没有判断是由哪个服务器调用过来的，所以有可能有隐患

    GlobalObject().root.callChild("net","loseConnect",id)


@rootserviceHandle
def netconnlost(dynamicId):
    '''客户端断开连接时的处理
    @param dynamicId: int 客户端的动态ID
    '''
    DropClient(dynamicId);
    return






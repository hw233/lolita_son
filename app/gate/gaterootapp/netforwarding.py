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
def loseConnect(id):
    """
    """
    GlobalObject().root.callChild("net","loseConnect",id)

def SavePlayerInfoInDB(dynamicId):
    '''将玩家信息写入数据库'''
    u = UsersManager().getUserByDynamicId(dynamicId)
    scene = u.getSceneNode();
    if scene:
        GlobalObject().root.callChild(scene,2,dynamicId,u.characterId);

    GlobalObject().root.callChild("chat",2,dynamicId,u.characterId);

    node = u.getNode()
    d = GlobalObject().root.callChild(node,2,dynamicId,u.characterId);
    return d

def SaveDBSuccedOrError(result,u):
    '''写入角色数据成功后的处理
    @param result: 写入后返回的结果
    @param vcharacter: 角色的实例
    '''
    u.lockChar(False)#释放角色锁定
    return True

def dropClient(deferResult,dynamicId,u):
    '''清理客户端的记录
    @param result: 写入后返回的结果
    '''
    node = u.getNode()
    if node:#角色在场景中的处理
        GameSerManager().dropClient(node, dynamicId)
    scene = u.getSceneNode();
    if scene:#角色在场景中的处理
        SceneSerManager().dropClient(scene, dynamicId)

    UsersManager().dropUserByDynamicId(dynamicId)

@rootserviceHandle
def netconnlost(dynamicId):
    '''客户端断开连接时的处理
    @param dynamicId: int 客户端的动态ID
    '''
    u = UsersManager().getUserByDynamicId(dynamicId)
    if u:
        if u.isCharacterLocked():
            return;
        if u.isLoginCharacter():
            u.lockChar(True);
            d = SavePlayerInfoInDB(dynamicId)#保存角色,写入角色数据
            d.addErrback(SaveDBSuccedOrError,u)#解锁角色
            d.addCallback(dropClient,dynamicId,u)#清理客户端的数据
    else:
        UsersManager().dropUserByDynamicId(dynamicId)






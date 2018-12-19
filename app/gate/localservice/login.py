#coding:utf8
'''
Created on 2012-2-27

@author: sean_lan
'''
import json
from app.gate.gateservice import localserviceHandle
import app.protocol.netutil as netutil
from twisted.python import log
from firefly.server.globalobject import GlobalObject
from app.share.dbopear import dbuser
import app.protocol.ProtocolDesc as ProtocolDesc
from app.gate.core.User import User
from app.gate.core.UserManager import UsersManager
from app.gate.core.scenesermanger import SceneSerManager
import app.util.helper as helper
@localserviceHandle
def loginToServer_275(key,dynamicId,request_proto):
    argument = netutil.c2s_buf2data("C2S_LOGIN",request_proto);
    username = argument['account']
    password = argument['pwd']
    log.msg('loginToServer_1 %d %s ' % (dynamicId,str(argument)));
    userinfo = dbuser.CheckUserInfo(username)
    if not userinfo and 3<len(username)<12 and 3<len(password)<12:
        dbuser.creatUserInfo(username, password,helper.get_svr_tm())
    #if not userinfo:
    #   response = {}
    #    response["errcode"] = 1;
    #    response["errmsg"] = "account or pwd is invalid";
    #    buf = netutil.s2c_data2buf("S2C_LOGIN",response)
    #    GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_LOGIN,buf, [dynamicId]);
    #    return
    oldUser = UsersManager().getUserByUsername(username)
    u = oldUser;
    if oldUser:
        if oldUser.dynamicId != dynamicId:
            response = {}
            buf = netutil.s2c_data2buf("S2C_LOGIN_RELOGIN",response)
            GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_LOGIN_RELOGIN,buf, [dynamicId]);
            GlobalObject().root.callChild("net","loseConnect",oldUser.dynamicId)
        oldUser.dynamicId = dynamicId;
        response = {}
        response["flag"] = 1;
        buf = netutil.s2c_data2buf("S2C_LOGIN_OK",response)
        GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_LOGIN_OK,buf, [dynamicId]);
    else:
        u = User(username,password,dynamicId);
        if not u.CheckEffective():
            response = {}
            response["errcode"] = 2;
            response["errmsg"] = "account is banned";
            buf = netutil.s2c_data2buf("S2C_LOGIN",response)
            GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_LOGIN,buf, [dynamicId]);
            return;
        UsersManager().addUser(u);
        response = {}
        response["flag"] = 0;
        buf = netutil.s2c_data2buf("S2C_LOGIN_OK",response)
        GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_LOGIN_OK,buf, [dynamicId]);
        if u.characterId == 0:
            u.creatNewCharacter("character_%d"%(u.id),0,0,helper.get_svr_tm());
    response = {}
    roleinfo = {"rid":u.characterId,"shape":0,"cls":0,"grade":0,"desc":"","flag":0,"newtm":0,"theme":0,"name":"","offline":0,"logintm":0,"orgsrvid":0};
    response["roles"] = [roleinfo];
    buf = netutil.s2c_data2buf("S2C_LOGIN_ROLEINFO",response)
    GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_LOGIN_ROLEINFO,buf, [dynamicId]);
    return

@localserviceHandle
def selectrole_276(key,dynamicId,request_proto):
    argument = netutil.c2s_buf2data("C2S_LOGIN_SELECTROLE",request_proto);
    rid = argument['rid'];
    user=UsersManager().getUserByDynamicId(dynamicId)
    if not user:
        response = {}
        response["msg"] = "you haven't login";
        buf = netutil.s2c_data2buf("S2C_NOTIFY_FLOAT",response)
        GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_NOTIFY_FLOAT,buf, [dynamicId]);
        return;
    if user.characterId == 0:
        response = {}
        response["msg"] = "you haven't character";
        buf = netutil.s2c_data2buf("S2C_NOTIFY_FLOAT",response)
        GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_NOTIFY_FLOAT,buf, [dynamicId]);
        return;
    if user.characterId != rid:
        response = {}
        response["msg"] = "error characterId %d %d"%(rid,user.characterId);
        buf = netutil.s2c_data2buf("S2C_NOTIFY_FLOAT",response)
        GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_NOTIFY_FLOAT,buf, [dynamicId]);
        return;
    if user.isCharacterLocked():
        return;
    if not user.CheckEffective():
        response = {}
        response["msg"] = "account is banned";
        buf = netutil.s2c_data2buf("S2C_NOTIFY_FLOAT",response)
        GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_NOTIFY_FLOAT,buf, [dynamicId]);
        return;
    if user.isLoginCharacter():
        return;
    nownode = SceneSerManager().getBsetScenNodeId()
    d = GlobalObject().root.callChild(nownode,1,dynamicId, rid)
    user.setNode(nownode)
    SceneSerManager().addClient(nownode, dynamicId)

    response = {}
    buf = netutil.s2c_data2buf("S2C_LOGIN_SELECTROLE",response)
    GlobalObject().root.callChild("net","pushObject",ProtocolDesc.S2C_LOGIN_SELECTROLE,buf, [dynamicId]);
    return

@localserviceHandle
def createrole_278(key,dynamicId,request_proto):
    return
@localserviceHandle
def delrole_279(key,dynamicId,request_proto):
    return
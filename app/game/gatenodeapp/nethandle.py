#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from app.game.gatenodeservice import remoteserviceHandle
import app.protocol.netutil as netutil
from twisted.python import log
from firefly.server.globalobject import GlobalObject
import app.protocol.ProtocolDesc as ProtocolDesc
import app.base.event_dispatcher
import app.game.core.game_event_def
@remoteserviceHandle
def enter_1(dynamicId, characterId):
    app.base.event_dispatcher.event_dispatcher().fire_event(app.game.core.game_event_def.EVENT_LOGIN,{"dId":dynamicId,"cId":characterId});
    return
@remoteserviceHandle
def NetConnLost_2(dynamicId, characterId):
    '''loginout
    '''
    app.base.event_dispatcher.event_dispatcher().fire_event(app.game.core.game_event_def.EVENT_LOGOUT,{"dId":dynamicId,"cId":characterId});
    return True

@remoteserviceHandle
def nethandle_3(cmd,dynamicId, characterId,request_proto):
    log.msg("nethandle_3 %x %d %d"%(cmd,dynamicId,characterId))
    netdata = netutil.c2s_buff2databycmd(cmd,request_proto);
    app.base.event_dispatcher.event_dispatcher().fire_net_event(cmd,{"dId":dynamicId,"cId":characterId,"data":netdata});
    #if cmd == ProtocolDesc.C2S_WEBSOCKET_HELLO:
    #    log.msg('testnet_256 %s ' % (dynamicId));
    #    c_data = netutil.c2s_buf2data("C2S_WEBSOCKET_HELLO",request_proto);
    #    log.msg('msg:%s'%(c_data['msg']));
    #    c_data['msg'] = "svr reply:"+c_data['msg'];
    #    buf = netutil.s2c_data2buf("S2C_WEBSOCKET_HELLO",c_data)
    #    GlobalObject().remote['gate'].callRemote("pushObject",ProtocolDesc.S2C_WEBSOCKET_HELLO,buf, [dynamicId]) 
    return 
@remoteserviceHandle
def broadcast_4(srcsvr,cmd,dynamicId, characterId,data):
    app.base.event_dispatcher.event_dispatcher().fire_broadnet_event(cmd,{"srcsvr":srcsvr,"dId":dynamicId,"cId":characterId,"data":request_proto});
    return     

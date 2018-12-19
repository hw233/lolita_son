# coding:utf8
'''
Created on 2011-9-20
登陆服务器协议
@author: lan (www.9miao.com)
'''
from twisted.internet import protocol, reactor
from twisted.python import log
from manager import ConnectionManager
from datapack import DataPackProtoc
reactor = reactor


def DefferedErrorHandle(e):
    '''延迟对象的错误处理'''
    log.err(str(e))
    return


class LiberateProtocol(protocol.Protocol):
    '''协议'''

    buff = ""

    def connectionMade(self):
        '''连接建立处理
        '''
        log.msg('Client %d login in.[%s,%d]' % (self.transport.sessionno,
                self.transport.client[0], self.transport.client[1]))
        self.factory.connmanager.addConnection(self)
        self.factory.doConnectionMade(self)
        self.datahandler = self.dataHandleCoroutine()
        self.datahandler.next()

    def connectionLost(self, reason):
        '''连接断开处理
        '''
        log.msg('Client %d login out.' % (self.transport.sessionno))
        self.factory.doConnectionLost(self)
        self.factory.connmanager.dropConnectionByID(self.transport.sessionno)

    def safeToWriteData(self, data, command):
        '''线程安全的向客户端发送数据
        @param data: str 要向客户端写的数据
        '''
        if not self.transport.connected or data is None:
            return
        senddata = self.factory.produceResult(data, command)
        reactor.callFromThread(self.transport.write, senddata)

    def dataHandleCoroutine(self):
        """
        """
        length = self.factory.dataprotocl.getHeadlength()  # 获取协议头的长度
        while True:
            data = yield
            self.buff += data
            while self.buff.__len__() >= length:
                unpackdata = self.factory.dataprotocl.unpack(self.buff[
                                                             :length])
                if not unpackdata.get('result'):
                    log.msg('illegal data package --')
                    self.transport.loseConnection()
                    break
                command = unpackdata.get('command')
                rlength = unpackdata.get('length')
                request = self.buff[length:length+rlength]
                if request.__len__() < rlength:
                    log.msg('some data lose')
                    break
                self.buff = self.buff[length+rlength:]
                d = self.factory.doDataReceived(self, command, request)
                if not d:
                    continue
                d.addCallback(self.safeToWriteData, command)
                d.addErrback(DefferedErrorHandle)

    def dataReceived(self, data):
        '''数据到达处理
        @param data: str 客户端传送过来的数据
        '''
        self.datahandler.send(data)

# websocket start
handshake = '\
HTTP/1.1 101 Web Socket Protocol Handshake\r\n\
Upgrade: WebSocket\r\n\
Connection: Upgrade\r\n\
Sec-WebSocket-Accept: %s\r\n\r\n\
'
import re
import hashlib
import base64


class WebSocketLiberateProtocol(LiberateProtocol):

    def __init__(self):
        self._b_ready = False;
        return

    def dataHandleCoroutine(self):
        """
        """
        length = self.factory.dataprotocl.getHeadlength()  # 获取协议头的长度
        while True:
            data = yield
            self.buff += data
            log.msg('protoc dataHandleCoroutine get data ',data.__len__(),self.buff.__len__(),self._b_ready);
            if not self._b_ready:
                if not self.check_handshake_key(self.buff):
                    continue;
                hc, use_len = self.get_handshake_key(self.buff);
                self.buff = self.buff[use_len:];
                self.transport.write(hc);
                self._b_ready = True;
            #
            buff_len = self.get_buff_len(self.buff);
            if buff_len == -1:
                continue;
            opcode = self.get_opcode(self.buff);
            use_len, c_buff = self.parse_buff(self.buff, buff_len);
            log.msg('protoc dataHandleCoroutine ',buff_len,use_len,self.buff.__len__(),c_buff.__len__(),opcode);
            self.buff = self.buff[use_len:];
            if opcode == 0x8:
                log.msg('protoc quit ',c_buff);
                continue;
            while c_buff.__len__() >= length:
                unpackdata = self.factory.dataprotocl.unpack(c_buff[:length])
                if not unpackdata.get('result'):
                    log.msg('illegal data package --1')
                    self.transport.loseConnection()
                    break
                command = unpackdata.get('command')
                rlength = unpackdata.get('length')
                request = c_buff[length:length+rlength]
                if request.__len__() < rlength:
                    log.msg('some data lose %d %d %s',request.__len__(),rlength,command);
                    break
                c_buff = c_buff[length+rlength:]
                d = self.factory.doDataReceived(self, command, request)
                log.msg('protoc doDataReceived ',command,c_buff.__len__(),rlength,d);
                if not d:
                    continue
                d.addCallback(self.safeToWriteData, command)
                d.addErrback(DefferedErrorHandle)

    def safeToWriteData(self, data, command):
        '''线程安全的向客户端发送数据
        @param data: str 要向客户端写的数据
        '''
        if not self.transport.connected or data is None:
            return
        log.msg('websocket safeToWriteData ',command,len(data))
        senddata = self.factory.produceResult(data, command)
        log.msg('websocket safeToWriteData startbuildmsg ',command,len(senddata))
        senddata = self.buildMessage(senddata, False);
        log.msg('websocket safeToWriteData send ',command,len(senddata))
        reactor.callFromThread(self.transport.write, senddata)

    def get_handshake_key(self, buf):
        pos = buf.find("\r\n\r\n")
        cmd = buf[:pos+5]
        key = re.search("Sec-WebSocket-Key:\s*(\S+)\s*", cmd)
        key = key.group(1)
        key = key+'258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        key = base64.b64encode(hashlib.sha1(key).digest())
        return handshake % key, pos+4

    def check_handshake_key(self, buf):
        pos = buf.find("\r\n\r\n")
        if pos == -1:
            return False;
        cmd = buf[:pos+5]
        key = re.search("Sec-WebSocket-Key:\s*(\S+)\s*", cmd)
        if not key:
            return False;
        return True;
    def get_opcode(self,buf):
        opcode = ord(buf[0]) & 0b1111
        return opcode;
    def get_buff_len(self, buf):
        head_len = 2;
        buf_len = len(buf)
        if buf_len < head_len:
            return -1
        fin = ord(buf[0]) >> 7
        opcode = ord(buf[0]) & 0b1111
        payload = ord(buf[1]) & 0b1111111
        mask = ord(buf[1]) >> 7
        log.msg("get_buff_len opcode ",opcode)
        mask_len = 0;
        if mask:
            mask_len = 4;
        if payload < 126:
            if buf_len < (payload+head_len+mask_len):
                return -1
        elif payload == 126:
            ext_payload_len = 2;
            if buf_len < (head_len + ext_payload_len):  # ext_payload_len = 2
                return -1
            ext_len = 0;
            buf = buf[head_len:];
            for k, i in [(0, 1), (1, 0)]:
                ext_len += (ord(buf[k])*(1 << (8*i)))
            if buf_len < (ext_len+head_len+mask_len+ext_payload_len):
                return -1
            payload = ext_len
        else:
            ext_payload_len = 8;
            if buf_len < (head_len + ext_payload_len):  # ext_payload_len = 2
                return -1
            ext_len = 0;
            buf = buf[head_len:];
            for k, i in [(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]:
                ext_len += (ord(buf[k])*(1 << (8*i)))
            if buf_len < (ext_len+head_len+mask_len+ext_payload_len):
                return -1
            payload = ext_len
        return payload

    def parse_buff(self, buff, buff_len):
        mask = ord(buff[1]) >> 7;
        head_len = 2;
        mask_len = 0;
        ext_payload_len = 0;
        if mask:
            mask_len = 4;
        ret = buff;
        if buff_len < 126:
            ext_payload_len = 0;
        elif buff_len < 0xffff:
            ext_payload_len = 2;
        else:
            ext_payload_len = 8;

        buff_start = head_len+ext_payload_len+mask_len;
        ret = buff[buff_start:buff_start+buff_len];
        if mask:
            mask_start = head_len+ext_payload_len;
            mask_key = buff[mask_start:mask_start+mask_len];
            decoded_msg = "";
            for i in xrange(buff_len):
                c = ord(ret[i]) ^ ord(mask_key[i % 4])
                decoded_msg += str(chr(c))
            ret = decoded_msg;
        return head_len+ext_payload_len+mask_len+buff_len,ret
    ######
    def encodeMessage(self,buf, key):
        log.msg('protoc encodeMessage ',len(buf));
        encoded_msg = ""
        buf_len = len(buf)
        for i in xrange(buf_len):
            c = ord(buf[i]) ^ ord(key[i % 4])
            encoded_msg += str(chr(c))
        return encoded_msg
    def buildMessage(self,buf, mask=True):
        import sys
        log.msg("protoc buildMessage ",mask,sys.getdefaultencoding());
        c_buf = buf
        msg = ""
        if mask:
            key = "".join([str(chr(random.randrange(1,255))) for i in xrange(4)])
        # first byte
        o = (1 << 7) + 2
        log.msg('first byte ',o);
        msg += str(chr(o))
        # second byte
        buf_len = len(buf)
        if buf_len < 126:
            log.msg("protoc bm 1 ",mask);
            o = buf_len
            if mask:
                msg += str(chr(o + (1<<7)))
            else:
                msg += str(chr(o))
            log.msg("protoc bm 1 add buff ",mask,msg,buf);
            if mask:
                msg += key
                msg += self.encodeMessage(buf,key)
            else:
                msg += buf
            return msg;
        elif buf_len <= ((1 << 16) - 1):
            log.msg("protoc bm 2 ",mask);
            if mask:
                msg += str(chr(126 + (1 << 7)))
            else:
                msg += str(chr(126))
            for i in range(1, 3):
                o = (buf_len >> (16 - (8*i))) & (2**8 - 1)
                msg += str(chr(o))
            log.msg("protoc bm 2 add buff",mask);
            if mask:
                msg += key
                msg += self.encodeMessage(buf, key)
            else:
                msg += buf
            return msg;
        elif buf_len <= ((1 << 64) - 1):
            log.msg("protoc bm 3 ",mask);
            if mask:
                msg += str(chr(127 + (1 << 7)))
            else:
                msg += str(chr(127))
            for i in range(1, 9):
                o = (buf_len >> (64 - (8*i))) & (2**8 - 1)
                msg += str(chr(o))
            log.msg("protoc bm 3 add buff",mask);
            if mask:
                msg += key
                msg += self.encodeMessage(buf, key)
            else:
                msg += buf
            return msg;
        log.msg("protoc BuildMessage end ",len(msg));
        return msg
# websocket end
class LiberateFactory(protocol.ServerFactory):
    '''协议工厂'''
    protocol = WebSocketLiberateProtocol
    # protocol = LiberateProtocol
    
    def __init__(self,dataprotocl=DataPackProtoc()):
        '''初始化
        '''
        self.service = None
        self.connmanager = ConnectionManager()
        self.dataprotocl = dataprotocl
        
    def setDataProtocl(self,dataprotocl):
        '''
        '''
        self.dataprotocl = dataprotocl
        
    def doConnectionMade(self,conn):
        '''当连接建立时的处理'''
        pass
    
    def doConnectionLost(self,conn):
        '''连接断开时的处理'''
        pass
    
    def addServiceChannel(self,service):
        '''添加服务通道'''
        self.service = service
    
    def doDataReceived(self,conn,commandID,data):
        '''数据到达时的处理'''
        defer_tool = self.service.callTarget(commandID,conn,data)
        return defer_tool
    
    def produceResult(self,command,response):
        '''产生客户端需要的最终结果
        @param response: str 分布式客户端获取的结果
        '''
        return self.dataprotocl.pack(command,response)
    
    def loseConnection(self,connID):
        """主动端口与客户端的连接
        """
        self.connmanager.loseConnection(connID)
    
    def pushObject(self,topicID , msg, sendList):
        '''服务端向客户端推消息
        @param topicID: int 消息的主题id号
        @param msg: 消息的类容，protobuf结构类型
        @param sendList: 推向的目标列表(客户端id 列表)
        '''
        self.connmanager.pushObject(topicID, msg, sendList)


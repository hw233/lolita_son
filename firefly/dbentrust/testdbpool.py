#coding:utf8
'''
Created on 2013-5-8

@author: lan (www.9miao.com)
'''
from DBUtils.PooledDB import PooledDB
import MySQLdb

from MySQLdb.cursors import DictCursor
from MySQLdb.constants import FIELD_TYPE
from MySQLdb import convertors
DBCS = {'mysql':MySQLdb,}

class DBPool(object):
    '''
    '''
    def initPool(self,**kw):
        '''
        '''
        myconv = convertors.conversions.copy();

        myconv[FIELD_TYPE.VARCHAR] = str;
        print "FIELD_TYPE.VARCHAR:%s"%(FIELD_TYPE.VARCHAR);
        kw['conv'] = myconv;
        self.config = kw
        creator = DBCS.get(kw.get('engine','mysql'),MySQLdb)
        self.pool = PooledDB(creator,5,**kw)
        
    def connection(self):
        return self.pool.connection()

dbpool = DBPool()

def getUserCharacterTotalInfo(characterId):
    sql = "select * from tb_character where id = %d"%(characterId)
    conn = dbpool.connection()
    cursor = conn.cursor(cursorclass=DictCursor)
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
def creatNewCharacter(nickname):
    '''创建新的角色
    @param nickname: str 角色的昵称
    @param profession: int 角色的职业编号
    @param userId: int 用户的id
    @param fieldname: str 用户角色关系表中的字段名，表示用户的第几个角色
    '''
    print "dbUser creatNewCharacter %s %s"%(nickname,type(nickname));
    sql = "insert into `tb_character`(nickName,sex,figure,tm,town,position_x,position_y) \
    values('%s',%d,%d,%d,%d,%d,%d)"%(nickname ,0,0,0,0,0,0)
    sql2 = "SELECT @@IDENTITY"
    conn = dbpool.connection()
    cursor = conn.cursor()
    count = cursor.execute(sql)
    conn.commit()
    cursor.execute(sql2)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    if result and count:
        return result;
    else:
        return 0
def testfunc():
    d = {};
    d['host'] = "localhost";
    d['port'] = 3306;
    d['passwd'] = "rodger"
    d['user'] = "root";
    d['charset'] = 'utf8';
    d['db'] = "fishsvr";
    dbpool.initPool(**d);
    r = getUserCharacterTotalInfo(1000002);
    return r;
def testfunc2():
    d = {};
    d['host'] = "localhost";
    d['port'] = 3306;
    d['passwd'] = "rodger"
    d['user'] = "root";
    d['charset'] = 'utf8';
    d['db'] = "fishsvr";
    dbpool.initPool(**d);
    r = creatNewCharacter("mytestchar");
    return r;


#coding:utf8
'''
Created on 2013-5-8

@author: lan (www.9miao.com)
'''
from DBUtils.PooledDB import PooledDB
import MySQLdb

from MySQLdb.cursors import DictCursor

DBCS = {'mysql':MySQLdb,}

class DBPool(object):
    '''
    '''
    def initPool(self,**kw):
        '''
        '''
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
def testfunc():
    d = {};
    d['host'] = "localhost";
    d['port'] = 3306;
    d['passwd'] = "rodger"
    d['user'] = "root";
    d['charset'] = 'utf8';
    d['db'] = "fishsvr";
    dbpool.initPool(**d);
    r = getUserCharacterTotalInfo(1000001);
    return r;
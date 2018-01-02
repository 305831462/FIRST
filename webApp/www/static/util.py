#coding: utf -8

'访问数据库的代码 创建数据库连接、游标对象，然后执行SQL语句，最后处理异常，清理资源'

__author__ = 'sunyunpeng'

# 由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步IO操作，
#因为所有用户都是由一个线程服务的，协程的执行速度必须非常快，才能处理大量用户的请求。
#而耗时的IO操作不能在协程中以同步的方式调用，否则，等待一个IO操作时，系统无法响应任何其他用户。
import asyncio
import sqlite3
# 导入MySQL驱动:
import mysql.connector

#创建连接池
async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )


# file = open("/tmp/foo.txt")
# try:
#     data = file.read()
# finally:
#     file.close()


# with open("/tmp/foo.txt") as file:
#     data = file.read()


async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    async with __pool.get() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(sql.replace('?', '%s'), args or ())
            if size:
                rs = await cur.fetchmany(size)
            else:
                rs = await cur.fetchall()
        logging.info('rows returned: %s' % len(rs))
        return rs

async def execute(sql, args, autocommit=True):
    log(sql)
    async with __pool.get() as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
            raise
        return affected

# sudo /usr/local/mysql/support-files/mysql.server start
# sudo /usr/local/mysql/support-files/mysql.server stop
# sudo /usr/local/mysql/support-files/mysql.server restart

# 在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：

# [client]
# default-character-set = utf8

# [mysqld]
# default-storage-engine = INNODB
# character-set-server = utf8
# collation-server = utf8_general_ci

# show variables like '%char%';

def testCreateMySqlDB():
    # 注意把password设为你的root口令:
    conn = mysql.connector.connect(user='root',  database='test')
    cursor = conn.cursor()
    # 创建user表:
    # cursor.execute('create table testTable (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('insert into testTable (id, name) values (%s, %s)', ['3', '外国人'])
    # cursor.rowcount
    # 提交事务:
    conn.commit()
    cursor.close()
    conn.close()
    

def testSelcet():
    conn = mysql.connector.connect(user='root',  database='test') #password='password',
    # 运行查询:
    cursor = conn.cursor()
    cursor.execute('select * from testTable where id = %s', ('3',))
    values = cursor.fetchall()
    print(values)
    # 关闭Cursor和Connection:
    cursor.close()
    conn.close()

# testCreateMySqlDB()
testSelcet()













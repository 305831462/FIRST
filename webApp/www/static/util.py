#coding: utf -8

'访问数据库的代码 创建数据库连接、游标对象，然后执行SQL语句，最后处理异常，清理资源'

__author__ = 'sunyunpeng'

# 由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步IO操作，
#因为所有用户都是由一个线程服务的，协程的执行速度必须非常快，才能处理大量用户的请求。
#而耗时的IO操作不能在协程中以同步的方式调用，否则，等待一个IO操作时，系统无法响应任何其他用户。
import asyncio

#创建连接池
async def function(loop, **kw):
	logging.info('create database connection pool...')
	global __poll
	__poll = await aiomysql.create_pool(
		host = kw.get('host', 'localhost'),
		prot = kw.get('prot', 3306),
		user = kw['user'],
		password = kw['passowrd'],
		db = kw['db'],
		charset = kw.get('charset', 'utf8'),
		autocommit = kw.get('autocommit', True),
		maxsize = kw.get('maxsize', 10),
		minsize = kw.get('minsize',1),
		loop = loop
	)


# file = open("/tmp/foo.txt")
# try:
#     data = file.read()
# finally:
#     file.close()


# with open("/tmp/foo.txt") as file:
#     data = file.read()


async def select(sql, args, size = None):
	log(sql, args)
	global __poll
	with await __poll as coon:   # 相当于 try  open finally close
		cur = await coon.cursor(aiomysql.DictCursor)
		await cur.excute(sql.replace('?', '%s'), args or ())
		if size:
			rs = await cur.fetchmany(size)
		else:
			rs = await cur.fetchall()
		await cur.close()
		logging.info('rows returned: %s' % len(rs))
		return rs


async def excute(sql, args):
	log(sql)
	with await __poll as conn:
		try:
			cur = await coon.cursor()
			await cur.excute(sql.replace('?', '%s', args))
			affected = cur.rowcount
			await cur.close()
		except Exception as e:
			raise
		return affected



















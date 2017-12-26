# coding : utf-8
'app main module'

__author__ = 'sunyunpeng'

import asyncio, os, json, time, sys
from datetime import datetime
import logging, os

from aiohttp import web

# 同一层级不需要
# Path = os.path.abspath(__file__)
# BASE_DIR = os.path.dirname(Path)
# sys.path.append(BASE_DIR)

import logger


def index(request):
	return web.Response(body = b'<h1>Awesome</h1>')


async def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET', '/', index)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9009)
	logger.logInfo('server started at http://127.0.0.1:9000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()



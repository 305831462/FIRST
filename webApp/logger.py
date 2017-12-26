# coding = utf-8

__author__  = 'sunyunpeng'

import logging, os
import codecs
import shutil

#创建一个logger
logger =  logging.getLogger()
logger.setLevel(logging.INFO)

#第二步 创建一个handler 用于写入日志
logPath = './log'
if os.path.exists(logPath):
	# os.removedirs(logPath) 删除空文件夹
	shutil.rmtree(logPath)  #递归删除文件夹
	os.makedirs(logPath)
else:
	os.makedirs(logPath)

logfile = logPath + '/logger.txt'
if (not os.path.isfile(logfile)):
	# os.mknod(logfile)       # 创建空文件
	# fo = open(logfile, "wb") #没有就创建
	f = codecs.open(logfile, 'r', 'utf8') #尽量用这种方式 不能创建
# fo = open(logfile, "wb")
# f = codecs.open(logfile, 'a', 'utf8')  #没有就创建
# f = codecs.open(logfile, 'r', 'utf8')


# 函数用来删除一个文件:os.remove()
# 删除多个目录：os.removedirs（r“c：\python”）


fh = logging.FileHandler(logfile, mode = 'w')
fh.setLevel(logging.DEBUG)

#第三步 创建一个handler 用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

#第四步 定义handle的输出格式
# logging.basicConfig函数各参数:
# filename: 指定日志文件名
# filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
# format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
#  %(levelno)s: 打印日志级别的数值
#  %(levelname)s: 打印日志级别名称
#  %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
#  %(filename)s: 打印当前执行程序名
#  %(funcName)s: 打印日志的当前函数
#  %(lineno)d: 打印日志的当前行号
#  %(asctime)s: 打印日志的时间
#  %(thread)d: 打印线程ID
#  %(threadName)s: 打印线程名称
#  %(process)d: 打印进程ID
#  %(message)s: 打印日志信息
# datefmt: 指定时间格式，同time.strftime()
# level: 设置日志级别，默认为logging.WARNING
# stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

formatter = logging.Formatter('%(asctime)s&nbsp;-&nbsp;%(filename)s[line:%(lineno)d]&nbsp;-&nbsp;%(levelname)s:&nbsp;%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)  
logger.addHandler(ch) 


def logInfo(info):
	logger.info(info)

if __name__ == '__main__':
	pass
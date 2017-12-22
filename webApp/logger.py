# coding = utf-8

__author  = 'sunyunpeng'

import logging

#创建一个logger
logger =  logging.getLogger()
logger.setLevel(logging.INFO)

#第二步 创建一个handler 用于写入日志
logfile = './log/logger.txt'
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


def logInfo(info):
	logger.debug(info)


if __name__ == '__main__':
	pass
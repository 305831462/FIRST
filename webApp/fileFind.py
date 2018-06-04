
import os
import re
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

#根据文件扩展名判断文件类型
def endWith(s,*endstring):
    array = map(s.endswith,endstring)
    if True in array:
        return True
    else:
        return False

#将全部已搜索到的关键字列表中的内容保存到result.log文件中
def writeResultLog(dirname, luaTableStr):
    #行分隔符
    ls = os.linesep
    #结果日志文件名
    logfilename = dirname + "/script/FileAuthorMap.lua" #相对路径,文件在.py文件所在的目录中
    with open(logfilename,'w', encoding = 'utf-8') as fobj:
        fobj.writelines(luaTableStr)
        fobj.close()  

#筛掉不符合要求的文件
def isConfigureFile(filename):
	if (re.match(r'^DB_.*', filename)) :           #DB 表
		return True 
	elif (re.match(r'^copy_.*', filename)) : 		
		return True
	elif (re.match(r'^config_.*', filename)) :
		return True
	elif (re.match(r'^.*copy\d+.lua', filename)) :
		return True
	elif (re.match(r'^i18n_.*.lua', filename)) :  # 国际化
		return True


# 没有对应电话名字的按模块查找对应人
def getTelByModel(filename):
	# 孙云鹏负责的模块
	if (re.match(r'^SBList.*', filename)) :
		return '18612697503' 

	if (re.match(r'^Partner.*', filename)) :
		return '18612697503' 

	if (re.match(r'.*Drop.*', filename)) :
		return '18612697503' 

	if (re.match(r'.*Cell.*', filename)) :
		return '18612697503'

	if (re.match(r'.*trea.*', filename) or re.match(r'.*Trea.*', filename)) :
		return '18612697503'  

	if (re.match(r'.*MainTitle.*', filename)) :
		return '18612697503'

	if (re.match(r'.*Partner.*', filename) or re.match(r'.*Patner.*', filename) ) :
		return '18612697503'

	if (re.match(r'.*Bag.*', filename)) :
		return '18612697503'

	if (re.match(r'.*HeroFightUtil.*', filename)) :
		return '18612697503'
		

	#虞淙负责的模块
	if (re.match(r'.*WorldBoss.*', filename)) :
		return '18511452622'

	if (re.match(r'.*Formation.*', filename)) :
		return '18511452622'

	if (re.match(r'.*Buzhen.*', filename)) :
		return '18511452622'

	if (re.match(r'.*SkyPiea.*', filename)) :
		return '18511452622'
		

	#吕南春负责的模块
	if (re.match(r'.*copy.*', filename) or re.match(r'.*Copy.*', filename)) :
		return '18810465863'

	if (re.match(r'.*ShipLibrary.*', filename)) :
		return '18511452622'
	
	if (re.match(r'.*ShipInfo.*', filename)) :
		return '18511452622'
	
	#张琦
	if (re.match(r'.*LevelWelfare.*', filename)) :
		return '13810677600'

	if (re.match(r'.*GroupPurchase.*', filename)) :
		return '13810677600'

	if (re.match(r'.*BuyBox.*', filename)) :
		return '13810677600'

	if (re.match(r'.*Recharge.*', filename)) :
		return '13810677600'

	if (re.match(r'.*Impel.*', filename)) :
		return '13810677600'
		
		
	#杨娜
	if (re.match(r'.*MainRegist.*', filename)) :
		return '18600262413'

	if (re.match(r'.*MainRewardInfo.*', filename)) :
		return '18600262413'
		
	else :
		return "isAtAll"



#通过名字查找电话
def getTelByName(name):
	#是否是中文
	# zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
    # match = zh_pattern.search(name)

	if (name == '孙云鹏' or name.lower() == 'sunyunpeng'  or name.lower() == 'sunyupeng' or name.lower() == 'sunyunoeng') :
		return '18612697503'
	elif (name == '虞淙' or name.lower() == 'yucong' or name.lower() == 'yucng')  :
		return '18511452622'
	elif (name == '张琦' or name.lower() == 'zhangqi')  :
		return '13810677600'
	elif (name == '吕南春' or name.lower() == 'lvnanchun')  :
		return '18810465863'
	elif (name == '胡晓周' or name.lower() == 'huxiaozhou')  :
		return '18611560890'
	elif (name == '杨娜' or name.lower() == 'yangna')  :
		return '18600262413'
	elif (name == '郭春昊' or name.lower() == 'guochunhao')  :
		return '17184094012'
	else :
		return None
	

#遍历打开所有要在其中搜索内容的文件，若待搜索关键字列表为空，则不再继续遍历
def searchFilesContent(dirname):
	luaTableStr = '''module("FileAuthorMap", package.seeall)

'''
	configureFileList = []       #配置列表
	conformFileAuthorList = []	#确定名字的列表
	noConformFileAuthorList = [] #不确定名字的列表

	for root, dirs, files in os.walk(dirname):

	    for file in files:

	    	if endWith(file,'.lua'): #只在扩展名为.lua文件中搜索
	    		if (isConfigureFile(file)) : # 策划表
	    			configureFileList.append('	["' +file + '"]' + ' = ' + '"' + "isAtAll" + '"')

	    		else:
		    		filename = root + os.sep + file  #绝对路径

		    		#将路径中的单反斜杠替换为双反斜杠，因为单反斜杠可能会导致将路径中的内容进行转义了，replace函数中"\\"表示单反斜杠，"\\\\"表示双反斜杠
		    		filename = filename.replace("\\","\\\\")
		    		with open(filename,'r', encoding = 'utf-8') as fobj:

			    		#遍历文件的每一行
			    		for fileLine in fobj:

			    			# pattern = re.compile(r'Author')
			    			matchObj = re.match(r'(.*)(Author: )(.*)', fileLine)
			    			if (matchObj != None) :
				    			author = matchObj[3]
				    			# 拼接table 字符串
				    			telNum = getTelByName(author)
				    			if (telNum) :
				    				conformFileAuthorList.append('	["' + file + '"]' + ' = ' + '"' + telNum + '"')
				    			else :
				    				telNum = getTelByModel(file)
				    				noConformFileAuthorList.append('	["' + file + '"]' + ' = ' + '"' + telNum + '"')

	fileList = conformFileAuthorList + noConformFileAuthorList + configureFileList

#配置列表
	luaTableStr = luaTableStr + '''
local authorMap = {
'''	    				
	for luaStr in fileList:
		luaTableStr = luaTableStr + luaStr + ',' +'\n' 

	luaTableStr = luaTableStr + "}" + '''

-- 根据文件名字查找电话号码
function getTelByFileName( fileName )
	return authorMap[fileName]
end
'''
	writeResultLog(dirname, luaTableStr)

	print("search file succed")

#仅当本python模块直接执行时，才执行如下语句，若被别的python模块引入，则不执行
if __name__ == '__main__':
    searchFilesContent(sys.argv[1])

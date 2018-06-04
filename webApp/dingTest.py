import requests
import json
import urllib.parse
url = 'https://oapi.dingtalk.com/robot/send?access_token=faa8a4758761fff3c9a2269a0cacb573d2a906de9c1b74f0bf8e400251ebdcf0'
HEADERS = {
"Content-Type": "application/json ;charset=utf-8 "
}

String_textMsg = {
     "msgtype": "text",
     "text": {
         "content": "我就是我,  @18612697503 是不一样的烟火"
     },
     "at": {
         "atMobiles": [
             "18612697503"
         ], 
         # "isAtAll": "true"
     }
 }

String_textMsg = json.dumps(String_textMsg)
res = requests.post(url, data=String_textMsg, headers=HEADERS)
print(res.text)


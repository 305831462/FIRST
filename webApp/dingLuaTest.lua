
local arrField = {
                    ["msgtype"]         = "text",
                    ["text"]             = {["content"] = "我就是我,  @18612697503 是不一样的烟火"},
                    ["at"]                 = {    ["atMobiles"] = "18612697503", 
                                            ["isAtAll"] = "false"
                                          },
                    }

local cjson = require "cjson"
local jsonStr = cjson.encode(arrField)
local postData = jsonStr

local url = "https://oapi.dingtalk.com/robot/send?access_token=faa8a4758761fff3c9a2269a0cacb573d2a906de9c1b74f0bf8e400251ebdcf0"

local request = LuaHttpRequest:newRequest()
request:setRequestType(CCHttpRequest.kHttpPost)
request:setUrl(url)
request:setRequestData(postData, string.len(postData))
local arrHeader = CCArray:create()

arrHeader:addObject(CCString:create("Content-Type:application/json ;charset=utf-8 "))
request:setHeaders(arrHeader)

request:setResponseScriptFunc(function(sender, res)
    local status = res:getResponseCode()
    local data = res:getResponseData()

    logger:debug({func = "dingding robot return", status = status, data = data })
end)

CCHttpClient:getInstance():send(request)
request:release()
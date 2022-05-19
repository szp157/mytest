# -*- coding: UTF-8 -*-


import json
from time import sleep
from urllib import request
import requests


config = {"token":"8a8a5190aebbf3ab7581ca96ca6f2140e34d5160","id":"20216"}

def getphone():
    url = "http://api.my531.com/GetPhone/?token=" + config["token"] + "&card=0&id=" + config["id"]
    result = requests.get(url)
   
    result = result.content

    a = result.find("1|".encode())
    b = result[a+2:]
    
    return b


def getcode(phone):
    url = "http://api.my531.com/GetMsg/?token=" + config["token"] + "&dev=szptx123&id=" + config["id"] + "&phone=" + phone
    result = requests.get(url)
    result = bytes.decode(result.content)
    return result


def addblack(phone):
    url = "http://api.my531.com/Addblack/?token="+config["token"]+"&type=json&id="+config["id"]+"&phone="+phone
    result = requests.get(url)
    son = result.content
    return son
    

def main():

    phone = ""
    phone = getphone()
    print(phone)
    phone = bytes.decode(phone)
    url = "https://jdapi.shmedia.tech/media-basic-port/api/app/auth/send_validate_code"

    data = '{"mobile":"' + phone + '"}'

    header = {
        "log-header": "I am the log request header.",
        "deviceId": "",
        "siteId": "310114",
        "token": "",
        "Content-Type": "application/json; charset=UTF-8",
        "Content-Length": "24",
        "Host": "jdapi.shmedia.tech",
        "Connection": "Keep-Alive",
        "User-Agent": "okhttp/3.14.2"

    }


    result = requests.post(url,data = data,headers=header)
    print(result.content)

    mydata = result.content
    myjson = json.loads(mydata)

    print(myjson["msg"])

    if myjson["msg"].find("ccess") > 0 :
        #发送验证码成功
        ftk = myjson["data"]["formToken"]
        print(ftk)

        url = "https://jdapi.shmedia.tech/media-basic-port/api/app/auth/validate_code_login"

        for i in range(0,15):
            print("正在进行第%d次获取验证码"%(i+1))
            code = getcode(phone)
            print(code)
            if len(code) > 35:
                break
            sleep(3)
        
        if i >= 14:
            exit()


        before = code.find("验证码")
        code = code[before+3:before+9]
        print(code)

        data = '{"formToken":"'+ftk+'","mobile":"'+phone+'","validateCode":"'+code+'"}'

        result = requests.post(url,data=data,headers=header)

        mydata = bytes.decode(result.content)
        myheader = result.headers
        print(mydata)
        print(myheader)

        #myjson = json.loads(myheader)

        print(myheader["token"])

        token = myheader["token"]

        url = "https://yxapi.shmedia.tech/unite/api/login"

        data = '{"token":"'+token+'","platform":"310114","activitys_id":"20"}'

        header = {
            'Host': 'yxapi.shmedia.tech',
            'Connection': 'keep-alive',
            'Content-Length': '292',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://yxapi.shmedia.tech',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Android SDK built for x86 Build/OSM1.180201.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari; Rmt/Jiading; Version/3.0.8',
            'id': 'null',
            'Content-Type': 'application/json',
            'Referer': 'https://yxapi.shmedia.tech/JDBlindbox/',
            'Accept-Language': 'zh-CN,en-US;q=0.8',
            'X-Requested-With': 'com.wdit.shrmtjd'
        }
        result = requests.post(url,data=data,headers=header)

        mydata = bytes.decode(result.content)
        print(mydata)

        myjson = json.loads(mydata)

        tid = myjson["data"]["id"]
        print(tid)

        #进行抽奖
        url = "https://yxapi.shmedia.tech/unite/api/go/prize/draw"

        data = '{"gifts_id":"17","platform":"310114"}'

        header = {
            'Host': 'yxapi.shmedia.tech',
            'Connection': 'keep-alive',
            'Content-Length': '37',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://yxapi.shmedia.tech',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Android SDK built for x86 Build/OSM1.180201.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari; Rmt/Jiading; Version/3.0.8',
            'id': tid,
            'Content-Type': 'application/json',
            'Referer': 'https://yxapi.shmedia.tech/JDBlindbox/',
            'Accept-Language': 'zh-CN,en-US;q=0.8',
            'X-Requested-With': 'com.wdit.shrmtjd'
        }

        result = requests.post(url,data=data,headers=header)


        mydata = bytes.decode(result.content)
        print(mydata)

        myjson = json.loads(mydata)
        print(myjson)

        
        fdata = phone + '----token:' + token + '----tid:' + tid + '----' + myjson["message"]
        with open('上海嘉定.txt','a+',encoding='utf-8') as f:
            f.write(fdata+'\n')
            f.close()


        

for k in range(10):
    main()
    sleep(2)



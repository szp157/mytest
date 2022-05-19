
# -*- coding: UTF-8 -*-


import json
import  random
from time import sleep
from urllib import request
from attr import s
import requests
import time
import datetime




config = {"token":"8a8a5190aebbf3ab7581ca96ca6f2140e34d5160","id":"10046"}

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


phone = getphone()
phone = bytes.decode(phone)
mytime = time.time()
print(phone)


rtid = "0HoeUbB3JrHRS4n4yfwAelfkkqKNKBEj"
#sgvG7nEkHA7q056NZq8UFSfcmkkBwvvf
mynum = random.choice(range(28))
mynum2 = random.choice(range(28))
mylist = "1234567890ABCDEFGHIJKLMNOPQRSTUV"

#rtid = rtid.replace(rtid[mynum:mynum+4],mylist[mynum2:mynum2+4])
print(rtid)

mytime = int(round(mytime*1000))
print(mytime)

url = 'https://dl.reg.163.com/dl/ini?pd=yanxuan_web&pkid=pXPYGTc&pkht=you.163.com&channel=0&topURL=https%3A%2F%2Fm.you.163.com%2Fu%2Flogin%3Fcallback%3D%252Fucenter&rtid='+rtid+'&nocache='+str(mytime)
result = requests.get(url)

print(result.headers)
webpx = result.headers["Set-Cookie"]

webpx = webpx[webpx.find("l_s_yanxuan_webpXPYGTc"):webpx.find(";")]
print(webpx)


url = 'https://dl.reg.163.com/dl/yd/nlregssms?un='+phone+'&pd=yanxuan_web&pkid=pXPYGTc&pkht=you.163.com&channel=14&topURL=https%3A%2F%2Fact.you.163.com%2Fact%2Fpub%2Fssr%2FWkIQTkVgpmXP.html%3Fchannel_type%3D1&rtid='+rtid+'&nocache='+str(mytime)
print(url)
head = {
    'Host': 'dl.reg.163.com',
    'Connection':'keep-alive',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Content-Type': 'application/json',
    'Accept':'*/*',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'l_s_yanxuan_webpXPYGTc=1A8C55A9259CC4C2D3ED749B79A4AC7F1693939C4B15C37123BBA16C235B12D5B53FA4A055869356573C9D6C4021F5C9B0CC93E47922135DE2FE8CDAB8BCDA1A4C757CA4B9AC92D0A795C6D1A37FA5310E56A48871198A3CA6FA9E0E456D16B11B3B7C274C7EC1486C5578829CB2C17F'
}

result = requests.get(url=url,headers=head)
result1 = bytes.decode(result.content)
print(result1)

if result1.find('201')>0:
    print('发送成功')

    for i in range(0,20):
        print("正在进行第%d次获取验证码"%(i+1))
        code = getcode(phone)
        print(code)
        if len(code) > 30:
            break
        sleep(5)
        
    if i >= 19:
        exit()


    before = code.find("验证码")
    code = code[before+4:before+10]
    print(code)

    mytime = int(round(mytime*1000))
    print(mytime)
    url = 'https://dl.reg.163.com/dl/yd/nlgt?un='+phone+'&channel=14&pd=yanxuan_web&pkid=pXPYGTc&pkht=you.163.com&topURL=https%3A%2F%2Fact.you.163.com%2Fact%2Fpub%2Fssr%2FWkIQTkVgpmXP.html%3Fchannel_type%3D1&rtid='+rtid+'&nocache='+str(mytime)
    head = {
        'Host': 'dl.reg.163.com',
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html?cd=https%3A%2F%2Fyanxuan.nosdn.127.net%2F&cf=aa792d9e06498deb43023ed84ab1514d.css&MGID=1648104268305.7393&wdaId=&pkid=pXPYGTc&product=yanxuan_web',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'l_yd_s_yanxuan_webpXPYGTc='+webpx
        }

    result = requests.get(url,headers=head)
    myjson = json.loads(bytes.decode(result.content))
    print(myjson)
    tk = myjson["tk"]
    print(tk)

    url = "https://dl.reg.163.com/dl/yd/nlregvfsms"

    data = '{"un":"'+phone+'","sms":"'+code+'","pd":"yanxuan_web","pkid":"pXPYGTc","pkht":"you.163.com","tk":"'+tk+'","domains":"","channel":14,"topURL":"https://act.you.163.com/act/pub/ssr/WkIQTkVgpmXP.html?channel_type=1","rtid":"'+rtid+'"}'

    head = {
        'Host': 'dl.reg.163.com',
        'Connection': 'keep-alive',
        'Content-Length': '280',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://dl.reg.163.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://dl.reg.163.com/webzj/v1.0.1/pub/index_dl2_new.html?cd=https%3A%2F%2Fyanxuan.nosdn.127.net%2F&cf=aa792d9e06498deb43023ed84ab1514d.css&MGID=1648035803346.0393&wdaId=&pkid=pXPYGTc&product=yanxuan_web',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'l_yd_s_yanxuan_webpXPYGTc='+webpx
    }

    result = requests.post(url,data=data,headers=head)
    print(result.headers)
    print(result.content)
    myjson = result.headers
    cookie = myjson["Set-Cookie"]
    print(cookie)
    before1 = cookie.find("l_yd_sign=")
    after1 = cookie.find(";",before1)
    before2 = cookie.find("NTES_YD_SESS=",before1)
    after2 = cookie.find(";",before2)
    before3 = cookie.find("P_INFO=",before2)
    after3 = cookie.find(";",before3)

    mycookie = cookie[before1:after1] + ';' + cookie[before2:after2] + ';' + cookie[before3:after3]
    print(mycookie)
    data = phone + '----' + mycookie
    with open('网易.txt','a+',encoding="utf-8") as f1:
        f1.write(data+'\n')
        f1.close()

    




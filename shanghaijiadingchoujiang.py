# -*- coding: UTF-8 -*-

import json
import requests


with open('上海嘉定.txt','r',encoding='utf-8') as f:
    list = f.readlines()
    print(list)

    for i in range(0,len(list)):
        list[i] = list[i].strip('\n')
        phone = list[i][0:11]
        print(phone)
        before = list[i].find('token:')
        after = list[i].find('----tid')
        ftk = list[i][before+6:after]
        print(ftk)

        url = "https://yxapi.shmedia.tech/unite/api/login"

        data = '{"token":"'+ftk+'","platform":"310114","activitys_id":"20"}'

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

        message = myjson["message"]
        if message.find("已中奖") >= 0:
            code = myjson["data"]
            #print(code)
            adata = phone + '----' + str(code)
            print(adata)
            with open('中奖名单.txt','a+',encoding='utf-8') as f2:
                f2.write(adata+'\n')
                f2.close()


    f.close()
    



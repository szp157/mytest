# -*- coding: UTF-8 -*-

import json
from time import sleep
import requests

mylist = [140,47,130]

url = "https://m.you.163.com/xhr/lifeRights/receive.json?csrf_token="

mycookies = ''


with open('wangyi.txt','r',encoding='utf-8') as f:
    list = f.readlines()
    print(list)

    for a in range(0,len(list)):
        list[a] = list[a].strip('\n')
        b = list[a].find("----")
        mycookies = list[a][b+4:len(list[a])]
        print(mycookies)
        header = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-length': '33',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://act.you.163.com',
            'referer': 'https://act.you.163.com/act/pub/ssr/WkIQTkVgpmXP.html?channel_type=1',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'cookie': mycookies
        }

        for i in range(0,len(mylist)):
            
            data = 'rightsId=' + str(mylist[i])
            print(data)
            result = requests.post(url=url,data=data,headers=header)
            result = result.content.decode("utf-8")
            #print(result)
            dic = json.loads(result)
            print(dic)

# -*- coding: UTF-8 -*-

import json
from time import sleep
import requests

with open('wangyi.txt','r',encoding='utf-8') as f:
    list = f.readlines()
    print(list)

    url = "https://act.you.163.com/napi/aielx/inner/getComplexWelfareNoCode?csrf_token="
    data = '{"aieChannel": "6af75697a0a4c193"}'

    for i in range(0,len(list)):
        list[i] = list[i].strip('\n')
        a = list[i].find("----")
        mycookies = list[i][a+4:len(list[i])]
        print(mycookies)

        header = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-length': '33',
            'content-type': 'application/json',
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

        result = requests.post(url=url,data=data,headers=header)
        result = bytes.decode(result.content)
        print(result)
        sleep(3)




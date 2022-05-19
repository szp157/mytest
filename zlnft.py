# -*- coding: UTF-8 -*-

from datetime import date
import json
import requests

url = "https://www.zlnft.cn/api/krshop/market/getNftSellList"

header = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9',
            'content-length': '111',
            'content-type': 'application/json',
            'origin': 'https://m.zlnft.net',
            'referer': 'https://m.zlnft.net/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': "Android",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'token': '23baa950-dd7e-4aa8-b713-49294c6cab52',
            'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
        }

data1 = '{"nft_id":"6716","is_sell":"","no_sort":"","price_sort":"asc","page":"1","pageSize":"10","_platform":"android"}'
result = requests.post(url=url,data=data1,headers=header)

mydata = result.content.decode(encoding="GBK",errors='ignore')
print(mydata)

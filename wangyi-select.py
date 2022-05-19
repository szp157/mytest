# -*- coding: UTF-8 -*-

import json
from time import sleep
import requests

url = "https://m.you.163.com/xhr/lifeRights/pageListByType.json?csrf_token="
data = '&page=1&size=100'
mycookies = 'yx_csrf=572f8c63fda60f131eabea5a22d8b6d2;yx_userid=26244479388;yx_username=yd.b47baba4d44440228%40163.com;yx_sid=763108d7-501c-4704-affa-4e4e05ece389;yx_stat_seqList=v_75a7f49de8%7Cv_9dba3645a1%3B-1%3Bv_1a6d68232e%3B-1%3Bv_75a7f49de8%3B-1;NTES_YD_SESS=2S_CnCSpYT6i_PNSQWKuSlqMb6qdvq7OyirWPzo6LrzS.6Js.4TFkU2uzdnw2yUHcHBga6DXxtBtyv6o42fR1bQdeRn8LFeybHjqykaQ.krDGFUkXMvacPmkTGDqG4y3HrmigdQ0qzUyGPNc5Iz5AOrQ_rSLUtI67T98FDkJge3vT6eBNpA5A9ND7t4jyp.6jY3zUFNMO0xMxBohXkXx7INIiWHpzAq2lKWHmDW1Vv7RB;P_INFO=16756326705|1652705933|1|yanxuan_web|00&99|null&null&null#gud&null#10#0|&0|null|16756326705;_bl_uid=yslOk31O8yvqnvfpqiwCtn38adj9;yx_s_tid=tid_web_6c7476cb084640e7bab76e02d65b3020_87270ec12_1;yx_but_id=90fbae2a3afd422999379748c7f79f975adab0b6442979fb_v1_nl;yx_s_device=65d38ab-79b3-2e2b-86bd-1e5ec13cb3;yx_stat_seesionId=223479ba-c15b-475c-9cf4-f0f64ca6287b1652705916451;yx_aui=223479ba-c15b-475c-9cf4-f0f64ca6287b;S_INFO=1652705933|0|0&60##|16756326705;mail_psc_fingerprint=f8e1d342442f62f9dd9e36ef6afe0f12;yx_stat_ypmList=;'

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

result = requests.post(url=url,data=data,headers=header)
result = result.content.decode("utf-8")
#print(result)
dic = json.loads(result)
print(dic)
list = dic['data']['result']

#print(list[0]['name'])

mydata = ""
for i in range (0,len(list)):
    #print(list[i]['name'])
    mydata = str(mydata) + list[i]['name'] + '----' + str(list[i]['externalRightsId']) + '----' + str(list[i]['id']) + '\n'


print(mydata)

with open('网易查询.txt','a+',encoding='utf-8') as f2:
    f2.write(mydata + '\n')
    f2.close()


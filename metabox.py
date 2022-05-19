# -*- coding: UTF-8 -*-

import imp
import json
import requests




url = "https://www.metaboxglobal.cn/api/backend/resell/v1/list?language=CN&page_num=1&order_by=2&group_name=&page_size=100"

header = {
            'access-control-allow-credentials': 'true',
            'access-control-allow-headers': 'Content-Type, Content-Length, Accept-Encoding, X-Auth-Token, X-CSRF-Token, Authorization, accept, origin, Cache-Control, X-Requested-With',
            'access-control-allow-methods': 'POST, OPTIONS, GET, PUT, DELETE',
            'access-control-allow-origin': '*',
            'content-type': 'application/json; charset=utf-8',
            'date': 'Thu, 12 May 2022 10:58:26 GMT',
            'eagleid': 'b7e89f2416523531066833821e',
            'server': 'Tengine',
            'timing-allow-origin': '*',
            'vary': 'Accept-Encoding',
            'via': 'cache29.l2nu16[15,0], kunlun6.cn1585[64,0]'
        }

result = requests.get(url=url,headers=header)

mydata = result.content.decode(encoding="GBK",errors='ignore')

#print(mydata)


stra = mydata.find('cards"')
strb = mydata.find(']}')

data1 = mydata[stra:strb+1]
#print(data1)

myname = []
myprice = []
mylevel = []
b = 0
for i in range(100):
    a = data1.find('name":"',b)
    b = data1.find('",',a)
    name = data1[a+7:b]
    myname.append(name)

    a = data1.find('price":',b)
    b = data1.find(',',a)
    price = data1[a+7:b]
    myprice.append(price)

    a = data1.find('level":"',b)
    b = data1.find('"}',a)
    level1 = data1[a+8:b]
    mylevel.append(level1)

print(myname)
print(myprice)
print(mylevel)

for j in range(100):
     print(myname[j]+'----'+myprice[j]+'----'+mylevel[j])



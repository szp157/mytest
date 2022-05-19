
import json
from pathlib import Path
import time
from requests import request
import requests
from selenium import webdriver
import selenium

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')


config = {"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyODI5OTQ2OTYyNzg1NDg0OCwidXNlcm5hbWUiOiJzenBwZ3kxMjMiLCJleHAiOjg4NTI2MDcxODUsImlzcyI6InljY29kZSJ9.lqS-W8MMSFizeiyqQjBEzAlRHJbz-0vR_a2YES5sy0Y","id":"14197"}


def getphone():
    url = "http://www.dbnx.xyz:7923/api/v1/getphonenumber?token=" + config["token"] + "&projectId=" + config["id"]
    result = requests.get(url)
   
    result = result.content

    result = result.decode()
    print(result)
    a = result.find('mobileNo')
    b = result[a+11:a+22]
    #print(b)

    a = result.find('mid')
    b = result.find('",',a)
    c = result[a+6:b]
    print(c)
    return c


def getcode(mid):
    url = "http://www.dbnx.xyz:7923/api/v1/getsms?token=" + config["token"] + "&mid=" + mid
    result = requests.get(url)
    result = result.content.decode(encoding="utf-8")
    print(result)
    return result


def addblack(mid):
    url = "http://www.dbnx.xyz:7923/api/v1/addblacknumber?token="+config["token"]+ "&mid=" + mid
    result = requests.get(url)
    son = result.content
    return son


def mymain():
    b = webdriver.Chrome()
    b.get('https://m.you.163.com/u/login?callback=%2Fucenter')
    b.implicitly_wait(2)

    b.find_element_by_xpath('//*[@id="j-bd"]/div/div[2]/div/div[1]/div[2]/div/div[1]').click()
    b.implicitly_wait(2)

    #b.find_element_by_id()

    list = b.find_elements_by_xpath("//iframe[contains(@id,'x-URS-iframe')]")

    b.switch_to.frame(list[0])

    #获取mid，后取出phone
    mid = getphone()
    phone = mid[(len(mid) - 11):len(mid)]

    b.find_element_by_id('phoneipt').send_keys(phone)
    b.implicitly_wait(2)
    b.implicitly_wait(2)


    #点击获取验证码
    list = b.find_elements_by_tag_name("a")
    #print(list)


    for l in list:
        print(l.get_attribute('href'))


    list[3].click()

    time.sleep(2)

    for i in range(0,15):
            print("正在进行第%d次获取验证码"%(i+1))
            code = getcode(mid)
            print(code)
            if code.find('code":1000') > 0:
                break
            time.sleep(3)
        
    if i >= 14:
        print(addblack(mid=mid))
        exit()
    #输入验证码

    ac = code.find('验证码')
    smscode = code[ac+4:ac+10]
    print(smscode)
    #smscode = "888888"
    b.find_element_by_name('phonecode').send_keys(smscode)
    time.sleep(2)

    list[4].click()

    time.sleep(10)
    mycookie = b.get_cookies()
    print(mycookie)
    #mycookie = json.dumps(mycookie)
    #Path('./wangyi.txt').write_text(mycookie)
    #time.sleep(5000)

    #b.quit()
    mycookies = ""
    #mydic = {}
    for i in range (0,len(mycookie)):
        print(mycookie[i])
        mycookies = mycookies + mycookie[i]['name'] + "=" + mycookie[i]['value'] + ";"
        
    print(mycookies)

    with open('wangyi.txt','a+',encoding='utf-8') as f2:
                f2.write(phone + "----" + mycookies+'\n')
                f2.close()

mymain()





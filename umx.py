from urllib import request
import requests


url = "https://api.umxverse.com/asset/productCache/market/selling?page=0&size=20&authorName=%E9%AB%98%E5%B0%8F%E5%8D%8E&authorId=97830388cBAF7345F8f3bf9DD913D5B58C2B7954&seriesId=&status=&sort=time&productName="


head = {
    "x-section-id":"8021236a00a3f32717f1b8546045f9a0",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"

}

result = requests.get(url)
#print(result)

#print(result.content)

#作品名、价格、在售
name=price=good = []
data = {}
data = result.content
'''
beforestr = data.find('total":'.encode())
afterstr = data.find(',"totalPages'.encode())
total = int(data[beforestr+7:afterstr])

print(total)
data1 = {}

data1 = dict(tuple(data))


print(data1.keys())


#for i in range(0,total):

'''

print(data[0])
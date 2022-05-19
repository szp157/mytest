import requests

url = 'https://dl.reg.163.com/dl/ini?pd=yanxuan_web&pkid=pXPYGTc&pkht=you.163.com&channel=0&topURL=https%3A%2F%2Fm.you.163.com%2Fu%2Flogin%3Fcallback%3D%252Fucenter&rtid=0HoeUbB3JrHRS4n4yfwAelfkkqKNKBEj&nocache=1648209677422'
result = requests.get(url)

print(result.headers)
webpx = result.headers["Set-Cookie"]

webpx = webpx[webpx.find("l_s_yanxuan_webpXPYGTc"):webpx.find(";")]
print(webpx)

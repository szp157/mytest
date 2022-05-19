
#输入年月日，计算第几天

from tkinter.tix import DisplayStyle
'''
year = int(input("年份："))
month = int(input("月份："))
day = int(input("日期："))

couth = 0

months = [1,2,3,4,5,6,7,8,9,10,11,12]
days = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(0,13):
    if month == months[i]:
        for j in range(0,i):
            couth = couth + days[j]
        break
    


couth = couth + day
print(couth)

if((year%100!=0 and year%4==0)or(year%100==0 and year%400==0)):
    if(month>2):
        couth += 1

print("今天是第%d天" %couth)
'''


year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0 < month <=12:
    sum = months[month-1]
else:
    print("data error")

sum = sum + day
leap = 0

if (year%400==0) or ((year%4==0)and(year%100!=0)):
    leap = 1

if(leap==1) and (month>2):
    sum += 1

print('it is the %dth day' %sum)


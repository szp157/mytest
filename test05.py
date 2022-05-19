#!/usr/bin/python3
#输出一个有序的序列
'''
a = int(input("整数1:"))
b = int(input("整数2:"))
c = int(input("整数3:"))

l = [a,b,c]

for i in range(0,3):
    for j in range(i,3):
        if l[i] > l[j]:
            d = l[i]
            l[i] = l[j]
            l[j] = d
            break

print(l)

'''
'''
l = []
for i in range(3):
    x = int(input("请输入第%d个整数：\n"%(i+1)))
    l.append(x)

l.sort()
print(l)
'''

l = [8,2,50,66,89,55,520,12,1]
print(l)
print(len(l))
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if l[i] > l[j]:
            d = l[i]
            l[i] = l[j]
            l[j] = d
            continue

print(l)



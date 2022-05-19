
#1,2,3,4组成三位数

list = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j) and (i!=k) and (j!=k):
                a = str(i)+str(j)+str(k)
                ##print(a)
                list.append(a)

print(list)
print(len(list))

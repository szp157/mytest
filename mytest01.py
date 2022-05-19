
list3 = []
with open('ip1.txt','r') as f1:
    list1 = f1.readlines()
    #print(list1)
    for i in range(0,len(list1)):
        with open('ip2.txt','r') as f2:
            list2 = f2.readlines()
            #print(list2)
            for j in range(0,len(list2)):
                #print(list2[j])
                if list1[i] == list2[j]:
                    list3.append(list1[i])
                    print(list1[i])
                    break
        f2.close()

f1.close()
print(list3)




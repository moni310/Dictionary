# n=int(input("enter any nuber"))
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)

dic = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for i in dic.keys():
    print(i,end=" ")
for j in dic.values():
    for k in j:
        print(k)
    
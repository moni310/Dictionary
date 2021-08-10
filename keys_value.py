
# dic = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# for i in dic.keys():
#     print(i,end=" ")
# print()
# b=[]
# for j in dic.values():
#     b.append(j)
# # print(b)
# m=b
# k=0
# while k<len(m):
#     j=0
#     while j<len(m[k]):
#         s=m[k][j]
#         print(s,end=" ")
#         j=j+1
#     print()
#     k=k+1


list=[[1,"shikha","v"],[2,"neha","v"],[3,"joya","v"],[4,"moni","v"]]
i=0
b=[]
while i<len(list):
    j=1
    while j<len(list[i]):
        m=list[i][j]
        b.append(m)
        j=j+1
    i=i+1
print(b)

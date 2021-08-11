dic=[[1,"shikha","v"],[2,"neha","v"],[3,"joya","v"]]
i=0
b=[]
while i<len(dic):
    i=i+1
    b.append(i)
list2=b
em=[]
k=0
while k<len(dic):
    j=1
    while j<len(dic[k]):
        m=dic[k][j]
        em.append(m)
        j=j+1
    k=k+1
list=em
i=0
list3=[]
while i<len(list):
    empty=[]
    empty.append(list[i])
    empty.append(list[i+1])
    i=i+2
    list3.append(empty)
print(dict(zip(list2,list3)))

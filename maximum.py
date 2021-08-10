dic={"apple":9,"mango":90,"banana":43,"pineapple":31,"maggi":34}
b=[]
for i in dic.values():
    b.append(i)
list=b
print(list)
m=0
j=0
while j<len(list): 
    if list[j]>m:
        m=list[j]
    j=j+1
print(m)
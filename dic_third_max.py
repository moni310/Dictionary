dic={"a":5,"b":26,"c":49,"d":88}
m=0
for i in dic:
    if dic[i]>m:
        m=dic[i]
max1=m
n=0
for j in dic:
    if dic[j]>n and dic[j]<max1:
        n=dic[j]
max2=n
max3=0
for a in dic:
    if dic[a]>max3 and dic[a]<max1 and dic[a]<max2:
        max3=dic[a]
print(max3)


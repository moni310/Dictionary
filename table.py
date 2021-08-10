i=1
b = {}
num=int(input("enter the number"))
while i<=num:
    j=1
    em=[]
    while j<=10:
        m=i*j
        em.append(m)
        j=j+1
    b[i] = em
    i=i+1
print(b)

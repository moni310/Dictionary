dic={"bijender":45,"deepak":60,"param":20,"anjali":30,"roshini":50}
b=sorted(dic.values())
em=[]
for i in dic.keys():
    em.append(i)
list=em
print(dict(zip(em,b)))
    


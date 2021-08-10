dic1 = {'a': 100, 'b': 200, 'c':300}
dic2 = {'a': 300, 'b': 200, 'd':400}
for i in dic1:
    if i in dic2:
        dic1[i]=dic2[i]+dic1[i]
dic2.update(dic1)
print(dic2)
dic={"V":"S001", "V": "S002", "VI": "S001","VI": "S005", "VII":"S005", "V":"S009","VIII":"S007"}
d=[]
for i in dic.values():
    if i not in d:
        d.append(i)
print(d)
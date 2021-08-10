list=[6,6,5,4,5,1,2,1,2]
empty=[]
i=0
for i in list:
    if i not in empty:
        empty.append(i)
print(empty)


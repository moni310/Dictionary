empty=[]
empty1=[]   
for i in range(1,11):
    student=input("enter the students name:")
    empty.append(student)
    marks=int(input("enter your marks:"))
    empty1.append(marks)
dic=dict(zip(empty,empty1))
print(dic)
    
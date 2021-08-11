text="mahinahizoyahi"
i=0
c=0
user=input("enter any alphabet:")
while i<len(text):
    j=0
    while j<len(text[i]):
        m=text[i][j]
        if m==user:
            c=c+1
        j=j+1
    i=i+1
print(user,c)

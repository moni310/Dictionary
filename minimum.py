list=[[3],[5,4,2],[5,2],[66,4,2,1]]
i=0
m=1
n=1
k=len(list)
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j]>m:
            m=list[i][j]
        if list[i][j]<n:
            n=list[i][j]
        j=j+1
    i=i+1
print(m,"maximum")
print(n,"minimum")



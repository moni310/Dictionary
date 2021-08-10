list=[[3],[5,4,2],[5,5,2,1,0,77,2],[66,4,2,1,0,8,9,7,6,9]]
i=0
m=[0]
while i<len(list):
    if len(list[i])>len(m):
        m=list[i]
    i=i+1
print("maximum list",m,"maximum length",len(m))

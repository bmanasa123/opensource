x=int(input())
c=1
for i in range(1,x+1):
    row=[]
    for j in range(i):
        row.append(c)
        c+=1
    print(" ".join(map(str,row)))

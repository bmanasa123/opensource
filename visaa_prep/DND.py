n,m=list(map(int,input().split()))
arr=list(map(int,input().split()))
x=[]
y=[]
for i in range(n):
    if arr[i]%m==0:
        x.append(arr[i])
    else:
        y.append(arr[i])
a=sum(x)
b=sum(y)
print(a-b)

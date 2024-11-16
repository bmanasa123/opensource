n=int(input())
arr=list(map(int,input().split()))
y=arr[0]
x=[]
for i in range(1,n):
    x.append(arr[i])
x.append(y)
print(" ".join(map(str,x)))

n=int(input())
x=[]
arr=list(map(int,input().split()))
for i in range(n):
    l=sum(arr[:i])
    r=sum(arr[i+1:])
    b=abs(l-r)
    x.append(b)
print(' '.join(map(str,x)))

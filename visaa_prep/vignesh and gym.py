x,y,z=list(map(int,input().split()))
m=x+y
if z>=m:
    print(2)
elif z>=x:
    print(1)
else:
    print(0)

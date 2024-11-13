x,y,z=list(map(int,input().split()))
a=x*y
b=z*1440
if b>=a:
    print("YES")
else:
    print("NO")

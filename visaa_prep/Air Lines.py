import math
x,y=list(map(int,input().split()))
z=x*100
s=y-z
if s>y:
    print("0")
else:
    a=math.ceil(s/100)
    print(a)

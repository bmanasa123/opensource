import math
n=int(input())
for _ in range(n):
    x,y=list(map(int,input().split()))
    a=(x/10)*y
    print(math.ceil(a))

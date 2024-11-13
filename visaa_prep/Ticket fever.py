n=int(input())
for _ in range(n):
    N,M=list(map(int,input().split()))
    x=N-M
    if x<0:
        print(0)
    else:
        print(x)

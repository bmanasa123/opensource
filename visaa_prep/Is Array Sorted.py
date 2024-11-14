n=int(input())
a=list(map(int,input().split()))
x=sorted(a)
if a==x:
    print("true")
else:
    print("false")

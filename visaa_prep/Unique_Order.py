def helo(arr):
    seen=set()
    unique=[]
    for num in arr:
        if num not in seen:
            unique.append(num)
            seen.add(num)
    return unique
N=int(input())
arr=list(map(int,input().split()))
re=helo(arr)
print(" ".join(map(str,re)))

n=int(input())
arr=list(map(int,input().split()))
unique_sum=sum(set(arr))
total=sum(arr)
single=2*unique_sum-total
print(single)

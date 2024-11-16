n=int(input())
arr=list(map(int,input().split()))
max_count=0
curr_count=0
for i in range(n):
    if arr[i]==0:
        curr_count+=1
        max_count=max(max_count,curr_count)
    else:
        curr_count=0
print(max_count)

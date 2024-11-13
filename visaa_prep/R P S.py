v,c=input().split()
if (v=='R' and c=='S') or (v=='S' and c=='P') or (v=='P' and c=='R'):
    print("Vignesh")
elif (v=='S' and c=='R') or (v=='P' and c=='S') or (v=='R' and c=='P'):
    print("Charan")
else:
    print("NULL")

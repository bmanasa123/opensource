n=int(input())
int_min=-2**31
int_max=2**31-1
sign=-1 if n<0 else 1
rev=str(abs(n))[::-1]
rev_int=sign*int(rev)
if int_min<=rev_int<=int_max:
    print(rev_int)
else:
    print("0")

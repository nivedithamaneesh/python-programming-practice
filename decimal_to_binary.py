n=int(input("enter any number:"))
bin=""
if n==0:
    bin="0"
else:
    while n>0:
        rem=n%2
        bin=str(rem)+bin
        n=n//2
print(bin)

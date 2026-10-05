n=int(input("enter any number:"))
oct=""
if n==0:
    oct="0"
else:
    while n>0:
        rem=n%8
        oct=str(rem)+oct
        n=n//8
print("octal:", oct)

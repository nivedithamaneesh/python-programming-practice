n= int(input("enter any number:"))
dec=0
place=1
while n>0:
    digit=n%10
    dec=dec+digit*place
    place=place*2
    n=n//10
print(dec)

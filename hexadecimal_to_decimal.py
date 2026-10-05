n=input("enter any hexadecimal").upper()
hex_digits="0123456789ABCDEF"
dec=0
place=1
for i in range (len(n)-1,-1,-1):
    digit=hex_digits.index(n[i])
    dec=dec+digit*place
    place=place*16
print(dec)

n=int(input("enter any number:"))
hex_digits="0123456789ABCDEF"
hexadecimal=""
if n==0:
    hexadecimal="0"
else:
    while n>0:
        rem=n%16
        hexadecimal=hex_digits[rem]+hexadecimal
        n=n//16
print(hexadecimal)

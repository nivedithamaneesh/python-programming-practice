price1=int(input("Enter the amount:"))
price2=int(input("Enter the amount:"))
price3=int(input("Enter the amount:"))
discount=0
cashback=0
delivery_charge=50
total=price1 + price2 + price3
if total>1000:
    discount=total*0.1
    total=total-discount
total=total+delivery_charge
if total>1000:
        cashback=100
        total=total-cashback
print("Original total:", price1 + price2 + price3)
print("Discount:", discount)
print("Delivery charge:", delivery_charge)
print("Cashback:", cashback)
print("Final amount:", total)

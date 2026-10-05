total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
medical = input("Do you have a medical certificate? (yes/no): ").lower()

attendance = (attended_classes / total_classes) * 100

print("Attendance:", attendance, "%")

if attendance >= 75:
    print("Eligible")
elif attendance >= 65 and medical == "yes":
    print("Eligible with medical relaxation")
else:
    print("Not eligible")

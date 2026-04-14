num = int(input("Enter any number: "))
if num % 2 == 0:
    print("Even number! ")
elif num % 2 == 1:
    print("Odd number! ")

user = input("Username: ")
password = int(input("Password: "))
if user == "admin" or "Admin" and password == 1234:
    print("Access granted")
else:
    print("Access denied")

score = int(input("Enter your score: "))
if score >= 70:
    print("A1")
elif score >= 60:
    print("B2")
elif score >= 50:
    print("C")
else:
    print("F")

age = int(input("Enter your age: "))
if age >= 18:
    print ("You can vote")
else:
    print("You are NOT eligible to vote")

age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

score = int(input("Enter your score: "))
if score >= 80:
    print("Excellent A1")
elif score >= 70:
    print("Good B2")
elif score >= 60:
    print("Good B3")
elif score >= 50:
    print("Pass")
else:
    print("Fail")


num = int(input("Enter a random number: "))
if num == 10:
    print("Perfect score! ")
else:
    print("Nice attempt! ")

age = int(input("Enter age: "))
country = input("Enter your country: ")
if age >= 18 and country == "Nigeria":
    print("You can vote in Nigeria")

age = int(input("Enter your age: "))
country = input("Are you a citizen? (Yes/No): ")
if age >= 18 and country == "Yes" or "yes":
    print("You ar eligible to vote")
else:
    print("You are NOT eligible to vote")



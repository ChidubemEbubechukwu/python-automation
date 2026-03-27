attempts = 0

while attempts < 5:
    user = input("Username: ")
    password = input("Password: ")

    if user == "admin" and password == "1234":
        print("Access granted")
        break
    else:
        print("Access denied")

    attempts += 1

if attempts == 5:
    print("Account locked")


print("Task 1")
for i in range(1,11):
    print(i)

print("Task 2")
count = 0
num = 1
while num != 0:
    num = int(input("Enter number(0 to stop): "))
    count += num
print("Sum of all numbers entered", count)


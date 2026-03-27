for i in range(5):
    print("Hello")

for i in range(1,6):
    print(i)

count = 1
while count <= 5:
    print(count)
    count += 1

count = 2
while count <= 16:
    print(count)
    count += 2

print("Example: ")
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted")

Username = ""
while Username != "Chidubem Ebubechukwu":
    Username = input("Enter Username: ")
print("Access granted")

for i in range(10):
    if i == 5:
        break
    count +=1
print(i)


for i in range(5):
    if i == 2 or 3:
        continue
    print(i)

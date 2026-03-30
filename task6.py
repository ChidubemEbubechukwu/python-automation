fruits = ["mango", "banana", "orange", "watermelon"]
print(fruits)

print(fruits[0])

fruits[1] = "apple"
print(fruits)

fruits.append ("grape")
print(fruits)

fruits.remove ("watermelon")
print(fruits)

for fruit in fruits:
    print(fruit)


names = []
for i in range(5):
    name = input("Enter a name: ")
    names.append(name)
print ("Names entered: ")

for name in names:
    print(name)

scores = []
for i in range(5):
    score = int(input("Enter score: "))
    scores.append(score)

print("All scores:", scores)
print("Total:", sum(scores))
print("Highest score:", max(scores))
print("Lowest score:", min(scores))

nums = []
for i in range(5):
    num = int(input("Enter number: "))
    nums.append(num)
print("Numbers entered: ",nums)


names =  []
for i in range(5):
    name = input("Enter name: ")
    names.append(name)
print("Names entered: ",names[::-1])

count = 0
num = 1
while num != 0:
    num =  int(input("Enter Number: "))
    nums.append(num)
    break
print ("All numbers: ", num)
print("Total: ",sum(num))
print("Highest number: ", max(num))
print("Lowest number: ", min(num))
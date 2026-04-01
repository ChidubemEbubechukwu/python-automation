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
for i in range(3):
    name = input("Enter a name: ")
    names.append(name)
print ("Names entered: ")

for name in names:
    print(name)

scores = []
for i in range(3):
    score = int(input("Enter score: "))
    scores.append(score)

print("All scores:", scores)
print("Total:", sum(scores))
print("Highest score:", max(scores))
print("Lowest score:", min(scores))

nums = []
for i in range(3):
    num = int(input("Enter number: "))
    nums.append(num)
print("Numbers entered: ",nums)


names =  []
for i in range(3):
    name = input("Enter name: ")
    names.append(name)
print("Names entered: ",names[::-1])

nums = []
num = 1

while num != 0:
    num =  int(input("Enter Number(0 to stop): "))
    
    if num != 0:
        nums.append(num)

print ("All numbers: ", nums)

if len(nums) > 0:
       print("Total: ",sum(nums))
       print("Highest number: ", max(nums))
       print("Lowest number: ",  min(nums))

<<<<<<< HEAD


=======
>>>>>>> 8faefbc (Week 1 Day 6: Learned lists and loops with input handling, number storage, and analysis)
else:
    print("No numbers entered!") 
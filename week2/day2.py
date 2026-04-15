# WEEK 2 DAY 2 - FUNCTIONS & AUTOMATION

def greet_user():
    name = input("Enter your name: ")
    print(f"Welcome, {name}!")

def add_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Total = {num1 + num2}")
    print(f"Difference = {num1 - num2}")
    print(f"Multiplication = {num1 * num2}")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Greet User")
        print("2. Add Numbers")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            greet_user()
        elif choice == "2":
            add_numbers()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
#Run code            
menu()


print("Class work")
def greet_user():
    name = input("Enter name: ")
    print(f"Welcome, {name}!")

def show_info():
    name = input("Enter name: ")
    print(f"My name is {name}")
    print("I am learning Python")

def subtract_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Difference = {num1 - num2}")

def multiply_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"Multiplication = {num1 * num2}")

def divide_numbers():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    if num2 == 0:
        print("Cannot divide by ZERO")
    else:
        print(f"Division = {num1 / num2}")
    
def menu():
    while True:
        print("\n -----Menu-----")
        print("1. Hello User")
        print("2. Difference")
        print("3. Product")
        print("4. Division")
        print("5. Show Info")
        print("6. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            greet_user()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            multiply_numbers()
        elif choice == "4":
            divide_numbers()
        elif choice == "5":
            show_info()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, Try again!")
menu()     
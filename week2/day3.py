# WEEK 2 DAY 3 - FILE HANDLING

file = open("data.txt", "w")
file.write("Hello, this is my first file!\n")
file.close()

print("Data written successfully!")

file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

import datetime
def save_user():
    name = input("Enter your name: ")
    date = datetime.date.today()

    
    file = open("users.txt", "a")
    file.write(name + "-" + str(date) + "\n")
    file.close()
    
    print("User saved!")

def view_users():
    try:
        file = open("users.txt", "r")
        content = file.read()
        file.close()

        print("\nSaved Users:")

        lines = content.split("\n")

        count = 1
        for name in lines:
            if name != "":
                print(f"{count}. {name}")
                count += 1

    except:
        print("No users yet")

def clear_users():
    file = open("users.txt", "w")
    file.close()

    print("Users cleared")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Save User")
        print("2. View Users")
        print("3. Exit")
        print("4. Clear Users")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            save_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            print("Goodbye!")
            break
        elif choice == "4":
            clear_users()
            break
        else:
            print("Invalid choice")

menu()
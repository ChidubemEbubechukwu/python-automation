from datetime import date

FILE_NAME = "automation_users.txt"


# Save user
def save_user():
    name = input("Enter user name: ")
    today = date.today()

    with open(FILE_NAME, "a") as file:
        file.write(f"{name} - {today}\n")

    print("User saved!")


# View users
def view_users():
    try:
        with open(FILE_NAME, "r") as file:
            print("\n--- Users List ---")

            for i, line in enumerate(file, start=1):
                print(f"{i}. {line.strip()}")

    except FileNotFoundError:
        print("No users found.")


# Search user
def search_user():
    name = input("Enter name to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for line in file:
                if name.lower() in line.lower():
                    print("Found:", line.strip())
                    found = True

            if not found:
                print("User not found.")

    except FileNotFoundError:
        print("No users found.")


# Count users
def count_users():
    try:
        with open(FILE_NAME, "r") as file:
            count = sum(1 for line in file if line.strip() != "")

        print(f"Total users: {count}")

    except FileNotFoundError:
        print("No users found.")


# Remove duplicates
def remove_duplicates():
    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        unique = list(set(lines))

        with open(FILE_NAME, "w") as file:
            file.writelines(unique)

        print("Duplicates removed.")

    except FileNotFoundError:
        print("No users found.")


# Menu
def menu():
    while True:
        print("\n--- AUTOMATION MENU ---")
        print("1. Save User")
        print("2. View Users")
        print("3. Search User")
        print("4. Count Users")
        print("5. Remove Duplicates")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            save_user()
        elif choice == "2":
            view_users()
        elif choice == "3":
            search_user()
        elif choice == "4":
            count_users()
        elif choice == "5":
            remove_duplicates()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


menu()
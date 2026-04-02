numbers = []
while True:
    print("1. Add number")
    print("2. View numbers")
    print("3. Show Total")
    print("4. Show Max/Min")
    print("5. Show Average")
    print("6. Exit")

    choice = input("Enter choice: ").strip()
    
    if choice == "1":
        try:
            num = int(input("Enter Number: "))
            numbers.append(num)
        except:
            print("Invalid choice, please enter number")
    
    
    elif choice == "2":
        if numbers:
            print("Numbers: ",numbers)
        else:
            print("No numbers yet")
    
    elif choice == "3":
        if numbers:
            print("Total: ",sum(numbers))
        else:
            print("No numbers yet")

    elif choice == "4":
        if numbers:
            print("Highest number: ",max(numbers))
            print("Lowest number: ",min(numbers))
        else:
            print("No numbers yet")
    
    elif choice == "5":
        if numbers:
            print("Average:", sum(numbers)/len(numbers))
        else:
            print("No numbers yet")
        
    elif choice == "6":
        confirm = input("Confirm choice(yes/no): ")
        if confirm.lower() == "yes":
            print("Goodbye!")
            break
        else:
            print("Cancelled")
    
    else:
        print("Invalid choice")
        
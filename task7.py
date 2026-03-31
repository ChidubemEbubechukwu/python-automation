numbers = []
while True:
    print("\n1. Add number")
    print("2. View numbers")
    print("3. Show total")
    print("4. Show Max/Min")
    print("5. Average")
    print("6. Clear all numbers")
    print("7. Exit")
    
    choice = input("Enter choice: ").strip()
    
    if choice == "1":
        num = int(input("Enter number: "))
        numbers.append(num)

    elif choice == "2":
        print("Numbers", numbers)
    
    elif choice == "3":
        print("Total: ", sum(numbers))
    
    elif choice == "4":
        if len(numbers) > 0:
            print("Max: ", max(numbers))
            print("Min: ", min(numbers))
        else:
            print("No numbers yet!")
    
    elif choice == "5":
        print("Average :", sum(numbers)/len (numbers))
        if len(numbers) == 0:
            print("No numbers yet!")
    
    elif choice == "6":
        confirm = input("Are you sure? (yes/no): ")
        if confirm.lower() == "yes":
            numbers.clear()
            print("All numbers cleared")
        else:
            print("Cancelled")

    elif choice == "7":
        confirm = input("Are you sure ?(yes/no): ")
        if confirm.lower() == "yes":
            print("Goodbye!")
            break
        else:
            print("Cancelled")
        
        
    else:
        print('Invalid choice')
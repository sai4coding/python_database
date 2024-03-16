people = {'sai': 22, 'teja': 21, 'ganesh': 23}


def intro():
    print("Hello, welcome to the database!\n")
    print("Enter your password to continue.")
    enter_password()


def enter_password():
    password = 'python123'
    entry1 = input("Enter password: ")

    if len(entry1) < 3 or entry1 != password:
        print('Access denied.')
    else:
        print('Welcome!')
        data_base()


def data_base():
    while True:  # Loop for continuous interaction
        print("\nAvailable options:")
        print("1. Clear database")
        print("2. Update database")
        print("3. Print database")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            clear_database()
        elif choice == 2:
            update_dictionary()
        elif choice == 3:
            print_database()
        elif choice == 4:
            print("Exiting database.")
            break
        else:
            print("Invalid choice. Please try again.")


def clear_database():
    confirmation = input("Are you sure you want to clear the database? (y/n): ")
    if confirmation.lower() == 'y':
        people.clear()
        print("Database cleared.")
    else:
        print("Database remains unchanged.")


def update_dictionary():
    while True:
        action = input("Add (a) or Remove (r) an entry? (a/r/q to quit): ")

        if action.lower() == 'a':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            people[name] = age
            print(people)
        elif action.lower() == 'r':
            name = input("Enter name to remove: ")
            if name in people:
                del people[name]
                print(people)
            else:
                print("Name not found in database.")
        elif action.lower() == 'q':
            break
        else:
            print("Invalid action. Please try again.")


def print_database():
    if people:
        print("Current database:")
        for name, age in people.items():
            print(f"{name}: {age}")
    else:
        print("Database is empty.")


intro()

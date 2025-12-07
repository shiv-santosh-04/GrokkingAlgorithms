phone_book = {}

while True:
    print("1. Add New Contact")
    print("2. Search Contact")
    print("3. Exit")
    choice = input("Enter the choice ")
    if choice == "1":
        name = input("Enter the name:").strip()
        number = input("Enter the number:").strip()

        phone_book[name] = number

    elif choice == "2":
        search = input("Enter the name of contact to be searched:").strip()

        if search in phone_book:
            print(f"contact {search} number:{phone_book[search]}")

    elif choice == "3":
        print("Exiting")
        break
    else:
        print("Invalid Choice")
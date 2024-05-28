def price():
    # List of products
    laptops = [
        {"name": "Laptop Asus ram 16", "price": 1000},
        {"name": "Laptop hp ram 16", "price": 1200}
    ]
    
    Computers = [
        {"name": "computers gigabyte ram 16", "price": 800},
        {"name": "computers gigabyte ram 32", "price": 900}
    ]

    while True:
        # Display main menu
        print("Please choose:")
        print("1. Laptop")
        print("2. Computers")
        print("3. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            # Display laptop options
            print("Available laptops:")
            for i, laptop in enumerate(laptops):
                print(f"{i + 1}. {laptop['name']} - ${laptop['price']}")

            laptop_choice = int(input("Please select an option: ")) - 1
            if 0 <= laptop_choice < len(laptops):
                print(f"You selected {laptops[laptop_choice]['name']} with a price of ${laptops[laptop_choice]['price']}.")
            else:
                print("Invalid choice!")

        elif choice == "2":
            # Display desktop options
            print("Available Computers:")
            for i, desktop in enumerate(Computers):
                print(f"{i + 1}. {desktop['name']} - ${desktop['price']}")

            desktop_choice = int(input("Please select an option: ")) - 1
            if 0 <= desktop_choice < len(Computers):
                print(f"You selected {Computers[desktop_choice]['name']} with a price of ${Computers[desktop_choice]['price']}.")
            else:
                print("Invalid choice!")

        elif choice == "3":
            # Exit the program
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    price()

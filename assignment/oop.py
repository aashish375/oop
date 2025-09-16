

class listing:
    def __init__(self, address, price, bedrooms, bathrooms, sqft):
        self.address = address
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.sqft = sqft

    def __str__(self):
        return (f"Address: {self.address}\n"
                f"Price: ${self.price:,.2f}\n"
                f"Bedrooms: {self.bedrooms}\n"
                f"Bathrooms: {self.bathrooms}\n"
                f"Sq. Ft.: {self.sqft}\n")

def main():
    all_listings = [
        listing("1234 Main St, Anytown, USA", 350000.00, 3, 2, 1800),
        listing("5678 Oak Ln, Suburbia, USA", 275000.00, 4, 3, 2200),
        listing("9101 Pine Rd, Countryside, USA", 425000.00, 5, 4, 2800)
    ]

    while True:
        print("\nWelcome to the House Flipper CLI.")
        print("1. See all listings")
        print("2. Check a specific listing's details")
        print("3. Buy a house")
        print("4. Add a new listing")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print("\n--- Available Listings ---")
            if not all_listings:
                print("No listings right now.")
            else:
                for i, house in enumerate(all_listings):
                    print(f"--- Listing #{i+1} ---")
                    print(house)
        
        elif choice == '2':
            try:
                list_num = int(input("Enter the number of the listing to view: "))
                if 1 <= list_num <= len(all_listings):
                    print("\n--- Listing Details ---")
                    print(all_listings[list_num - 1])
                else:
                    print("That listing number doesn't exist.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '3':
            try:
                list_num = int(input("Enter the number of the listing to purchase: "))
                if 1 <= list_num <= len(all_listings):
                    purchased_house = all_listings.pop(list_num - 1)
                    print(f"\nYou just bought the house at {purchased_house.address}.")
                    print("It's no longer listed.")
                else:
                    print("That listing number doesn't exist.")
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '4':
            print("\n--- Adding a New Listing ---")
            try:
                address = input("Enter the address: ")
                price = float(input("Enter the price: "))
                bedrooms = int(input("Enter the number of bedrooms: "))
                bathrooms = int(input("Enter the number of bathrooms: "))
                sqft = int(input("Enter the square footage: "))

                new_listing = listing(address, price, bedrooms, bathrooms, sqft)
                all_listings.append(new_listing)
                print(f"\nListing for {address} has been added.")
            except ValueError:
                print("Something went wrong. Ensure you're entering numbers where needed.")

        elif choice == '5':
            print("Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



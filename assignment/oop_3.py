
class Listing:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name.strip() != "":
            self.__name = new_name
        else:
            print("Name can't be empty.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_priceS
        else:
            print("Price must be more than zero.")

    def __str__(self):
        return f"Item: {self.__name}\nPrice: ${self.__price:,.2f}"


# subclasses
class HouseListing(Listing):
    def __init__(self, name, price, beds, baths, sqft):
        super().__init__(name, price)
        self.__beds = beds
        self.__baths = baths
        self.__sqft = sqft

    def __str__(self):
        return (super().__str__() +
                f"\nBedrooms: {self.__beds}\n"
                f"Bathrooms: {self.__baths}\n"
                f"Sqft: {self.__sqft}\n")


class FurnitureListing(Listing):
    def __init__(self, name, price, material, cond):
        super().__init__(name, price)
        self.__material = material
        self.__cond = cond

    def __str__(self):
        return (super().__str__() +
                f"\nMaterial: {self.__material}\n"
                f"Condition: {self.__cond}\n")


class PerishableListing(Listing):
    def __init__(self, name, price, exp_date, weight):
        super().__init__(name, price)
        self.__exp_date = exp_date
        self.__weight = weight

    def __str__(self):
        return (super().__str__() +
                f"\nExpires: {self.__exp_date}\n"
                f"Weight: {self.__weight} lbs\n")


def main():
    listings = [
        HouseListing("1234 Main St", 350000, 3, 2, 1800),
        FurnitureListing("Oak Dining Table", 450, "Wood", "Good"),
        PerishableListing("Milk Carton", 3.50, "2025-09-25", 1)
    ]

    while True:
        print("\n--- Marketplace Menu ---")
        print("1. Show all listings")
        print("2. View a listing")
        print("3. Buy something")
        print("4. Add listing")
        print("5. Quit")

        choice = input("Pick (1-5): ")

        if choice == "1":
            if not listings:
                print("Nothing is listed right now.")
            else:
                for i, item in enumerate(listings, start=1):
                    print(f"\nListing #{i}")
                    print(item)

        elif choice == "2":
            try:
                num = int(input("Which listing number? "))
                if 1 <= num <= len(listings):
                    print(listings[num - 1])
                else:
                    print("That number doesn't exist.")
            except ValueError:
                print("Enter a number.")

        elif choice == "3":
            try:
                num = int(input("Which listing do you want to buy? "))
                if 1 <= num <= len(listings):
                    bought = listings.pop(num - 1)
                    print(f"You bought: {bought.name}. It’s gone now.")
                else:
                    print("Not a valid number.")
            except ValueError:
                print("Enter a number.")

        elif choice == "4":
            print("What type of listing?")
            print("1 = House, 2 = Furniture, 3 = Perishable")
            try:
                t = int(input("Enter choice: "))
                if t == 1:
                    n = input("Address: ")
                    p = float(input("Price: "))
                    b = int(input("Bedrooms: "))
                    ba = int(input("Bathrooms: "))
                    s = int(input("Sqft: "))
                    listings.append(HouseListing(n, p, b, ba, s))
                elif t == 2:
                    n = input("Name: ")
                    p = float(input("Price: "))
                    m = input("Material: ")
                    c = input("Condition: ")
                    listings.append(FurnitureListing(n, p, m, c))
                elif t == 3:
                    n = input("Name: ")
                    p = float(input("Price: "))
                    e = input("Expiration date: ")
                    w = float(input("Weight (lbs): "))
                    listings.append(PerishableListing(n, p, e, w))
                else:
                    print("Invalid type.")
            except ValueError:
                print("Bad input.")

        elif choice == "5":
            print("Bye.")
            break
        else:
            print("Not a valid option.")


if __name__ == "__main__":
    main()

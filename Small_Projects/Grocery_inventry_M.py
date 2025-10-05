# Q3. Grocery Inventory Management
# 👉 Problem:
# Each grocery item should be stored like this:

# {
#    "item_id": 1,
#    "name": "Rice",
#    "category": "Grains",
#    "stock": {
#        "quantity": 50,
#        "unit": "kg",
#        "price_per_unit": 60
#    }
# }
# Allow user to add new items.
# Update stock when something is sold.
# Show total value of stock (quantity × price).
# Save data into inventory.json.
# --------------------------------------------------------------------------------------

# from Small_ThingsPy import FormatData as GMS

import sys
sys.path.append(r"c:\Users\Mahadeb Maity\OneDrive\Python\Beginners_Python\Python")

from Small_ThingsPy import FormatData as GMS

def admin_menu():
    print("=== Admin Access ===")
    # Your admin logic here
    GMS.greetings()
    GMS.Main()

def staff_menu():
    print("=== Staff Access ===")
    # Your staff logic here
    print("1. Update Stock")
    print("2. Check Inventory")


def customer_menu():
    print("=== Customer Access ===")
    # Your customer logic here
    print("1. View Products")
    print("2. Buy Product")

def main():
    while True:
        print("\n===== Grocery Management System =====")
        print("1. Admin Access")
        print("2. Staff Access")
        print("3. Customer Access")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            staff_menu()
        elif choice == "3":
            customer_menu()
        elif choice == "4":
            print("Exiting System... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
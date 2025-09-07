import importlib

try:
    _tabulate_mod = importlib.import_module("tabulate")
    tabulate = getattr(_tabulate_mod, "tabulate")
except Exception:
    # Lightweight fallback for tabulate to avoid requiring the external package.
    # It supports basic headers and grid-like ASCII output used by this script.
    def tabulate(rows, headers=None, tablefmt=None):
        # Convert all cells to strings
        data_rows = [list(map(str, r)) for r in rows]
        header_row = list(map(str, headers)) if headers else None

        # Build full table data including header if present
        if header_row:
            data = [header_row] + data_rows
        else:
            data = data_rows

        if not data:
            return ""

        # Transpose to compute column widths
        cols = list(zip(*data))
        widths = [max(len(str(item)) for item in col) for col in cols]

        def format_row(row):
            return "| " + " | ".join(str(cell).ljust(widths[i]) for i, cell in enumerate(row)) + " |"

        sep = "+-" + "-+-".join("-" * w for w in widths) + "-+"

        lines = [sep]
        if header_row:
            lines.append(format_row(data[0]))
            lines.append(sep)
            for row in data[1:]:
                lines.append(format_row(row))
            lines.append(sep)
        else:
            for row in data:
                lines.append(format_row(row))
            lines.append(sep)

        return "\n".join(lines)

import shutil
import json
import os

def greetings():
    Headings = shutil.get_terminal_size().columns
    print("Welcome".center(Headings, "*"))
    print("Grocery Inventory System".center(Headings, "*"))

def options():
    print("\n===== INVENTORY MENU =====")
    print("1. 🛒  Add Item")
    print("2. 📋  Display Items")
    print("3. ✏️   Update Items")
    print("4. ❌  Delete Items")
    print("5. ↩️   Undo Deleted Items")
    print("6. 🔍 Search Items")
    print("7. 💾  Save & Exit")

def show_menu(title, options):
    """
    Display a numbered menu from a list of options.
    Returns the selected option or None if invalid.
    """
    print(f"\n===== {title} =====")
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("\nEnter your choice number: ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(options):
        return options[int(choice) - 1]
    elif choice == '':
        return "kg"
    else:
        print("⚠️ Invalid choice! Please try again.")
        return None

def update_quantity_with_unit(units, Quantity_unit,old_qty):
    unit = show_menu(f"UNIT SELECTION {Quantity_unit}", units)
    print(f"\n👉 You selected unit: {unit}")

    if unit:
        qty = input(f"Enter Quantity in {unit} (leave blank to keep same): ").strip()
        
        if qty:  # user entered a number
            new_qty = f"{qty} {unit}"
        else:    # user pressed Enter → keep old quantity
            new_qty = old_qty
    else:
        return old_qty   # no unit selected → return old quantity

    return new_qty


def get_numeric_input(Price, min_value=0):
    """
    Safely get numeric input from the user.
    
    Arguments:
    prompt (str): The message shown to the user.
    min_value (float): Minimum allowed value (default is 0).
    
    Returns:
    float: A valid numeric input from the user.
    """
    while True:
        try:
            value = float(Price)  # accepts int or float
            if value < min_value:
                print(f"⚠️ Value cannot be less than {min_value}. Try again.")
                continue
            return value
        except ValueError:
            print("⚠️ Invalid input! Please enter a numeric value.")


def StoreData():
    # Load existing inventory (if any)
    try:
        with open("Results/Inventory.json", "r") as file:
            Inventory = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        Inventory = {}

    # Next ID (robust even if IDs aren't contiguous)
    next_id = (max((item["ID"] for item in Inventory.values()), default=0) + 1)

    new_items = 0  # track how many items are added this session

    while True:
        raw = input("Enter Grocery Item Name:(or 'stop' & 'Enter' to Finish!)=> ").strip()
        if raw.lower() in ("stop", ""):
            # If user finished immediately with no additions -> don't save anything
            if new_items == 0:
                print("⚠ No items added. Nothing saved.")
                return
            else:
                break  # we added something; proceed to save

        # normalize product name after validation
        Product = raw.title()
        
        # price (as number)
        price = get_numeric_input(input(f"Enter price of {Product}: ").strip())

        # unit handling
        units = ["mg", "g", "kg", "quintal", "ton",
                        "ml", "liter", "gallon", "cup", "tsp", "tbsp",
                        "packet", "box", "carton", "bottle", "jar", "can", "pouch", "sachet", "bag",
                        "piece", "dozen", "pair", "petti", "chain",
                        "bundle", "bunch", "sack", "barrel", "drum"]
        
        Default = "kg" 
        Quantity_unit = f"For {Product}"
        Product_Weight_unit = update_quantity_with_unit(units,Quantity_unit,Default)
        
        # parts = str(Product_Weightunit).split(maxsplit=1)
        # if len(parts) == 2:
        #     Product_Weight_unit = parts[1]   # "petties"
        # else:
        #     Product_Weight_unit = ""


        # if Product_Weight_unit in ("kg", "quintal"):
        #     # qty = int(input(f"Enter Quantity of {Product} in {Product_Weight_unit}: "))
        #     Quantity = f"{Product_Weightunit}"
        # else:
        #     # qty = int(input(f"Enter how many {Product_Weight_unit} of {Product}: "))
            # Quantity = f"{Product_Weightunit}"
        Quantity = f"{Product_Weight_unit}"
        # If product already exists, update it while keeping its ID
        if Product in Inventory:
            existing_id = Inventory[Product]["ID"]
            Inventory[Product] = {"ID": existing_id, "price": price, "Quantity": Quantity}
        else:
            Inventory[Product] = {"ID": next_id, "price": price, "Quantity": Quantity}
            next_id += 1

        new_items += 1

    # Save only if we actually added something
    os.makedirs("Results", exist_ok=True)
    with open("Results/Inventory.json", "w") as file:
        json.dump(Inventory, file, indent=4)

    print(f"✅ Data Saved Successfully! ({new_items} item(s) added)")

def Display_Product():
    try:
        with open("Results/Inventory.json", "r") as file:
            Inventory = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("⚠ No inventory found. Please add items first.")
        return

    if not Inventory:
        print("⚠ Inventory is empty. Please add items first.")
        return

    # Build rows and sort by ID for stable display
    rows = []
    for product, details in Inventory.items():
        rows.append([details["ID"], product, details["price"], details["Quantity"]])
    rows.sort(key=lambda r: r[0])

    print("\nInventory List:")
    print(tabulate(rows, headers=["ID", "Product", "Price", "Quantity"], tablefmt="grid"))



def update_product():
    try:
        with open("Results/Inventory.json", "r") as file:
            inventory = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("⚠ No inventory found. Please add items first.")
        return
    if not inventory:
        print("⚠ Inventory is empty. Please add items first.")
        return


    try:
        Name = input("Enter Product Name to update: ").title()
        if Name in inventory:
            print("\nCurrent Details:", inventory[Name])

            # Ask for new values (press Enter to keep old one)
            # --- Handle Price ---
            new_price = input(f"Enter new price of {Name} (leave blank to keep same): ").strip()
            if new_price:
                inventory[Name]["price"] = int(new_price)
            # unit handling
            units = ["mg", "g", "kg", "quintal", "ton",
                        "ml", "liter", "gallon", "cup", "tsp", "tbsp",
                        "packet", "box", "carton", "bottle", "jar", "can", "pouch", "sachet", "bag",
                        "piece", "dozen", "pair", "petti", "chain",
                        "bundle", "bunch", "sack", "barrel", "drum"]

            # new_qty = update_quantity_with_unit()

            # --- Handle Quantity & Unit ---
            old_qty = inventory[Name]["Quantity"]   
            parts = old_qty.split(maxsplit=1)
            if len(parts) == 2:
                old_unit = parts[1]   # "petties"
            else:
                old_unit = ""         
            print(f"Old Unit: {old_unit}")

            Quantity_unit = f" For Changing {Name} unit Instead Off {old_unit}"
            new_qty = update_quantity_with_unit(units,Quantity_unit,old_unit)
            print(f"Current Quantity : {new_qty}")
            inventory[Name]["Quantity"] = new_qty

            print("\n✅ Product updated successfully!")
            print(f"Updated Details of {Name} : {inventory[Name]}")
        else:
            print("❌ Product not found!")

    except ValueError:
        print("⚠️ Invalid input! Please enter correct values.")


    with open("Results/Inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)


# def Delete_Product():
#     # Load Restore_items.json safely
#     Restore_file = "Results/Restore_items.json"
#     if os.path.exists(Restore_file) and os.path.getsize(Restore_file) > 0:
#         with open(Restore_file, "r") as file:
#             try:
#                 Restore_items = json.load(file)
#             except json.JSONDecodeError:
#                 Restore_items = {}
#     else:
#         Restore_items = {}

#     # Load inventory safely
#     inventory_file = "Results/inventory.json"
#     if os.path.exists(inventory_file) and os.path.getsize(inventory_file) > 0:
#         with open(inventory_file, "r") as file:
#             try:
#                 Inventory = json.load(file)
#             except json.JSONDecodeError:
#                 Inventory = {}
#     else:
#         Inventory = {}

#     if not Inventory:
#         print("⚠️ Inventory is empty. Nothing to delete.")
#         return

#     # Let user delete multiple items at once
#     product_names = input(
#         "Enter product name(s) to delete (separate multiple items with commas): "
#     ).split(",")
#     product_names = [name.strip().title() for name in product_names if name.strip()]

#     # Dictionary to store deleted items for undo
#     restore_items = {}

#     for product_name in product_names:
#         if product_name in Inventory:
#             confirm = input(f"Are you sure you want to delete '{product_name}'? (yes/no): ").lower()
#             if confirm == "yes":
#                 restore_items[product_name] = Inventory[product_name]
#                 del Inventory[product_name]
#                 print(f"✅ '{product_name}' deleted successfully! You can undo this action.")
#             else:
#                 print(f"❌ Deletion of '{product_name}' cancelled.")
#         else:
#             print(f"⚠️ '{product_name}' not found in Inventory.")

    
#     if restore_items:
#         os.makedirs("Results", exist_ok=True)
#         with open(Restore_file, "w") as file:
#             json.dump(restore_items, file, indent=4)
#         print("📂 Deleted items saved for undo.")
#         with open(inventory_file, "w") as file:
#             json.dump(Inventory, file, indent=4)
#         print("📂 Inventory updated successfully and saved for undo.")
#     else:
#         print("⚠️ No items were deleted.")

def Delete_Product():
    Restore_file = "Results/Restore_items.json"
    inventory_file = "Results/inventory.json"

    # Load Restore_items.json safely
    if os.path.exists(Restore_file) and os.path.getsize(Restore_file) > 0:
        with open(Restore_file, "r") as file:
            try:
                restore_items = json.load(file)
            except json.JSONDecodeError:
                restore_items = {}
    else:
        restore_items = {}

    # Load inventory safely
    if os.path.exists(inventory_file) and os.path.getsize(inventory_file) > 0:
        with open(inventory_file, "r") as file:
            try:
                Inventory = json.load(file)
            except json.JSONDecodeError:
                Inventory = {}
    else:
        Inventory = {}

    if not Inventory:
        print("⚠️ Inventory is empty. Nothing to delete.")
        return

    # Let user delete multiple items at once
    product_names = input(
        "Enter product name(s) to delete (separate multiple items with commas): "
    ).split(",")
    product_names = [name.strip().title() for name in product_names if name.strip()]

    # Temporary dict for this delete session
    session_deleted = {}

    for product_name in product_names:
        if product_name in Inventory:
            confirm = input(f"Are you sure you want to delete '{product_name}'? (yes/no): ").lower()
            if confirm == "yes":
                session_deleted[product_name] = Inventory[product_name]
                del Inventory[product_name]
                print(f"✅ '{product_name}' deleted successfully! You can undo this action.")
            else:
                print(f"❌ Deletion of '{product_name}' cancelled.")
        else:
            print(f"⚠️ '{product_name}' not found in Inventory.")

    # Save only if something deleted
    if session_deleted:
        # merge with old restore_items
        restore_items.update(session_deleted)

        os.makedirs("Results", exist_ok=True)
        with open(Restore_file, "w") as file:
            json.dump(restore_items, file, indent=4)

        with open(inventory_file, "w") as file:
            json.dump(Inventory, file, indent=4)

        print("📂 Deleted items saved for undo.")
        print("📂 Inventory updated successfully.")
    else:
        print("⚠️ No items were deleted.")


def Undo_Delete():
    inventory_file = "Results/inventory.json"
    restore_file = "Results/Restore_items.json"

    # Step 1: Load current inventory
    if os.path.exists(inventory_file) and os.path.getsize(inventory_file) > 0:
        with open(inventory_file, "r") as file:
            inventory = json.load(file)
    else:
        inventory = {}

    # Step 2: Load items to restore
    if os.path.exists(restore_file) and os.path.getsize(restore_file) > 0:
        with open(restore_file, "r") as file:
            try:
                restore_items = json.load(file)
            except json.JSONDecodeError:
                restore_items = {}
    else:
        restore_items = {}

    # Step 3: Move restore_items back into inventory
    if restore_items:
        inventory.update(restore_items)

        # Save updated inventory
        with open(inventory_file, "w") as file:
            json.dump(inventory, file, indent=4)

        # Clear restore file after undo
        with open(restore_file, "w") as file:
            json.dump({}, file)

        print(f"♻️ Undo successful! Restored '{restore_items}'.")
        print(f"✅ Restored {len(restore_items)} item(s) back into inventory!")

        rows = []
        for product, details in restore_items.items():
            rows.append([details["ID"], product, details["price"], details["Quantity"]])
        rows.sort(key=lambda r: r[0])

        print("\n Restored items List:")
        print(tabulate(rows, headers=["ID", "Product", "Price", "Quantity"], tablefmt="grid"))
    else:
        print("⚠️ No items available to restore.")


def search_item():
    if not os.path.exists("Results/inventory.json"):
        print("⚠ Inventory file not found!")
        return

    with open("Results/inventory.json", "r") as file:
        try:
            inventory = json.load(file)
        except json.JSONDecodeError:
            print("⚠ Inventory is empty or corrupted!")
            return

    if not inventory:
        print("⚠ Inventory is empty.")
        return

    item_name = input("🔎 Enter product name to search: ").strip().title()

    # Normalize keys (since JSON keys are case sensitive)
    product_keys = {key.title(): key for key in inventory.keys()}

    if item_name in product_keys:
        actual_key = product_keys[item_name]  # get original key
        details = inventory[actual_key]

        headers = ["Product", "ID", "Price", "Quantity"]
        row = [[actual_key, details.get("ID", ""), details.get("price", ""), details.get("Quantity", "")]]
        
        print(tabulate(row, headers=headers, tablefmt="grid"))
    else:
        print("❌ Item not found in inventory.")


def Choice_validation():
    while True:
        Choice = input("Enter your choice!(Press 'Enter' to Exit!) => ").strip()
        if Choice == "":
            exit()
        return Choice

def Main():
    while True:
        options()
        Choice = Choice_validation()

        if Choice == "1":
            print("Now Adding Items...! ")
            StoreData()
        elif Choice == "2":
            print("Display items...!")
            Display_Product()
        elif Choice == "3":
            print("Updating...!")
            update_product()
        elif Choice == "4":
            print("Proccesing to Delete Product...!")
            Delete_Product()
        elif Choice == "5":
            print("Processing Undo...!")
            Undo_Delete()
        elif Choice == "6":
            print("Items Searching...\nPlease Wait Sometimes!")
            search_item()
        elif Choice == "7":
            print("Thank You!")
            exit()
        else:
            print("Invalid Input! Please Enter within a Given numbers!")

if __name__ == "__main__":
    greetings()
    Main()


# Hostel rent calculate
'''
## We need input from user: 
Total rent
Total food order for snacking
Electricity Bill units spend 
Charge per unit
person living in room /flat
##Output:
Total amount you have to pay
'''
'''
rent = float(input("Enter Your Hostel/flat rent = "))
food = float(input("Enter the amount of food order = "))
Electricity_spend = float(input("Enter the Total of electricity spend = "))
Charge_per_unit = float(input("Enter the charge per unit = "))
persons = float(input("Enter the total number of person living in a room/flat = "))

total_bill = Electricity_spend * Charge_per_unit
output = (food + rent + total_bill) // persons
print(f"Each person will pay = {output}")
'''
# -------------------------------------------------------------
# New Rental System 
from tabulate import tabulate
def Rental_system():
    print("--------Hostel/Flat Rental Management Syatem---------")
    Members = int(input("Enter The Number of Members!=> "))

    All_Member = []
    for i in range(1,Members+1):
        print(f"Enter details for Member{i}")
        Member_Name= input(f"Enter Name => ")
        Advanced_payment = float(input(f"Enter {Member_Name}'s Advanced amount In a month=> "))
        Marketting_Value = float(input(f"Enter {Member_Name}'s Marketting price=> "))

        All_Member.append({
            'Name':Member_Name,
            'Advanced_pay': Advanced_payment,
            'Marketting': Marketting_Value
        })

    print("------------Enter Monthly expenses-----------")
    Rice = float(input(f"Enter total Rice Expenses in a month => ")) 
    Grocery = float(input(f"Enter Grocery price=> "))
    Gas = float(input(f"Enter Gas  price=> "))
    water = float(input(f"Enter Water price  in a month=> "))
    Electric_Bill_unit = float(input(f"Enter  Electric bill unit=> "))
    Electric_charge_per_unit = float(input(f"Enter Electric charge per unit=> "))
    Electric_charge = Electric_Bill_unit * Electric_charge_per_unit
    others = float(input(f"Enter other Miscellaneous Expenses=> "))
    total_Marketting = 0
    for n in All_Member:
        total_Marketting += n['Marketting']

    Total_Expenses = (Rice + Grocery + Gas + water + Electric_charge + others + total_Marketting)
    per_head = Total_Expenses / Members

    Result = []
    for m in All_Member:
        total = m['Advanced_pay'] + m['Marketting']
        due = per_head - total

        Result.append([
            m['Name'],
            f"${m['Advanced_pay']:.2f}",
            f"${m['Marketting']:.2f}",
            f"${per_head:.2f}",
            f"${total:.2f}",
            f"${due:.2f}",
        ])

    # Display Data 
    print("---------Final Expenses Summery---------")
    headers = ["Name","Advanced Pay","Marketting","Per Head Expenses","Total Advanced","Due(+)/return(-)"]
    print(tabulate(Result,headers,tablefmt="fancy_grid"))


    # Save data 
    with open("Results/Rental_system.txt","w") as file:
        file.write(tabulate(Result,headers,tablefmt="grid"))
        file.write(f"\n\n Total Expenses:{Total_Expenses:.2f}")
        file.write(f"\nPer Head Expenses:{per_head:.2f}")

    print("\nRecord saved to 'Rental_report.txt'")

Rental_system()


#  1. Function to calculate performance bonus
print("----->/Corporate Talent & Payroll Management System\<-----")
def calculate_bonus(base_salary,performance_rating):
    if performance_rating == 5 :
        bonus_amount = 0.20
    # elif performance_rating == 4 or performance_rating == 3 :
    elif performance_rating in [4,3]:
        bonus_amount = 0.10
    else:
        bonus_amount= 0.00

    return  base_salary * bonus_amount            

# 2. Function to calculate progressive tax deductions

def calculate_tax(gross_salary):
    if gross_salary > 7000:
        tax_amount = 0.15
    elif gross_salary >= 3000 :
        tax_amount = 0.10 
    else :
        tax_amount = 0.00        

    return gross_salary * tax_amount    

# 3. Core runtime application

def main_hr_app():
    print("---  Corporate Payroll System  ---")

    name = input("Enter your name :")
    base_salary = float(input("Enter your salary (EGP):"))
    rating = int(input("Enter your Rating (1-5):"))

    if base_salary < 0 or rating < 1 or rating > 5 :
        print("Invalid data entered. Please restart and check your inputs.")
        return       
    

    # Process Flow via Functions

    bonus = calculate_bonus(base_salary, rating)
    gross_salary = base_salary + bonus
    tax = calculate_tax(gross_salary)
    net_salary = gross_salary - tax
    # Output Statement Generator
    print("\n" + "=" *40)
    print(f"PAYROLL STATEMENT FOR : {name.upper()}")
    print("=" * 40)
    print(f"base salary : {base_salary:.2f} EGP")
    print(f"bonus : {bonus:.2f}")
    print(f"gross salary : {gross_salary:.2f}EGP")
    print(f"Tax Deductions : {tax:.2f}")
    print("=" * 40)
    print(f"NET PAYABLE CASH : {net_salary:.2f}EGP")
    print("=" * 40)

# Trigger Program Run
main_hr_app()
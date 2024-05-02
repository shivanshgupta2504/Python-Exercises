"""
Calculate income tax for the given income by adhering to the rules below

Taxable Income	    Rate (in %)
First $10,000	    0
Next $10,000	    10
The remaining	    20
"""

def tax_pay(income):
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 0.1
    else:
        tax = (10000 * 0.1) + (income - 20000) * 0.2

    print("Your tax is: ", tax)
     


income = int(input("Enter your income: "))
tax_pay(income)


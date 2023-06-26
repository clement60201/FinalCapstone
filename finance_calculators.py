import math

print("""Investment - to calculate the amount of interest you'll earn on your investment\nBond - to calculate the amount you'll have to pay on a home loan\n 
Enter either 'investment' or 'bond' from the menu above to proceed: \n""")

finance_calculator_type = "investment OR bond"
finance_calculator = input("Choose finance calculator: ")
interest = "'simple' OR 'compound'"

if finance_calculator.lower() == "investment":
    deposit_amount = float(input("Please enter the amount you are depositing: £"))
    interest_rate = float(input("Please enter your interest rate: "))
    num_years_investing = int(input("Please enter the number of years you are investing: "))
    interest_type = input("Choose type of interest: 'simple' or 'compound' ")
    if interest_type.lower() == "simple":
        r_interest_rate = interest_rate / 100
        simple_interest = deposit_amount*(1 + r_interest_rate*num_years_investing)
        print(f"£{simple_interest.__round__(2)}")
    elif interest_type.lower() == "compound":
        r_interest_rate = interest_rate / 100
        compound_interest = deposit_amount * math.pow((1+r_interest_rate), num_years_investing)
        print(f"£{compound_interest.__round__(2)}")
    else:
        print(f"Invalid interest type; please choose {interest}: ")
elif finance_calculator.lower() == "bond":
    house_value = float(input("Please enter the current value of the property: £"))
    interest_rate = float(input("please enter the current interest rate "))
    i_interest_rate = (interest_rate / 100) / 12
    num_of_months_for_bond_repayment = int(input("Please enter the number of months planned to repay the bond: "))
    monthly_repayment = (i_interest_rate * house_value)/(1 - (1 + i_interest_rate)**(- num_of_months_for_bond_repayment))
    print(f"Your monthly repayment will be £{monthly_repayment.__round__(2)}")
else:
    print(f"Invalid finance calculator type; please choose {finance_calculator_type}:")
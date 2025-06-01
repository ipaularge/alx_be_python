# Prompt the user for income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output results
print("Your monthly savings are ${:.0f}.".format(monthly_savings))
print("Projected savings after one year, with interest, is: ${:.0f}.".format(annual_savings))

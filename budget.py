vinny_income = 150

amanda_income = 200

amanda_bills = [1, 2]

vinny_bills = [1, 2, 3]

food_expense = int(input("How much are you spending on food this month? > "))



def expense_summer(expenses):
  total_expenses = 0
  for expense in expenses:
    total_expenses += expense
  return int(total_expenses)


def budget_splitter():
  
  #Remaining spending money after bills calculation
  vinny_bills_summed = expense_summer(vinny_bills)
  amanda_bills_summed = expense_summer(amanda_bills)
  vinny_spending_money = vinny_income - vinny_bills_summed
  amanda_spending_money = amanda_income - amanda_bills_summed
  
  #Spending money and spending money percentage calculator
  combined_spending_money = vinny_spending_money + amanda_spending_money
  vinny_spending_money_percentage = vinny_spending_money / combined_spending_money
  amanda_spending_money_percentage = amanda_spending_money / combined_spending_money
  
  # Expense breakdown calculator
  vinny_food_percent = food_expense * vinny_spending_money_percentage
  amanda_food_percent = food_expense * amanda_spending_money_percentage

  #Readout
  print(f"Amanda's percentage is {amanda_spending_money_percentage} and Vinny's percentage is {vinny_spending_money_percentage}")
  print(f"Amanda's spending money after bills is {amanda_spending_money} and Vinny's is {vinny_spending_money}")
  print(f"Combined spending money after bills is {combined_spending_money}")
  print(f"If food cost is {food_expense} then Amanda pays {amanda_food_percent} and Vinny pays {vinny_food_percent}")
  


budget_splitter()
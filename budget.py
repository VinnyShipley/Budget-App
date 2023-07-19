vinny_income = 150

amanda_income = 200

amanda_bills = [1, 2]

vinny_bills = [1, 2, 3]


def income_collector():
  
  #Gets number of incomes
  number_of_incomes = input('How many incomes are we calculating today? > ')
  income_list = [0] * int(number_of_incomes)
  i = 0
  
  #Fills the income list with the entered incomes
  while i + 1 <= len(income_list):
    income_list_value = input(f"Income # {i + 1} amount: > ")
    income_list[i] = int(income_list_value)
    i += 1
  
  
  return income_list



# Creating input for user to enter expenses
def expense_collector():
  expense_list_length = input(f"How many expenses are you calculating today? > ")
  expense_list = [0] * int(expense_list_length)
  i = 0
  
  # Collects expenses
  while i + 1 <= len(expense_list):
    expense_list_value = input(f"Expense # {i + 1} cost in dollars: > ")
    expense_list[i] = int(expense_list_value)
    i += 1
  
  return expense_list




def budget_splitter():
  
  #Remaining spending money after bills calculation
  vinny_bills_summed = sum(vinny_bills)
  amanda_bills_summed = sum(amanda_bills)
  vinny_spending_money = vinny_income - vinny_bills_summed
  amanda_spending_money = amanda_income - amanda_bills_summed
  
  #Spending money and spending money percentage calculator
  combined_spending_money = vinny_spending_money + amanda_spending_money
  vinny_spending_money_percentage = vinny_spending_money / combined_spending_money
  amanda_spending_money_percentage = amanda_spending_money / combined_spending_money

  #Printout
  print(f"Amanda's percentage is {amanda_spending_money_percentage} and Vinny's percentage is {vinny_spending_money_percentage}")
  print(f"Amanda's spending money after bills is {amanda_spending_money} and Vinny's is {vinny_spending_money}")
  print(f"Combined spending money after bills is {combined_spending_money}")
  

income_collector()
expense_collector()
budget_splitter()
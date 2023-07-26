

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
def expense_collector(income_list_input):
  j = 0
  for income in income_list_input:
    expense_list_length = input(f"How many expenses are you calculating today for income {j + 1}> ")
    expense_list = [0] * int(expense_list_length)
    j += 1
    
  
    # Collects expenses
    i = 0
    while i + 1 <= len(expense_list):
      expense_list_value = input(f"Expense # {i + 1} cost in dollars: > ")
      expense_list[i] = int(expense_list_value)
      i += 1
  
  return expense_list




def budget_splitter(list_of_incomes_final, list_of_expenses_per_income_final):
  list_of_incomes_after_expenses = [0] * len(list_of_incomes_final)
  
  
  #Loop that subtracts expenses from the correct income and returns list of incomes after expenses
  j = 0
  for income in list_of_incomes_final:
    money_after_expenses = list_of_incomes_final[j] - list_of_expenses_per_income_final[j]
    list_of_incomes_after_expenses[j] = money_after_expenses
    j += 1
  
  #Creates and displays the combined money after expenses
  combined_spending_money = sum(list_of_incomes_after_expenses)
  print(f"The combined remaining money for fun expenses after bills is {combined_spending_money}")
  
  
  #Gathers percentages of spending money per incomes after expenses
  i = 0
  while i < len(list_of_incomes_final):
    precise_percent_person_pays =  list_of_incomes_after_expenses[i] / combined_spending_money
    rounded_percent_person_pays = round(precise_percent_person_pays, 2)
    print(f"The person with the income of {list_of_incomes_final[i]} will pay {rounded_percent_person_pays} % of the expenses after bills this month.")
    i += 1


incomes = income_collector()
expenses_for_each_income = expense_collector(incomes)
budget_splitter(incomes, expenses_for_each_income)
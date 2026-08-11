starting_balance = float(input("What is your starting balance: $"))
expenses = []
print(f"Starting balance: ${starting_balance}")
input_expensename = str(input("Enter an expense name:"))
input_expenseprice = float(input("Enter the expense price: $"))
expenses.append(f"{input_expensename} (${input_expenseprice})")
balance = starting_balance - input_expenseprice
print(f"Your current balance is : ${balance}")
print(f"Your expenses are: {expenses}")
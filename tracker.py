starting_balance = float(input("What is your starting balance: $"))
expenses = []
print(f"Starting balance: ${starting_balance}")
current_balance = starting_balance

while True:
    input_expensename = str(input("Enter an expense name (or type 'Done' to finish):"))
    if input_expensename == "done":
        break
    elif input_expensename == "Done":
        break
    elif input_expensename == "DONE":
        break
    elif input_expensename == "dOne":
        break
    elif input_expensename == "":
        print("Please enter a valid expense name.")
        continue
    else:
        input_expenseprice = float(input("Enter the expense price: $"))
        expenses.append(f"{input_expensename} (${input_expenseprice})")
        current_balance = current_balance - input_expenseprice
        print(f"Your current balance is : ${current_balance}")
        print(f"Your expenses are: {expenses}")

print("You have finished entering your expenses.")
print("Here is a summary of your expenses: ")
for expense in expenses:
    print(expense)
print(f"Your final balance is: ${current_balance}")

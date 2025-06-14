import datetime
import calendar

def main():
    """
    Main function for tracking and calculating expenses and income for the current month.
    """

    expenses = []  # List to store expenses
    incomes = []  # List to store incomes
    total_spent = 0  # Total expenses for the month
    total_earned = 0  # Total income for the month

    # Get the current year and month
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    month_name = calendar.month_name[current_month] #Get the name of current month

    print(f"\nTracking expenses and income for {month_name}, {current_year}") # Inform the user about the current month

    while True:
        print("\nChoose an action:")
        print("1. Add expense")
        print("2. Add income")
        print("3. View expenses for this month")
        print("4. View income for this month")
        print("5. Calculate total expenses for this month")
        print("6. Calculate total income for this month")
        print("7. Compare income and expenses for this month")
        print("8. Exit")

        choice = input("Enter the action number: ")

        if choice == "1":
            try:
                amount = float(input("Enter the expense amount: "))
                category = input("Enter the expense category (e.g., food, transportation, entertainment): ")
                date = datetime.date.today()
                expenses.append({"amount": amount, "category": category, "date": date})
                total_spent += amount
                print("Expense added.")
            except ValueError:
                print("Invalid amount format. Please try again.")

        elif choice == "2":
            try:
                amount = float(input("Enter the income amount: "))
                source = input("Enter the income source (e.g., salary, freelance, investment): ")
                date = datetime.date.today()
                incomes.append({"amount": amount, "source": source, "date": date})
                total_earned += amount
                print("Income added.")
            except ValueError:
                print("Invalid amount format. Please try again.")

        elif choice == "3":
            print(f"\nExpenses for {month_name}, {current_year}:")
            monthly_expenses = [expense for expense in expenses if expense['date'].year == current_year and expense['date'].month == current_month] #Filtration
            if not monthly_expenses:
                print("No expenses recorded for this month yet.")
            else:
                for expense in monthly_expenses:
                    print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

        elif choice == "4":
            print(f"\nIncome for {month_name}, {current_year}:")
            monthly_incomes = [income for income in incomes if income['date'].year == current_year and income['date'].month == current_month] #Filtration
            if not monthly_incomes:
                print("No income recorded for this month yet.")
            else:
                for income in monthly_incomes:
                    print(f"Amount: {income['amount']}, Source: {income['source']}, Date: {income['date']}")

        elif choice == "5":
             print(f"\nCalculating Total expenses for {month_name}, {current_year}") # Inform the user about action
             monthly_expenses = [expense for expense in expenses if expense['date'].year == current_year and expense['date'].month == current_month] #Filtration
             total_spent = sum(expense['amount'] for expense in monthly_expenses)
             print(f"Total expenses for {month_name}, {current_year}: {total_spent}")



        elif choice == "6":
            print(f"\nCalculating Total income for {month_name}, {current_year}") # Inform the user about action
            monthly_incomes = [income for income in incomes if income['date'].year == current_year and income['date'].month == current_month] #Filtration
            total_earned = sum(income['amount'] for income in monthly_incomes)
            print(f"Total income for {month_name}, {current_year}: {total_earned}")


        elif choice == "7":

             print(f"\nComparison for {month_name}, {current_year}") # Inform the user about action

             monthly_expenses = [expense for expense in expenses if expense['date'].year == current_year and expense['date'].month == current_month] #Filtration
             total_spent = sum(expense['amount'] for expense in monthly_expenses) # Calculating total again

             monthly_incomes = [income for income in incomes if income['date'].year == current_year and income['date'].month == current_month] #Filtration
             total_earned = sum(income['amount'] for income in monthly_incomes) # Calculating total again


             difference = total_earned - total_spent
             if difference > 0:
                print(f"Income exceeds expenses by: {difference} for {month_name}, {current_year}")
             elif difference < 0:
                print(f"Expenses exceed income by: {abs(difference)} for {month_name}, {current_year}")
             else:
                print(f"Income and expenses are equal for {month_name}, {current_year}.")

        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
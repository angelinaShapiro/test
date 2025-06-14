import datetime

def main():
    """
    Main function for tracking and calculating monthly expenses and income.
    """

    expenses = []  # List to store expenses
    incomes = [] # List to store incomes
    total_spent = 0  # Total expenses for the month
    total_earned = 0 # Total income for the month

    while True:
        print("\nChoose an action:")
        print("1. Add expense")
        print("2. Add income")
        print("3. View monthly expenses")
        print("4. View monthly income")
        print("5. Calculate total expenses")
        print("6. Calculate total income")
        print("7. Compare income and expenses")
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
            if not expenses:
                print("No expenses recorded for this month yet.")
            else:
                print("\nMonthly expenses:")
                for expense in expenses:
                    print(f"Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

        elif choice == "4":
            if not incomes:
                print("No income recorded for this month yet.")
            else:
                print("\nMonthly income:")
                for income in incomes:
                    print(f"Amount: {income['amount']}, Source: {income['source']}, Date: {income['date']}")

        elif choice == "5":
            print(f"Total monthly expenses: {total_spent}")

        elif choice == "6":
            print(f"Total monthly income: {total_earned}")

        elif choice == "7":
            difference = total_earned - total_spent
            if difference > 0:
                print(f"Income exceeds expenses by: {difference}")
            elif difference < 0:
                print(f"Expenses exceed income by: {abs(difference)}")
            else:
                print("Income and expenses are equal.")


        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
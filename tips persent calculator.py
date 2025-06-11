def tip_calculator():
    """Calculates the tip amount and total bill for a U.S. context."""

    while True:
        try:
            bill_amount = float(input("Enter the total bill amount: $"))
            if bill_amount <= 0:
                print("Bill amount must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for the bill amount.")

    while True:
        try:
            tip_percentage = float(input("Enter the tip percentage (e.g., 15, 20, 25): "))
            if tip_percentage < 0:
                print("Tip percentage must be a non-negative number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for the tip percentage.")

    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount

    print("\n--- Calculation ---")
    print(f"Bill Amount: ${bill_amount:.2f}")
    print(f"Tip Amount ({tip_percentage}%): ${tip_amount:.2f}")
    print(f"Total Bill: ${total_bill:.2f}")
    print("--------------------\n")

    print("Enjoy your meal!")

if __name__ == "__main__":
    tip_calculator()
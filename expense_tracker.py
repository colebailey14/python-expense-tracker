import csv
import os

CSV_FILE = "expenses.csv"

def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category])
    print(f"Expense '{name}' added successfully!")

def view_expenses():
    if not os.path.exists(CSV_FILE):
        print("No expenses recorded yet.")
        return

    total = 0
    print("\nYour Expenses:")
    print("Name\tAmount\tCategory")
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, amount, category = row
            print(f"{name}\t${amount}\t{category}")
            total += float(amount)
    print(f"\nTotal Expenses: ${total:.2f}\n")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

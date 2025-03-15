import json
import datetime

EXPENSE_FILE = "expenses.json"

def load_expenses():
    try:
        with open(EXPENSE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    try:
        amount = float(input("Enter amount spent: "))
        category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip()
        description = input("Enter description: ").strip()
        date = str(datetime.date.today())
        
        expense = {"date": date, "amount": amount, "category": category, "description": description}
        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("\nExpense History:")
    for exp in expenses:
        print(f"{exp['date']} - {exp['category']}: ${exp['amount']} ({exp['description']})")

def expense_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    
    monthly_summary = {}
    category_summary = {}
    
    for exp in expenses:
        month = exp['date'][:7]  # YYYY-MM format
        category = exp['category']
        amount = exp['amount']
        
        monthly_summary[month] = monthly_summary.get(month, 0) + amount
        category_summary[category] = category_summary.get(category, 0) + amount
    
    print("\nMonthly Expense Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")
    
    print("\nCategory-wise Expense Summary:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            expense_summary()
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
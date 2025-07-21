import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

class BudgetPlannerApp:
    def __init__(self, master):
        self.master = master
        master.title("Budget Planner")

        self.expenses = []

        self.label = tk.Label(master, text="Budget Planner", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry fields for expense details
        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=10, sticky=tk.E)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=1, column=1)

        self.category_label = tk.Label(master, text="Category:")
        self.category_label.grid(row=2, column=0, padx=10, sticky=tk.E)

        self.category_entry = tk.Entry(master)
        self.category_entry.grid(row=2, column=1)

        self.add_button = ttk.Button(master, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Button to view expenses
        self.view_button = ttk.Button(master, text="View Expenses", command=self.view_expenses)
        self.view_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Button to generate spending report
        self.report_button = ttk.Button(master, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=5, column=0, columnspan=2, pady=10)

    def add_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()

        if amount and category:
            self.expenses.append({"amount": float(amount), "category": category})
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
            tk.messagebox.showinfo("Expense Added", "Expense successfully added.")
        else:
            tk.messagebox.showwarning("Warning", "Please fill in all fields.")

    def view_expenses(self):
        if self.expenses:
            tk.messagebox.showinfo("Expenses", "\n".join([f"{expense['amount']} - {expense['category']}" for expense in self.expenses]))
        else:
            tk.messagebox.showinfo("Expenses", "No expenses added yet.")

    def generate_report(self):
        if self.expenses:
            categories = [expense['category'] for expense in self.expenses]
            unique_categories = list(set(categories))
            category_totals = {category: sum([expense['amount'] for expense in self.expenses if expense['category'] == category]) for category in unique_categories}

            plt.figure(figsize=(8, 6))
            plt.pie(category_totals.values(), labels=category_totals.keys(), autopct='%1.1f%%', startangle=140)
            plt.axis('equal')
            plt.title('Spending by Category')
            plt.show()
        else:
            tk.messagebox.showinfo("Report", "No expenses added yet.")

def main():
    root = tk.Tk()
    app = BudgetPlannerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

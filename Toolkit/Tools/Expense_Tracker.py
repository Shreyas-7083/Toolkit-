import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
from datetime import datetime

class ExpenseTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Expense Tracker")

        self.expenses = []

        self.label = tk.Label(master, text="Expense Tracker", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=1, column=0, padx=10)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=1, column=1)

        self.category_label = tk.Label(master, text="Category:")
        self.category_label.grid(row=2, column=0, padx=10)

        self.category_entry = tk.Entry(master)
        self.category_entry.grid(row=2, column=1)

        self.save_button = ttk.Button(master, text="Save Expense", command=self.save_expense)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.expense_list = tk.Listbox(master, width=50)
        self.expense_list.grid(row=4, column=0, columnspan=2)

        self.load_expenses()

    def save_expense(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if amount and category:
            self.expenses.append((date, amount, category))
            self.save_to_file()
            self.load_expenses()
            self.amount_entry.delete(0, tk.END)
            self.category_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter amount and category.")

    def save_to_file(self):
        with open("expenses.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category"])
            writer.writerows(self.expenses)

    def load_expenses(self):
        self.expense_list.delete(0, tk.END)
        try:
            with open("expenses.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header row
                for row in reader:
                    self.expense_list.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]}")
        except FileNotFoundError:
            pass

def main():
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

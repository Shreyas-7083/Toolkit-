import tkinter as tk
from tkinter import ttk
import sqlite3

class GroceryListApp:
    def __init__(self, master):
        self.master = master
        master.title("Grocery List")

        # Connect to SQLite database or create if not exists
        self.conn = sqlite3.connect("grocery_list.db")
        self.cursor = self.conn.cursor()

        # Create grocery table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS grocery (
                            id INTEGER PRIMARY KEY,
                            item TEXT,
                            quantity INTEGER
                            )''')
        self.conn.commit()

        self.label = tk.Label(master, text="Grocery List", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.item_label = tk.Label(master, text="Item:")
        self.item_label.grid(row=1, column=0, padx=10, sticky=tk.E)

        self.item_entry = tk.Entry(master)
        self.item_entry.grid(row=1, column=1)

        self.quantity_label = tk.Label(master, text="Quantity:")
        self.quantity_label.grid(row=2, column=0, padx=10, sticky=tk.E)

        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=2, column=1)

        self.add_button = ttk.Button(master, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.item_list = tk.Listbox(master, height=15, width=50)
        self.item_list.grid(row=4, column=0, columnspan=2)

        # Populate the item list from the database
        self.populate_item_list()

    def add_item(self):
        item = self.item_entry.get()
        quantity = self.quantity_entry.get()

        if item:
            # Insert item into database
            self.cursor.execute("INSERT INTO grocery (item, quantity) VALUES (?, ?)", (item, quantity))
            self.conn.commit()
            # Update item list
            self.populate_item_list()
            # Clear entry fields
            self.clear_entry_fields()

    def populate_item_list(self):
        # Clear the existing items in the listbox
        self.item_list.delete(0, tk.END)
        # Fetch items from database and insert into listbox
        self.cursor.execute("SELECT * FROM grocery")
        rows = self.cursor.fetchall()
        for row in rows:
            self.item_list.insert(tk.END, f"{row[1]} - {row[2]}")

    def clear_entry_fields(self):
        self.item_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = GroceryListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

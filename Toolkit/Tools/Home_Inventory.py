import tkinter as tk
from tkinter import ttk
import sqlite3

class HomeInventoryApp:
    def __init__(self, master):
        self.master = master
        master.title("Home Inventory")

        # Connect to SQLite database or create if not exists
        self.conn = sqlite3.connect("home_inventory.db")
        self.cursor = self.conn.cursor()

        # Create inventory table if not exists
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            category TEXT,
                            location TEXT,
                            purchase_date TEXT,
                            warranty TEXT,
                            price REAL
                            )''')
        self.conn.commit()

        self.label = tk.Label(master, text="Home Inventory", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry fields for item details
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, sticky=tk.E)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1)

        self.category_label = tk.Label(master, text="Category:")
        self.category_label.grid(row=2, column=0, padx=10, sticky=tk.E)

        self.category_entry = tk.Entry(master)
        self.category_entry.grid(row=2, column=1)

        self.location_label = tk.Label(master, text="Location:")
        self.location_label.grid(row=3, column=0, padx=10, sticky=tk.E)

        self.location_entry = tk.Entry(master)
        self.location_entry.grid(row=3, column=1)

        self.purchase_date_label = tk.Label(master, text="Purchase Date:")
        self.purchase_date_label.grid(row=4, column=0, padx=10, sticky=tk.E)

        self.purchase_date_entry = tk.Entry(master)
        self.purchase_date_entry.grid(row=4, column=1)

        self.warranty_label = tk.Label(master, text="Warranty:")
        self.warranty_label.grid(row=5, column=0, padx=10, sticky=tk.E)

        self.warranty_entry = tk.Entry(master)
        self.warranty_entry.grid(row=5, column=1)

        self.price_label = tk.Label(master, text="Price:")
        self.price_label.grid(row=6, column=0, padx=10, sticky=tk.E)

        self.price_entry = tk.Entry(master)
        self.price_entry.grid(row=6, column=1)

        # Button to add item
        self.add_button = ttk.Button(master, text="Add Item", command=self.add_item)
        self.add_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Treeview to display inventory
        self.tree = ttk.Treeview(master, columns=("Name", "Category", "Location", "Purchase Date", "Warranty", "Price"))
        self.tree.grid(row=8, column=0, columnspan=2)
        self.tree.heading("#0", text="ID")
        self.tree.heading("#1", text="Name")
        self.tree.heading("#2", text="Category")
        self.tree.heading("#3", text="Location")
        self.tree.heading("#4", text="Purchase Date")
        self.tree.heading("#5", text="Warranty")
        self.tree.heading("#6", text="Price")

        # Populate the inventory treeview
        self.populate_inventory()

    def add_item(self):
        name = self.name_entry.get()
        category = self.category_entry.get()
        location = self.location_entry.get()
        purchase_date = self.purchase_date_entry.get()
        warranty = self.warranty_entry.get()
        price = self.price_entry.get()

        if name and category:
            self.cursor.execute("INSERT INTO inventory (name, category, location, purchase_date, warranty, price) VALUES (?, ?, ?, ?, ?, ?)",
                                (name, category, location, purchase_date, warranty, price))
            self.conn.commit()
            self.populate_inventory()
            self.clear_entry_fields()

    def populate_inventory(self):
        self.tree.delete(*self.tree.get_children())
        self.cursor.execute("SELECT * FROM inventory")
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", text=row[0], values=row[1:])

    def clear_entry_fields(self):
        self.name_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.purchase_date_entry.delete(0, tk.END)
        self.warranty_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = HomeInventoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

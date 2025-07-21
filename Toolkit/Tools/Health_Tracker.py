import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class HealthTrackerApp:
    def __init__(self, master):
        self.master = master
        master.title("Health Tracker")

        self.label = tk.Label(master, text="Health Tracker", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Dropdown menu for category selection
        self.category_label = tk.Label(master, text="Category:")
        self.category_label.grid(row=1, column=0, padx=10, sticky=tk.E)

        self.categories = ["Weight", "Exercise", "Sleep", "Calories"]
        self.category_var = tk.StringVar(master)
        self.category_var.set(self.categories[0])  # Default category
        self.category_menu = ttk.OptionMenu(master, self.category_var, *self.categories)
        self.category_menu.grid(row=1, column=1)

        # Entry field for value input
        self.value_label = tk.Label(master, text="Value:")
        self.value_label.grid(row=2, column=0, padx=10, sticky=tk.E)

        self.value_entry = tk.Entry(master)
        self.value_entry.grid(row=2, column=1)

        # Entry field for date input
        self.date_label = tk.Label(master, text="Date:")
        self.date_label.grid(row=3, column=0, padx=10, sticky=tk.E)

        self.date_entry = tk.Entry(master)
        self.date_entry.grid(row=3, column=1)

        # Button to add health entry
        self.add_entry_button = ttk.Button(master, text="Add Entry", command=self.add_health_entry)
        self.add_entry_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Button to generate report
        self.report_button = ttk.Button(master, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Frame to hold health chart
        self.health_frame = ttk.Frame(master)
        self.health_frame.grid(row=6, column=0, columnspan=2)

        # Vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self.health_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def add_health_entry(self):
        category = self.category_var.get()
        value = self.value_entry.get()
        date = self.date_entry.get()
        # Add health entry to database or data structure
        messagebox.showinfo("Entry Added", f"Entry added: Category - {category}, Date - {date}, Value - {value}")

    def generate_report(self):
        # Simulated function to generate report
        # Display report in a messagebox or text widget
        messagebox.showinfo("Report Generated", "Report generated successfully.")

def main():
    root = tk.Tk()
    app = HealthTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

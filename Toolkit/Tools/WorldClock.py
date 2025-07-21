from datetime import datetime
import pytz
from tkinter import *
from tkinter import ttk

class WorldClockClass:
    def __init__(self, window):
        self.window = window
        self.window.title("World Clock")
        self.window.geometry("300x300+600+170")
        self.window.config(bg='#AE2321')
        self.window.resizable(False,False)
        self.window.focus_force()
        image_icon=PhotoImage(file="img/clock_logo.png")
        self.window.iconphoto(False,image_icon)

        lbl=Label(self.window,text="Select Country",font=("Elephant",20,"bold"),bg='#AE2321',fg="white")
        lbl.grid(row=0, column=1, padx=40, pady=15, sticky="w")
    
        self.date_label = Label(window, font=("Georgia", 16),bg='#AE2321',fg="white")
        self.date_label.grid(row=4, column=1, padx=95, pady=5, sticky="w")

        self.time_label = Label(window, font=("Georgia", 20),bg='#AE2321',fg="white")
        self.time_label.grid(row=5, column=1, padx=100, pady=5, sticky="w")

        # Get all time zones
        all_timezones = pytz.all_timezones
        
        
        # Create a dictionary mapping each country to its time zone
        self.countries = {}
        for timezone in all_timezones:
            country = timezone.split('/')[0]
            if country not in self.countries:
                self.countries[country] = []
            self.countries[country].append(timezone)

        # Create a sorted list of countries
        sorted_countries = sorted(self.countries.keys())
        
        # Create a dropdown list
        self.selected_country = StringVar()
        self.country_dropdown = ttk.Combobox(window,font=("Georgia", 12,"bold"),textvariable=self.selected_country)
        self.country_dropdown["values"] = sorted_countries
        self.country_dropdown.grid(row=1, column=1, padx=45, pady=10, sticky="w")
        self.country_dropdown.current(0)  # Set initial value
        self.country_dropdown.bind("<<ComboboxSelected>>", self.update_selected_time)

        # Update the time for the initially selected country
        self.update_selected_time()

    def update_selected_time(self, event=None):
        selected_country = self.selected_country.get()
        if selected_country:
            time_zones = self.countries[selected_country]
            if time_zones:
                timezone = time_zones[0]  # Use the first timezone for the selected country
                current_date=datetime.now(pytz.timezone(timezone)).strftime("%Y-%m-%d")
                self.date_label.config(text=current_date)
                current_time = datetime.now(pytz.timezone(timezone)).strftime("%H:%M:%S")
                self.time_label.config(text=current_time)
                
                

        # Schedule the update of time label every second
        self.window.after(1000, self.update_selected_time)

if __name__ == "__main__":
    window = Tk()
    obj = WorldClockClass(window)
    window.mainloop()

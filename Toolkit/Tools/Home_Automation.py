import tkinter as tk
from tkinter import ttk
import requests
import tkinter.messagebox

def toggle_lights(self):
    # Simulated API call to toggle lights
    try:
        # Assuming the API endpoint for toggling lights is at http://example.com/toggle_lights
        response = requests.post("http://example.com/toggle_lights")
        if response.status_code == 200:
            self.update_light_status()
            tkinter.messagebox.showinfo("Success", "Lights toggled successfully.")
        else:
            tkinter.messagebox.showerror("Error", f"Failed to toggle lights. Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        tkinter.messagebox.showerror("Error", f"Failed to toggle lights. Error: {str(e)}")

class HomeAutomationApp:
    def __init__(self, master):
        self.master = master
        master.title("Home Automation Control")

        self.label = tk.Label(master, text="Home Automation Control", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Button to turn lights on/off
        self.light_button = ttk.Button(master, text="Turn Lights On", command=self.toggle_lights)
        self.light_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Label to display light status
        self.light_status_label = tk.Label(master, text="")
        self.light_status_label.grid(row=2, column=0, columnspan=2)

        # Update light status label
        self.update_light_status()
    def toggle_lights(self):
    # Simulated API call to toggle lights
        try:
            # Assuming the API endpoint for toggling lights is at http://example.com/toggle_lights
            response = requests.post("http://example.com/toggle_lights")
            if response.status_code == 200:
                self.update_light_status()
                tkinter.messagebox.showinfo("Success", "Lights toggled successfully.")
            else:
                tkinter.messagebox.showerror("Error", f"Failed to toggle lights. Error code: {response.status_code}")
        except requests.exceptions.RequestException as e:
         tkinter.messagebox.showerror("Error", f"Failed to toggle lights. Error: {str(e)}")
    
    def update_light_status(self):
        # Simulated API call to get light status
        try:
            # Assuming the API endpoint for getting light status is at http://example.com/light_status
            response = requests.get("http://example.com/light_status")
            if response.status_code == 200:
                light_status = response.json()["status"]
                self.light_status_label.config(text=f"Light status: {light_status}")
            else:
                self.light_status_label.config(text="Light status: Unknown")
        except requests.exceptions.RequestException:
            self.light_status_label.config(text="Light status: Unknown")

def main():
    root = tk.Tk()
    app = HomeAutomationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

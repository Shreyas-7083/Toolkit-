import tkinter as tk
from tkinter import simpledialog
from datetime import datetime
from tkcalendar import Calendar

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        self.deadline_label = tk.Label(master, text="Deadline:")
        self.deadline_label.pack()

        self.deadline_calendar = Calendar(master, selectmode="day", date_pattern="yyyy-mm-dd")
        self.deadline_calendar.pack()

        self.deadline_time_label = tk.Label(master, text="Set Deadline Time (HH:MM):")
        self.deadline_time_label.pack()

        self.deadline_time_entry = tk.Entry(master)
        self.deadline_time_entry.pack()

        self.task_input = tk.Entry(master)
        self.task_input.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.edit_button = tk.Button(master, text="Edit Task", command=self.edit_task)
        self.edit_button.pack()

        self.task_list = tk.Listbox(master, width=200)
        self.task_list.pack()

        self.start_button = tk.Button(master, text="Start Task", command=self.start_task)
        self.start_button.pack()

        self.finish_button = tk.Button(master, text="Finish Task", command=self.finish_task)
        self.finish_button.pack()

    def add_task(self):
        task_name = self.task_input.get()
        deadline_date_str = self.deadline_calendar.get_date()
        deadline_time_str = self.deadline_time_entry.get()

        if task_name:
            deadline_datetime = None
            if deadline_date_str:
                deadline_date = datetime.strptime(deadline_date_str, "%Y-%m-%d").date()
                deadline_datetime = datetime.combine(deadline_date, datetime.min.time())

            if deadline_time_str:
                try:
                    hours, minutes = map(int, deadline_time_str.split(":"))
                    if deadline_datetime:
                        deadline_datetime = deadline_datetime.replace(hour=hours, minute=minutes)
                    else:
                        deadline_datetime = datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0)
                except ValueError:
                    messagebox.showerror("Error", "Invalid time format. Use HH:MM.")
                    return

            task = {"name": task_name, "status": "To Do", "deadline": deadline_datetime}
            self.tasks.append(task)
            self.update_task_list()

    def edit_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            new_name = simpledialog.askstring("Edit Task", "Enter new task name:", initialvalue=task["name"])
            if new_name:
                task["name"] = new_name
                self.update_task_list()

    def start_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task["status"] = "Work in Progress"
            self.update_task_list()

    def finish_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task["status"] = "Finished"
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            status = task["status"]
            name = task["name"]
            deadline = task["deadline"]
            if deadline:
                deadline_str = deadline.strftime("%Y-%m-%d %H:%M")
                self.task_list.insert(tk.END, f"{status}: {name} (Deadline: {deadline_str})")
            else:
                self.task_list.insert(tk.END, f"{status}: {name}")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
from datetime import datetime, timedelta
from tkcalendar import Calendar
from plyer import notification
import json, os, threading, time
import winsound  # Windows sound; for cross-platform use playsound

TASKS_FILE = "tasks.json"

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Advanced To-Do List with Alarms")
        master.geometry("850x600")

        self.tasks = []
        self.load_tasks()

        # ----- Input Section -----
        tk.Label(master, text="Deadline Date:").pack()
        self.deadline_calendar = Calendar(master, selectmode="day", date_pattern="yyyy-mm-dd")
        self.deadline_calendar.pack()

        tk.Label(master, text="Deadline Time (HH:MM):").pack()
        self.deadline_time_entry = tk.Entry(master)
        self.deadline_time_entry.pack()

        tk.Label(master, text="Task Name:").pack()
        self.task_input = tk.Entry(master, width=40)
        self.task_input.pack()

        tk.Label(master, text="Priority:").pack()
        self.priority_var = tk.StringVar(value="Medium")
        ttk.Combobox(master, textvariable=self.priority_var, values=["Low", "Medium", "High"]).pack()

        tk.Label(master, text="Reminder (minutes before deadline):").pack()
        self.reminder_entry = tk.Entry(master)
        self.reminder_entry.insert(0, "5")  # default 5 minutes
        self.reminder_entry.pack()

        # Buttons
        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=5)
        tk.Button(btn_frame, text="Add Task", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Edit Task", command=self.edit_task).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Task", command=self.delete_task).grid(row=0, column=2, padx=5)

        # Task List
        self.task_list = tk.Listbox(master, width=120, height=15)
        self.task_list.pack(pady=5)
        self.task_list.bind("<Double-1>", lambda e: self.edit_task())

        # Progress bar
        self.progress = ttk.Progressbar(master, length=400, mode="determinate")
        self.progress.pack(pady=5)

        # Status change buttons
        status_frame = tk.Frame(master)
        status_frame.pack(pady=5)
        tk.Button(status_frame, text="Start Task", command=lambda: self.change_status("Work in Progress")).grid(row=0, column=0, padx=5)
        tk.Button(status_frame, text="Finish Task", command=lambda: self.change_status("Finished")).grid(row=0, column=1, padx=5)

        self.update_task_list()

        # Background thread for alarms
        threading.Thread(target=self.deadline_checker, daemon=True).start()

    def add_task(self):
        task_name = self.task_input.get().strip()
        priority = self.priority_var.get()
        deadline_date_str = self.deadline_calendar.get_date()
        deadline_time_str = self.deadline_time_entry.get().strip()
        reminder_minutes = int(self.reminder_entry.get() or 0)

        if not task_name:
            messagebox.showerror("Error", "Task name cannot be empty")
            return

        deadline_datetime = None
        if deadline_date_str and deadline_time_str:
            try:
                deadline_date = datetime.strptime(deadline_date_str, "%Y-%m-%d").date()
                hours, minutes = map(int, deadline_time_str.split(":"))
                deadline_datetime = datetime.combine(deadline_date, datetime.min.time()).replace(hour=hours, minute=minutes)
            except:
                messagebox.showerror("Error", "Invalid date/time format")
                return

        task = {
            "name": task_name,
            "status": "To Do",
            "priority": priority,
            "deadline": deadline_datetime.isoformat() if deadline_datetime else None,
            "reminder_minutes": reminder_minutes,
            "notified": False
        }
        self.tasks.append(task)
        self.save_tasks()
        self.update_task_list()

    def edit_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            new_name = simpledialog.askstring("Edit Task", "Enter new task name:", initialvalue=task["name"])
            if new_name:
                task["name"] = new_name.strip()
                self.save_tasks()
                self.update_task_list()

    def delete_task(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            if messagebox.askyesno("Confirm", "Delete this task?"):
                del self.tasks[selected_index[0]]
                self.save_tasks()
                self.update_task_list()

    def change_status(self, new_status):
        selected_index = self.task_list.curselection()
        if selected_index:
            self.tasks[selected_index[0]]["status"] = new_status
            self.save_tasks()
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["status"] == "Finished")
        self.progress["value"] = (completed / total) * 100 if total > 0 else 0

        for task in self.tasks:
            deadline_str = ""
            color = "black"
            if task["deadline"]:
                deadline = datetime.fromisoformat(task["deadline"])
                if deadline < datetime.now():
                    color = "red"  # overdue
                deadline_str = f" (Deadline: {deadline.strftime('%Y-%m-%d %H:%M')})"

            self.task_list.insert(tk.END, f"{task['status']} | {task['name']} | Priority: {task['priority']}{deadline_str}")
            self.task_list.itemconfig(tk.END, {'fg': color})

    def save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                self.tasks = json.load(f)

    def deadline_checker(self):
        while True:
            now = datetime.now()
            for task in self.tasks:
                if task["deadline"] and not task["notified"] and task["status"] != "Finished":
                    deadline = datetime.fromisoformat(task["deadline"])
                    reminder_time = deadline - timedelta(minutes=task["reminder_minutes"])
                    if now >= reminder_time:
                        self.show_notification(task["name"], deadline)
                        task["notified"] = True
                        self.save_tasks()
            time.sleep(60)  # check every minute

    def show_notification(self, task_name, deadline):
        # Play sound alert
        winsound.Beep(1000, 1000)  # 1-second beep
        # System notification
        notification.notify(
            title="Task Reminder",
            message=f"Task '{task_name}' is due at {deadline.strftime('%H:%M')}",
            timeout=10
        )
        # Tkinter popup
        messagebox.showinfo("Reminder", f"Task '{task_name}' is due soon!")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class NoteOrganizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Note Organizer")

        # Create a database connection
        self.conn = sqlite3.connect('notes.db')
        self.c = self.conn.cursor()

        # Create notes table if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS notes
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          title TEXT NOT NULL,
                          content TEXT NOT NULL,
                          priority TEXT,
                          created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                          updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()

        # Label for title
        self.title_label = tk.Label(master, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        # Entry for title
        self.title_entry = tk.Entry(master, width=40)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        # Label for content
        self.content_label = tk.Label(master, text="Content:")
        self.content_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        # Text area for content
        self.content_text = tk.Text(master, height=10, width=50)
        self.content_text.grid(row=1, column=1, padx=10, pady=5)

        # Label for priority
        self.priority_label = tk.Label(master, text="Priority:")
        self.priority_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        # Entry for priority
        self.priority_entry = ttk.Combobox(master, values=["Low", "Medium", "High"], width=10)
        self.priority_entry.grid(row=2, column=1, padx=10, pady=5)

        # Button to add note
        self.add_button = ttk.Button(master, text="Add Note", command=self.add_note)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Button to update note
        self.update_button = ttk.Button(master, text="Update Note", command=self.update_note)
        self.update_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Button to delete note
        self.delete_button = ttk.Button(master, text="Delete Note", command=self.delete_note)
        self.delete_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        # Search entry and button
        self.search_entry = tk.Entry(master, width=40)
        self.search_entry.grid(row=6, column=0, padx=10, pady=5)
        self.search_button = ttk.Button(master, text="Search", command=self.search_note)
        self.search_button.grid(row=6, column=1, padx=10, pady=5)

        # Treeview to display notes
        self.tree = ttk.Treeview(master, columns=("Title", "Content", "Priority", "Created At", "Updated At"))
        self.tree.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Title')
        self.tree.heading('#2', text='Content')
        self.tree.heading('#3', text='Priority')
        self.tree.heading('#4', text='Created At')
        self.tree.heading('#5', text='Updated At')
        self.tree.bind('<ButtonRelease-1>', self.select_note)

        # Populate notes tree
        self.populate_notes()

    def add_note(self):
        # Get title, content, and priority from entry fields
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END)
        priority = self.priority_entry.get()

        if title.strip() == "":
            messagebox.showerror("Error", "Title cannot be empty.")
            return

        # Insert note into database
        self.c.execute("INSERT INTO notes (title, content, priority) VALUES (?, ?, ?)", (title, content, priority))
        self.conn.commit()

        # Clear entry fields
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
        self.priority_entry.set("")

        # Update notes tree
        self.populate_notes()

    def update_note(self):
        # Get selected note ID
        try:
            item = self.tree.selection()[0]
            note_id = self.tree.item(item, "text")
        except IndexError:
            messagebox.showerror("Error", "Please select a note to update.")
            return

        # Get title, content, and priority from entry fields
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END)
        priority = self.priority_entry.get()

        if title.strip() == "":
            messagebox.showerror("Error", "Title cannot be empty.")
            return

        # Update note in database
        self.c.execute("UPDATE notes SET title=?, content=?, priority=?, updated_at=CURRENT_TIMESTAMP WHERE id=?", 
                       (title, content, priority, note_id))
        self.conn.commit()

        # Update notes tree
        self.populate_notes()

    def delete_note(self):
        # Get selected note ID
        try:
            item = self.tree.selection()[0]
            note_id = self.tree.item(item, "text")
        except IndexError:
            messagebox.showerror("Error", "Please select a note to delete.")
            return

        # Confirm deletion with user
        confirm = messagebox.askyesno("Delete Note", "Are you sure you want to delete this note?")

        if confirm:
            # Delete note from database
            self.c.execute("DELETE FROM notes WHERE id=?", (note_id,))
            self.conn.commit()

            # Update notes tree
            self.populate_notes()

    def search_note(self):
        # Clear existing notes from tree
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Get search query
        query = self.search_entry.get()

        # Fetch notes from database based on search query
        self.c.execute("SELECT * FROM notes WHERE title LIKE ? OR content LIKE ?", ('%' + query + '%', '%' + query + '%'))
        notes = self.c.fetchall()

        # Populate notes tree with fetched notes
        for note in notes:
            self.tree.insert("", tk.END, text=note[0], values=(note[1], note[2], note[3], note[4], note[5]))

    def populate_notes(self):
        # Clear existing notes from tree
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch notes from database
        self.c.execute("SELECT * FROM notes")
        notes = self.c.fetchall()

        # Populate notes tree with fetched notes
        for note in notes:
            self.tree.insert("", tk.END, text=note[0], values=(note[1], note[2], note[3], note[4], note[5]))

    def select_note(self, event):
        # Get selected note ID
        item = self.tree.selection()[0]
        note_id = self.tree.item(item, "text")

        # Fetch note details from database
        self.c.execute("SELECT * FROM notes WHERE id=?", (note_id,))
        note = self.c.fetchone()

        # Display selected note details in entry fields
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, note[1])
        self.content_text.delete("1.0", tk.END)
        self.content_text.insert("1.0", note[2])
        self.priority_entry.set(note[3])

def main():
    root = tk.Tk()
    app = NoteOrganizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

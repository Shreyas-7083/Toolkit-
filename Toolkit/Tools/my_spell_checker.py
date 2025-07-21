import tkinter as tk
from tkinter import messagebox
from spellchecker import SpellChecker  


class SpellCheckerApp:
    def __init__(self, master):
        self.master = master
        master.title("Spell Checker")

        self.label = tk.Label(master, text="Enter text:")
        self.label.pack()

        self.textbox = tk.Text(master, height=10, width=50)
        self.textbox.pack()

        self.check_button = tk.Button(master, text="Check Spelling", command=self.check_spelling)
        self.check_button.pack()

    def check_spelling(self):
        text = self.textbox.get("1.0", "end-1c")
        spell = SpellChecker()
        misspelled = spell.unknown(text.split())

        if len(misspelled) == 0:
            messagebox.showinfo("Spell Check", "No misspelled words found!")
        else:
            suggestion_message = "Misspelled words found:\n"
            for word in misspelled:
                suggestions = spell.candidates(word)
                suggestion_message += f"{word}: {', '.join(suggestions)}\n"
            messagebox.showinfo("Spell Check", suggestion_message)

def main():
    root = tk.Tk()
    app = SpellCheckerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk

class RecipeManagerApp:
    def __init__(self, master):
        self.master = master
        master.title("Recipe Manager")

        self.recipes = []

        self.label = tk.Label(master, text="Recipe Manager", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry fields for adding recipes
        self.name_label = tk.Label(master, text="Recipe Name:")
        self.name_label.grid(row=1, column=0, padx=10, sticky=tk.E)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=1, column=1)

        self.ingredients_label = tk.Label(master, text="Ingredients:")
        self.ingredients_label.grid(row=2, column=0, padx=10, sticky=tk.E)

        self.ingredients_entry = tk.Text(master, height=10, width=50)
        self.ingredients_entry.grid(row=2, column=1)

        self.instructions_label = tk.Label(master, text="Instructions:")
        self.instructions_label.grid(row=3, column=0, padx=10, sticky=tk.E)

        self.instructions_entry = tk.Text(master, height=10, width=50)
        self.instructions_entry.grid(row=3, column=1)

        # Button to add recipe
        self.add_button = ttk.Button(master, text="Add Recipe", command=self.add_recipe)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Listbox to display recipe names
        self.recipe_list = tk.Listbox(master, height=15, width=30)
        self.recipe_list.grid(row=5, column=0, pady=10)

        # Text widget to display recipe details
        self.details_text = tk.Text(master, height=20, width=50)
        self.details_text.grid(row=5, column=1, padx=10)

        # Bind the listbox selection event to a method
        self.recipe_list.bind("<<ListboxSelect>>", self.show_recipe_details)

    def add_recipe(self):
        # Get the recipe details from the entry fields
        name = self.name_entry.get()
        ingredients = self.ingredients_entry.get("1.0", tk.END).strip()
        instructions = self.instructions_entry.get("1.0", tk.END).strip()

        if name and ingredients and instructions:
            # Add the recipe to the list of recipes
            self.recipes.append({"name": name, "ingredients": ingredients, "instructions": instructions})
            # Update the listbox with the recipe names
            self.update_recipe_list()
            # Clear the entry fields after adding the recipe
            self.clear_entry_fields()
        else:
            # Display a warning if any field is empty
            tk.messagebox.showwarning("Warning", "Please fill in all fields.")

    def update_recipe_list(self):
        # Clear the existing items in the listbox
        self.recipe_list.delete(0, tk.END)
        # Add each recipe name to the listbox
        for recipe in self.recipes:
            self.recipe_list.insert(tk.END, recipe["name"])

    def clear_entry_fields(self):
        # Clear the entry fields after adding a recipe
        self.name_entry.delete(0, tk.END)
        self.ingredients_entry.delete("1.0", tk.END)
        self.instructions_entry.delete("1.0", tk.END)

    def show_recipe_details(self, event):
        # Get the selected recipe index from the listbox
        index = self.recipe_list.curselection()
        if index:
            # Clear the existing text in the details text widget
            self.details_text.delete("1.0", tk.END)
            # Get the recipe details based on the selected index
            selected_recipe = self.recipes[index[0]]
            # Display the ingredients and instructions of the selected recipe
            self.details_text.insert(tk.END, f"Ingredients:\n{selected_recipe['ingredients']}\n\n")
            self.details_text.insert(tk.END, f"Instructions:\n{selected_recipe['instructions']}")

def main():
    root = tk.Tk()
    app = RecipeManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

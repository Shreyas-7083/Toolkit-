import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

class MathSolverApp:
    def __init__(self, master):
        self.master = master
        master.title("Math Solver")

        self.label = tk.Label(master, text="Math Solver", font=("Arial", 18))
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        # Entry fields for equation input
        self.equation_label = tk.Label(master, text="Equation:")
        self.equation_label.grid(row=1, column=0, padx=10, sticky=tk.E)

        self.equation_entry = tk.Entry(master, width=40)
        self.equation_entry.grid(row=1, column=1)

        # Button to solve equation
        self.solve_button = ttk.Button(master, text="Solve", command=self.solve_equation)
        self.solve_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Label to display solution
        self.solution_label = tk.Label(master, text="")
        self.solution_label.grid(row=3, column=0, columnspan=2, pady=10)

        # Button to plot solution
        self.plot_button = ttk.Button(master, text="Plot Solution", command=self.plot_solution)
        self.plot_button.grid(row=4, column=0, columnspan=2, pady=10)

    def solve_equation(self):
        # Get equation from entry field
        equation_str = self.equation_entry.get()

        try:
            # Parse equation using SymPy
            x = symbols('x')
            equation = Eq(eval(equation_str), 0)

            # Solve equation
            solution = solve(equation, x)

            # Display solution
            self.solution_label.config(text=f"Solution: {solution}")
        except Exception as e:
            # Display error if equation is invalid
            messagebox.showerror("Error", f"Invalid equation: {str(e)}")

    def plot_solution(self):
        # Get equation from entry field
        equation_str = self.equation_entry.get()

        try:
            # Parse equation using SymPy
            x = symbols('x')
            equation = eval(equation_str)

            # Generate x values for plotting
            x_values = np.linspace(-10, 10, 400)
            y_values = np.array([equation.subs(x, val) for val in x_values])

            # Plot equation
            plt.figure()
            plt.plot(x_values, y_values)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Solution Plot')
            plt.grid(True)
            plt.show()
        except Exception as e:
            # Display error if equation is invalid
            messagebox.showerror("Error", f"Invalid equation: {str(e)}")

def main():
    root = tk.Tk()
    app = MathSolverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

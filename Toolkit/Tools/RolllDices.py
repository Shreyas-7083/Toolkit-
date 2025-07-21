from tkinter import *
import random
from tkinter import ttk
import tkinter as tk


class RollDicesClass:
    def __init__(self, window):
        self.window = window
        self.window.title("RollDices")
        self.window.geometry("1000x600+400+170")
        self.window.config(bg="white")
        self.window.resizable(False,False)

        label=Label(self.window,text=" ",font=("times",260))
        
        image_icon= PhotoImage(file="Img\RollDices.png")
        self.window.iconphoto(False,image_icon)

        def roll():
            dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
            label.configure(text=f'{random.choice(dice)}{random.choice(dice)}{random.choice(dice)}')
            label.pack()

        self.button=Button(self.window,text="lets roll...",width=40,height=5,font=10,bg='white',bd=2,command=roll)
        self.button.pack(padx=10,pady=10)


if __name__=="__main__":
            window=Tk()
            obj = RollDicesClass(window)
            window.mainloop()
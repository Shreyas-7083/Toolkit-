from fileinput import filename
import os
from tkinter import *
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

class WhiteBoardClass:
    def __init__(self, window):
        self.window = window
        self.window.title("WhiteBoard")
        self.window.geometry("1000x600+400+170")
        self.window.config(bg="white")
        self.window.resizable(False,False)
        
        self.current_x=0
        self.current_y=0
        self.color = 'black'

        def locate_xy(work):
            self.current_x = work.x
            self.current_y = work.y
        
        def addLine(work):
                canvas.create_line ((self.current_x,self.current_y,work.x,work.y),width=get_current_value(),fill=self.color,capstyle=ROUND,smooth=TRUE)
                self.current_x, self.current_y = work.x ,work.y

        def show_color(new_color):
                self.color = new_color
        
        def new_canvas():
                canvas.delete('all')
                display_pallete()

        def insertimage():
              filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetype=(("PNG file","*.png"),("All file","new.txt")))
              
              f_img=tk.PhotoImage(file=filename)
              self.my_img=canvas.create_image(180,50,image=f_img)
              self.window.bind("<B3-Motion>",my_callback)

              def my_callback(event):
                  global f_img
                  f_img=tk.PhotoImage(file=filename)
                  self.my_img=Canvas.create_image(event.x,event.y,image=f_img)
        #icon
        image_icon= PhotoImage(file="Img/white_board_logo.png")
        self.window.iconphoto(False,image_icon)
        
        eraser=PhotoImage(file="Img/eraser_logo.png")
        width = 30
        height = 30
        eraser = eraser.subsample(eraser.width() // width, eraser.height() // height)
        eraser_btn=Button(self.window, image=eraser,bg="#f2f3f5",command=new_canvas)
        eraser_btn.image=eraser
        eraser_btn.place(x=30,y=400)
        
        importimage=PhotoImage(file="Img/addimage.png")
        width=30
        height=30
        importimage = importimage.subsample(importimage.width() // width, importimage.height() // height)
        Button(self.window,image=importimage,bg="white",command=insertimage).place(x=30,y=450)
        Button.image=importimage
        
               
        colors=Canvas(self.window,bg="#ffffff",width=37,height=300,bd=0)
        colors.place(x=30,y=60)

        def display_pallete():
                id = colors.create_rectangle((10,10,30,30),fill='black')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

                id = colors.create_rectangle((10,40,30,60),fill='gray')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('gray'))

                id = colors.create_rectangle((10,70,30,90),fill='brown4')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('brown4'))

                id = colors.create_rectangle((10,100,30,120),fill='orange')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('orange'))

                id = colors.create_rectangle((10,130,30,150),fill='yellow')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))
        
                id = colors.create_rectangle((10,160,30,180),fill='green')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))

                id = colors.create_rectangle((10,190,30,210),fill='blue')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

                id = colors.create_rectangle((10,220,30,240),fill='purple')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('purple'))

                id = colors.create_rectangle((10,250,30,270),fill='pink')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('pink'))

                id = colors.create_rectangle((10,280,30,300),fill='red')
                colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))
                  
        display_pallete()

        canvas=Canvas(self.window,width=930,height=500,background="white",cursor="hand2")
        canvas.place(x=100,y=10)

        canvas.bind('<Button-1>', locate_xy)
        canvas.bind('<B1-Motion>',addLine)

        # #slider

        current_value =tk.DoubleVar()

        def get_current_value():
                return '{: .2f}'.format(current_value.get())
        
        def slider_changed(event):
                value_label.configure(text=get_current_value())

        slider = ttk.Scale(self.window,from_=0,to=100,orient='horizontal',command=slider_changed, variable=current_value)
        slider.place(x=30,y=530)

            #value label
        value_label = ttk.Label(self.window,text=get_current_value())
        value_label.place(x=27,y=550)

if __name__=="__main__":
    window=Tk()
    obj = WhiteBoardClass(window)
    window.mainloop()
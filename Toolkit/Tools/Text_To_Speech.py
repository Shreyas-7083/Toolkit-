from tkinter import *
import tkinter
import pyttsx3
engine=pyttsx3.init()

class Text_To_SpeechClass:
    def __init__(self, window):
        self.window = window
        self.window.title("Text To Speech")
        self.window.geometry("1000x600+500+170")
        self.window.config(bg="white")
        self.window.resizable(False,False)

        image_icon= PhotoImage(file="Img\Text_To_Speech.png")
        self.window.iconphoto(False,image_icon)
    
        def speaknow():
            engine.say(textv.get())
            engine.runAndWait()
            engine.stop()

        textv=StringVar()

        obj=LabelFrame(self.window,text="Text To Speech",font=20,bd=1)
        obj.pack(fill="both",expand="yes",padx=10,pady=10)

        lbl=Label(obj,text="Text",font=30)
        lbl.pack(side=tkinter.LEFT,padx=5)

        text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
        text.pack(side=tkinter.LEFT,padx=10)

        btn=Button(obj,text="Speak",font=20,bg="black",fg="white",command=speaknow)
        btn.pack(side=tkinter.LEFT,padx=10)


if __name__=="__main__":
    window=Tk()
    obj = Text_To_SpeechClass(window)
    window.mainloop()
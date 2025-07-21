from tkinter import *
from tkinter import filedialog
class NotepadClass:


    def __init__(self,window):

        self.window=window
        self.window.title("Notepad")
        self.window.geometry("600x600+500+170")
        self.window.config(bg='gray')
        self.window.resizable(False,False)
        self.window.focus_force()
        # image_icon=PhotoImage(file="img/notepad_logo.png")
        # self.window.iconphoto(False,image_icon)

        def saveFile():
            openFile=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
            if openFile is None:
                return
            text=str(entry.get(1.0,END))
            openFile.write(text)
            openFile.close()
        def openFile():
            file=filedialog.askopenfile(mode='r',filetypes=[('text file','*.txt')])
            if file is not None:
                content=file.read()
            entry.insert(INSERT,content)


        save_btn=Button(self.window,text="Save File",width='20',height='2',bg="#fff",command=saveFile)
        save_btn.place(x=100,y=5)

        open_btn=Button(self.window,text="Open File",width='20',height='2',bg="#fff",command=openFile)
        open_btn.place(x=300,y=5)

        entry=Text(self.window,height='33',width='72',wrap=WORD)
        entry.place(x=10,y=60)
if __name__=="__main__":
    window=Tk()
    obj=NotepadClass(window)
    window.mainloop()
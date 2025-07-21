from tkinter import *
from tkinter import filedialog
import qrcode
class QRGeneratorClass:


    def __init__(self,window):

        self.window=window
        self.window.title("QR Generator")
        self.window.geometry("1000x550+400+170")
        self.window.config(bg='#AE2321')
        self.window.resizable(False,False)
        self.window.focus_force()

        image_icon=PhotoImage(file="img/qr_page_logo.png")
        self.window.iconphoto(False,image_icon)

        def generate():
            name=title_entry.get()
            txt=e_entry.get()
            qr=qrcode.make(txt)
            qr.save("Qrcodes/"+ str(name) + ".png")

            global img
            img=PhotoImage(file="Qrcodes/"+ str(name) + ".png")
            image_view.config(image=img)

        image_view=Label(self.window,bg="#AE2321")
        image_view.pack(padx=50,pady=10,side=RIGHT)

        title_lbl=Label(self.window,text="Title",fg="White",bg="#AE2321",font=15)
        title_lbl.place(x=50,y=170)

        title_entry=Entry(self.window,width=13,font="Arial,15")
        title_entry.place(x=50,y=200)
        
        e_entry=Entry(self.window,width=28,font="Arial,15")
        e_entry.place(x=50,y=250)
        
        btn=Button(self.window,text="Generate",width=20,height=2,bg="Black",fg="White",command=generate)
        btn.place(x=50,y=300)

        

if __name__=="__main__":
    window=Tk()
    obj=QRGeneratorClass(window)
    window.mainloop()

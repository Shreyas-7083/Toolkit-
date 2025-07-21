import os
from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
class PDFViewerClass:


    def __init__(self,window):

        self.window=window
        self.window.title("PDF Viewer")
        self.window.geometry("630x600+500+170")
        self.window.config(bg='white')
        self.window.resizable(False,False)
        self.window.focus_force()
        # image_icon=PhotoImage(file="img/pdf_logo.png")
        # self.window.iconphoto(False,image_icon)

        def BrowesFile():
            filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select PDF File",filetype=(("PDF File",".pdf"),("PDF File",".PDF"),("All File",".txt")))
            v1=pdf.ShowPdf()
            v2=v1.pdf_view(self.window,pdf_location=open(filename,"r"),width=77,height=100)
            v2.pack(pady=(0,0))

        btn=Button(self.window,text="Open",width=30,font="Arial 10",bd=4,command=BrowesFile)
        btn.pack()


if __name__=="__main__":
    window=Tk()
    obj=PDFViewerClass(window)
    window.mainloop()
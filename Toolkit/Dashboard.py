import time
from tkinter import *
from Calculator import CalculatorClass
from Notepad import NotepadClass
from PDFViewer import PDFViewerClass
from QRGenerator import QRGeneratorClass
from RolllDices import RollDicesClass
from SpeedTest import SpeedTestClass
from Text_To_Speech import Text_To_SpeechClass
from Translator import TranslatorClass
from Wheather import WheatherClass
from WhiteBoard import WhiteBoardClass
from WorldClock import WorldClockClass

class DashboardClass:
    def __init__(self,window):
        self.window=window
        self.window.state('zoomed')
        self.window.title("Dashboard")
        self.win_width=window.winfo_screenwidth()
        self.win_height=window.winfo_screenheight()
        self.window.geometry("%dx%d"%(self.win_width,self.win_height))
        self.window.config(bg='#FFFFFF')
    
        #title
        title=Label(self.window,text='TOOLKIT',compound=LEFT,font=('Georgia',30,'bold'),bg='#575200',fg='White',anchor="w",padx=20)
        title.place(x=0,y=0,relwidth=1,height=70)

        #welcome title with clock
        self.lbl_clock=Label(self.window,text='Welcome To Tookit \t\t\t\t Date:dd-mm-yyyy\t\t Time:hh:mm:ss',font=('Georgia',15),bg='#8a6626',fg='White')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #Menu Frame------------------------------------------------------------------------------------------------------
        self.menu_frame=Frame(self.window,borderwidth=2,background="antique white",highlightcolor="Black")
        self.menu_frame.place(x=0,y=100,relwidth=1,height=44)

        Label(self.menu_frame,text=" MENU => ",font=('TIMES NEW ROMAN',20,"bold"),bg="#A3842C",fg="antique white").place(x=10)
        self.home_btn=Button(self.menu_frame,text="HOME",font=('TIMES NEW ROMAN',16),bg="#A3842C",fg='antique white',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.home)
        self.home_btn.place(x=220)
        

        self.office_btn=Button(self.menu_frame,text="OFFICE",font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.officeTools)
        self.office_btn.place(x=360)

        self.student_btn=Button(self.menu_frame,text="STUDENTS",font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.studentTools)
        self.student_btn.place(x=500)

        self.kids_btn=Button(self.menu_frame,text="KIDS",font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.kidsTools)
        self.kids_btn.place(x=670)

        self.house_btn=Button(self.menu_frame,text="HOUSE HOLD",font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.houseTools)
        self.house_btn.place(x=780)

        self.about_btn=Button(self.menu_frame,text="ABOUT US",font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.about)
        self.about_btn.place(x=980)
        #---------------------------------------------------------------------------------------------------------------
        self.welcome1=Label(self.window,text="Welcome to Toolkit!",font=('TIMES NEW ROMAN',40,"bold","underline"),fg="Black").place(x=550,y=200)
        self.welcome2=Label(self.window,text="Time is your most valuable asset. \n Use it wisely and let Toolkit simplify your tasks, \nsaving you time for what truly matters.",font=('TIMES NEW ROMAN',15,"bold")).place(x=590,y=400)
        self.welcome3=Label(self.window,text="Toolkit is here to serve you, \nwhether you're a busy office employee, a diligent student, \na curious kid, or a household manager.\n Our versatile tools cater to your needs, making your daily tasks easier and more efficient. \nLet Toolkit be your companion in productivity and convenience,\n empowering you to accomplish more with less effort.",font=('TIMES NEW ROMAN',15,"bold"),fg="black").place(x=420,y=600)

        #---------------------------------------------------------------------------------------------------------------
        self.update_content()
    def home(self):
        self.menuContent()
        self.tool_frame.config(bg="White")
        self.home_btn.config(bg="#A3842C",fg="antique white")
        self.clear_frame()

    def officeTools(self):
        self.menuContent()
        self.office_btn.config(bg="#A3842C",fg="antique white")
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.tool_frame=Frame(self.window,bg="White",borderwidth=2,background="antique white",highlightcolor="Black")
        self.tool_frame.place(x=0,y=140,relheight=1,width=150)
        
        Label(self.tool_frame,text=" TOOLs ",width=250,font=('TIMES NEW ROMAN',20,"bold","underline"),bg="#A3842C",fg="antique white").pack(pady=(3,20))
        
        calculator_btn=Button(self.tool_frame,text="Calculator",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,relief="flat",command=self.calculator)
        calculator_btn.pack(pady=3)

        pdf_viewer_btn=Button(self.tool_frame,text="PDF Viewer",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,relief="flat",command=self.pdfViewer)
        pdf_viewer_btn.pack(pady=3)

        notepad_btn=Button(self.tool_frame,text="Notepad",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.notepad)
        notepad_btn.pack(pady=3)
        
        speed_test_btn=Button(self.tool_frame,text="SpeedTest",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.speedTest)
        speed_test_btn.pack(pady=3)

        white_board_btn=Button(self.tool_frame,text="White Board",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.whiteBoard)
        white_board_btn.pack(pady=3)

        world_clock_btn=Button(self.tool_frame,text="World Clock",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.wordClock)
        world_clock_btn.pack(pady=3)

        qr_generator_btn=Button(self.tool_frame,text="OR Generator",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.qrGenerator)
        qr_generator_btn.pack(pady=3)

        Weather_btn=Button(self.tool_frame,text="Wheather",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.wheather)
        Weather_btn.pack(pady=3)

        trance_btn=Button(self.tool_frame,text="Translator",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.translator)
        trance_btn.pack(pady=3)


    def studentTools(self):
        self.menuContent()
        self.student_btn.config(bg="#A3842C",fg="antique white")
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        
        self.tool_frame=Frame(self.window,bg="White",borderwidth=2,background="antique white",highlightcolor="Black")
        self.tool_frame.place(x=0,y=140,relheight=1,width=150)
        Label(self.tool_frame,text=" TOOLs ",width=250,font=('TIMES NEW ROMAN',20,"bold","underline"),bg="#A3842C",fg="antique white").pack(pady=(3,20))

        calculator_btn=Button(self.tool_frame,text="Calculator",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,relief="flat",command=self.calculator)
        calculator_btn.pack(pady=3)

        pdf_viewer_btn=Button(self.tool_frame,text="PDF Viewer",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,relief="flat",command=self.pdfViewer)
        pdf_viewer_btn.pack(pady=3)

        notepad_btn=Button(self.tool_frame,text="Notepad",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.notepad)
        notepad_btn.pack(pady=3)

        trance_btn=Button(self.tool_frame,text="Translator",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.translator)
        trance_btn.pack(pady=3)
        
        speed_test_btn=Button(self.tool_frame,text="SpeedTest",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.speedTest)
        speed_test_btn.pack(pady=3)

        white_board_btn=Button(self.tool_frame,text="White Board",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.whiteBoard)
        white_board_btn.pack(pady=3)

        world_clock_btn=Button(self.tool_frame,text="World Clock",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.wordClock)
        world_clock_btn.pack(pady=3)


        

    def kidsTools(self):
        self.menuContent()
        self.kids_btn.config(bg="#A3842C",fg="antique white")
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.tool_frame=Frame(self.window,bg="White",borderwidth=2,background="antique white",highlightcolor="Black")
        self.tool_frame.place(x=0,y=140,relheight=1,width=150)
        
        Label(self.tool_frame,text=" TOOLs ",width=250,font=('TIMES NEW ROMAN',20,"bold","underline"),bg="#A3842C",fg="antique white").pack(pady=(3,20))
        
        calculator_btn=Button(self.tool_frame,text="Calculator",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,relief="flat",command=self.calculator)
        calculator_btn.pack(pady=3)
        
        speed_test_btn=Button(self.tool_frame,text="SpeedTest",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.speedTest)
        speed_test_btn.pack(pady=3)

        white_board_btn=Button(self.tool_frame,text="White Board",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.whiteBoard)
        white_board_btn.pack(pady=3)

        world_clock_btn=Button(self.tool_frame,text="World Clock",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.wordClock)
        world_clock_btn.pack(pady=3)

        roll_dice_btn=Button(self.tool_frame,text="Roll Dice",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.rollDices)
        roll_dice_btn.pack(pady=3)

        trance_btn=Button(self.tool_frame,text="Translator",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.translator)
        trance_btn.pack(pady=3)


    def houseTools(self):
        self.menuContent()
        self.house_btn.config(bg="#A3842C",fg="antique white")
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.tool_frame=Frame(self.window,bg="White",borderwidth=2,background="antique white",highlightcolor="Black")
        self.tool_frame.place(x=0,y=140,relheight=1,width=150)
        
        Label(self.tool_frame,text=" TOOLs ",width=250,font=('TIMES NEW ROMAN',20,"bold","underline"),bg="#A3842C",fg="antique white").pack(pady=(3,20))
        
        calculator_btn=Button(self.tool_frame,text="Calculator",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,relief="flat",command=self.calculator)
        calculator_btn.pack(pady=3)

        
        speed_test_btn=Button(self.tool_frame,text="SpeedTest",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.speedTest)
        speed_test_btn.pack(pady=3)

        Weather_btn=Button(self.tool_frame,text="Wheather",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.wheather)
        Weather_btn.pack(pady=3)

        world_clock_btn=Button(self.tool_frame,text="World Clock",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.wordClock)
        world_clock_btn.pack(pady=3)

        trance_btn=Button(self.tool_frame,text="Translator",width=250,font=('TIMES NEW ROMAN',16),bg="antique white",fg='black',
                            cursor='hand2',activebackground="antique white",borderwidth=0,command=self.translator)
        trance_btn.pack(pady=3)


    def about(self):
        self.menuContent()
        self.about_btn.config(bg="#A3842C",fg="antique white")
        self.tool_frame.config(bg="white")
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.clear_frame()

        self.welcome1.config(text="hiii")
        self.welcome2.config(text="hello")
        self.welcome3.config(text="namaste")

    def clear_frame(self):
        print(self.tool_frame.winfo_children())
        for widgets in self.tool_frame.winfo_children():
            print(widgets)
            widgets.destroy()


    def calculator(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=CalculatorClass(self.new_win)

    def wheather(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=WheatherClass(self.new_win)

    def notepad(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=NotepadClass(self.new_win)

    def pdfViewer(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=PDFViewerClass(self.new_win)

    def qrGenerator(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=QRGeneratorClass(self.new_win)

    def wordClock(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=WorldClockClass(self.new_win)

    def speedTest(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=SpeedTestClass(self.new_win)

    def translator(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=TranslatorClass(self.new_win)

    def whiteBoard(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=WhiteBoardClass(self.new_win)

    def rollDices(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=RollDicesClass(self.new_win)   

    def textToSpeech(self):
        if hasattr(self, 'new_win') and isinstance(self.new_win, Toplevel):
            self.new_win.destroy()
        self.new_win=Toplevel(self.window)
        self.new_obj=Text_To_SpeechClass(self.new_win)

    def update_content(self):
        time1=time.strftime('%I:%M:%S')
        date1=time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f'Welcome To Tookit \t\t\t\t Date:{str(date1)}\t\t Time:{str(time1)}')
        self.lbl_clock.after(200,self.update_content) 

    def menuContent(self):
        self.office_btn.config(bg="antique white",fg="black")
        self.student_btn.config(bg="antique white",fg="black")
        self.kids_btn.config(bg="antique white",fg="black")
        self.about_btn.config(bg="antique white",fg="black")
        self.house_btn.config(bg="antique white",fg="black")
        self.home_btn.config(bg="antique white",fg="black")

    
        
if __name__=="__main__":
    window=Tk()
    obj=DashboardClass(window)
    window.mainloop()

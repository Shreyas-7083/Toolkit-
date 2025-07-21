from tkinter import *
import speedtest

class SpeedTestClass:
    def __init__(self, window):
        self.window = window
        self.window.title("Internet Speed Test")
        self.window.geometry("360x600+600+170")
        self.window.config(bg='#1a212d')
        self.window.resizable(False,False)
        self.window.focus_force()
        # image_icon=PhotoImage(file="img/speed_test_logo.png")
        # self.window.iconphoto(False,image_icon)

        def fun():
            test=speedtest.Speedtest()
            uploading=round(test.upload()/(1024*1024),2)
            upload.config(text=uploading)

            downloading=round(test.upload()/(1024*1024),2)
            download.config(text=downloading)
            download_main.config(text=downloading)

            servername=[]
            test.get_servers(servername)
            ping.config(text=test.results.ping)


        #images
        top_img=PhotoImage(file="img/netSpeed_top.png")
        top_img_lbl=Label(self.window,image=top_img,bg="#1a212d")
        top_img_lbl.image=top_img
        top_img_lbl.pack()

        main_img=PhotoImage(file="img/netSpeed_main.png")
        main_img_lbl=Label(self.window,image=main_img,bg="#1a212d")
        main_img_lbl.image=main_img
        main_img_lbl.pack(pady=(40,0))

        btn_img=PhotoImage(file="img/netSpeed_button.png")
        btn=Button(self.window,image=btn_img,bg="#1a212d",bd=0,activebackground="#1a212d",cursor="hand2",command=fun)
        btn.image=btn_img
        btn.pack(pady=10)

        # Label
        Label(self.window,text="PING",font="arial 10 bold",bg="#384056").place(x=50,y=0)
        Label(self.window,text="DOWNLOAD",font="arial 10 bold",bg="#384056").place(x=140,y=0)
        Label(self.window,text="UPLOAD",font="arial 10 bold",bg="#384056").place(x=260,y=0)

        Label(self.window,text="MS",font="arial 7 bold",bg="#384056",fg="white").place(x=60,y=80)
        Label(self.window,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=165,y=80)
        Label(self.window,text="MBPS",font="arial 7 bold",bg="#384056",fg="white").place(x=275,y=80)

        Label(self.window,text="Download",font="arial 15 bold",bg="#384056",fg="white").place(x=140,y=280)
        Label(self.window,text="MBPS",font="arial 15 bold",bg="#384056",fg="white").place(x=155,y=380)

        ping=Label(self.window,text="00",font="arial 13 bold",bg="#384056",fg="white")
        ping.place(x=70,y=60,anchor="center")

        download=Label(self.window,text="00",font="arial 13 bold",bg="#384056",fg="white")
        download.place(x=180,y=60,anchor="center")

        upload  =Label(self.window,text="00",font="arial 13 bold",bg="#384056",fg="white")
        upload  .place(x=290,y=60,anchor="center")

        download_main=Label(self.window,text="00",font="arial 40 bold",bg="#384056",fg="green")
        download_main.place(x=185,y=350,anchor="center")


if __name__ == "__main__":
    window = Tk()
    obj = SpeedTestClass(window)
    window.mainloop()

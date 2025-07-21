from tkinter import *
import requests
from tkinter import messagebox
from PIL import Image,ImageTk
class WheatherClass:

    def __init__(self,window):

        self.window=window
        self.window.title("Wheather")
        self.window.geometry("400x390+550+170")
        self.window.config(bg='light gray')
        self.window.resizable(False,False)
        self.window.focus_force()
        image_icon=PhotoImage(file="img/whether_logo.png")
        self.window.iconphoto(False,image_icon)

    #------------------------------------------------------------------------------------------
        #function to get whether info from openwheathermap Api
        def get_weather(city):
            API_key="1ebadbc6dd113031db0426be3e9b6681"
            url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
            res=requests.get(url)

            if res.status_code==404:
                messagebox.showerror("Error","City Not Found")
                return None
            #parse response JSON to information
            wheather=res.json()
            icon_id=wheather['weather'][0]['icon']
            tempreture=wheather['main']['temp']- 273.15
            description=wheather['weather'][0]['description']
            city=wheather['name']
            country=wheather['sys']['country']

            #get icon url
            icon_url=f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            return (icon_url,tempreture,description,city,country)
        #function to search city
        def search():
            city=city_entry.get()
            result=get_weather(city)
            if result is None:
                return
            #if city found unpack info
            icon_url,tempreture,description,city,country=result
            location_lbl.configure(text=f"{city}, {country}")

            #get icon from url
            image=Image.open(requests.get(icon_url,stream=True).raw)
            icon=ImageTk.PhotoImage(image)
            icon_lbl.configure(image=icon)
            icon_lbl.image=icon

            #update temp and desc lbl
            tepm_lbl.configure(text=f"Temperature : {tempreture:.2f}C")
            desc_lbl.configure(text=f"Desciption : {description}")
        #------------------------------------------------------------------------------------------
        #city name Entry
        city_entry=Entry(self.window,font=("Helvetica",18),justify="center",relief="ridge",bg="#f8efbb")
        city_entry.pack(pady=10)

        #search button
        
        search_btn=Button(self.window,text="Search",font=("Forte",14),cursor='hand2',command=search)
        search_btn.pack(pady=10)
        
        #Label to show city name
        location_lbl=Label(self.window,font=("Algerian",25),bg="light gray")
        location_lbl.pack(pady=20)

        #Label to show the whether icon
        icon_lbl=Label(self.window,bg="light gray")
        icon_lbl.pack()

        #Label to show tempreture
        tepm_lbl=Label(self.window,font=("Times New Roman",18),bg="light gray")
        tepm_lbl.pack()

        #Label to show wheather description
        desc_lbl=Label(self.window,font=("Times New Roman",18),bg="light gray")
        desc_lbl.pack()



if __name__=="__main__":
    window=Tk()
    obj=WheatherClass(window)
    window.mainloop()
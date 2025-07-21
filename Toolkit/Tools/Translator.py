from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from textblob import TextBlob
from langdetect import detect
import requests
class TranslatorClass:
    def __init__(self, window):
        self.window = window
        self.window.title("Translator")
        self.window.geometry("1000x600+400+170")
        self.window.config(bg="white")

        self.language = googletrans.LANGUAGES
        self.languageV = list(self.language.values())

        # combo1 = ttk.Combobox(self.window, values=languageV, font="Roboto 14", state="readonly")
        # combo1.place(x=10, y=20)
        # combo1.set("ENGLISH")
        self.combo1 = ttk.Combobox(self.window, values=self.languageV, font="Roboto 14", state="readonly")
        self.combo1.place(x=10, y=20)
        self.combo1.set("ENGLISH")

        label1 = Label(self.window, text="ENGLISH", font=("segoe", 30, "bold"), bg="white", width=18, bd=5, relief=GROOVE)
        label1.place(x=10, y=50)

        f = Frame(self.window, bg="Black", bd=5)
        f.place(x=10, y=118, width=440, height=210)

        self.text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text1.place(x=0, y=0, width=430, height=200)

        scrollbar1 = Scrollbar(f)
        scrollbar1.pack(side="right", fill="y")

        scrollbar1.configure(command=self.text1.yview)
        self.text1.configure(yscrollcommand=scrollbar1.set)

        # combo2 = ttk.Combobox(self.window, values=languageV, font="Roboto 14", state="readonly")
        # combo2.place(x=730, y=20)
        # combo2.set("SELECT LANGUAGE")
        

        self.combo2 = ttk.Combobox(self.window, values=self.languageV, font="Roboto 14", state="readonly")
        self.combo2.place(x=730, y=20)
        self.combo2.set("SELECT LANGUAGE")

        label2 = Label(self.window, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
        label2.place(x=620, y=50)

        f1 = Frame(self.window, bg="Black", bd=5)
        f1.place(x=620, y=118, width=440, height=210)

        self.text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
        self.text2.place(x=0, y=0, width=430, height=200)

        scrollbar2 = Scrollbar(f1)
        scrollbar2.pack(side="right", fill="y")

        scrollbar2.configure(command=self.text2.yview)
        self.text2.configure(yscrollcommand=scrollbar2.set)

        # Translate button
        translate = Button(self.window, text="Translate", font="Roboto 15 bold italic", activebackground="white",
                           cursor="hand2", bd=5, bg="red", fg="white", command=self.translate_now)
        translate.place(x=30, y=300)

    def translate_now(self):
        text_ = self.text1.get(1.0, END)
        print(text_)
        c2 = self.combo1.get()  # Changed from combo1 to self.combo1
        c3 = self.combo2.get()
        words = TextBlob(text_)
        print(words)
        if text_:
            try:
                words = TextBlob(text_)

                # lan = words.detect_language()
                lan = detect(text_)

                for i, j in self.language.items():
                    if j == c3:
                        lan_ = i
                words = words.translate(from_lang=lan, to=str(lan_))
                self.text2.delete(1.0, END)
                self.text2.insert(END, words)
            except Exception as e:
                messagebox.showerror("Translation Error", str(e))


if __name__ == "__main__":
    window = Tk()
    obj = TranslatorClass(window)
    window.mainloop()

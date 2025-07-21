import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from threading import Timer
import sounddevice as sd
import wavio
import os
from PIL import Image, ImageTk

class VoiceRecorderApp:
    def __init__(self, master):
        self.master = master
        master.title("Voice Recorder")

        self.frames = []
        self.recording = False
        self.duration = 0

        self.label = tk.Label(master, text="Voice Recorder", font=("Arial", 18))
        self.label.pack()

        # Button images
        self.start_img = Image.open("img/start_icon.png")
        self.stop_img = Image.open("img/stop_icon.png")

        # Resize button images
        self.start_img = self.start_img.resize((30, 30), Image.ANTIALIAS)
        self.stop_img = self.stop_img.resize((30, 30), Image.ANTIALIAS)

        # Convert button images to Tkinter PhotoImage
        self.start_icon = ImageTk.PhotoImage(self.start_img)
        self.stop_icon = ImageTk.PhotoImage(self.stop_img)

        # Create buttons with images
        self.start_button = ttk.Button(master, text="Start Recording", image=self.start_icon, compound=tk.LEFT, command=self.start_recording)
        self.start_button.pack()

        self.stop_button = ttk.Button(master, text="Stop Recording", image=self.stop_icon, compound=tk.LEFT, command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack()

        # Other GUI elements...
    def start_recording(self):
        self.recording = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.NORMAL)
        self.save_button.config(state=tk.DISABLED)

        self.frames = []
        self.start_timer()

        self.stream = sd.InputStream(callback=self.callback)
        self.stream.start()

    def stop_recording(self):
        self.recording = False
        self.stop_timer()
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.DISABLED)
        self.save_button.config(state=tk.NORMAL)

        self.stream.stop()
        self.stream.close()

    def pause_recording(self):
        if self.recording:
            self.recording = False
            self.stop_timer()
            self.pause_button.config(text="Resume Recording")
        else:
            self.recording = True
            self.start_timer()
            self.pause_button.config(text="Pause Recording")

    def start_timer(self):
        self.duration = 0
        self.update_duration()

    def stop_timer(self):
        pass

    def update_duration(self):
        if self.recording:
            self.duration += 1
            minutes = self.duration // 60
            seconds = self.duration % 60
            self.duration_label.config(text=f"Recording Duration: {minutes:02d}:{seconds:02d}")
            Timer(1, self.update_duration).start()

    def callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.frames.append(indata.copy())

    def save_recording(self):
        filename = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
        if filename:
            wavio.write(filename, self.frames, 44100, sampwidth=2)

def main():
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


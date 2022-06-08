from tkinter import Tk, Label
from tkinter.font import Font
from datetime import datetime

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")

label  = Label(window, font = ("Arial Black", 78, "bold"), bg= "steelblue", fg= "white")
label.pack(pady= 100)

def clock():
    time = datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500, clock)
clock()
window.mainloop()
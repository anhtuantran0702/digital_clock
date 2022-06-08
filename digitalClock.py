from tkinter import Tk, Label
from tkinter.font import Font

window = Tk()
window.title("Digital Clock")
window.geometry("600x300")

label  = Label(window, font = ("Arial Black", 78, "bold"), bg= "steelblue", fg= "white")
label.pack(pady= 100)
window.mainloop()
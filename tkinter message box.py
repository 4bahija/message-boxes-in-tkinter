import tkinter as tk
from tkinter.messagebox import showerror,showinfo,showwarning
win = tk.Tk()

def error():
    showerror("ERROR","this is error box")

def info():
    showinfo("INFO","this is information box")

def warning():
    showwarning("WARNING","alert you did it wrong")

button1=tk.Button(win,text="ERROR",command=error).grid(row=0,column=0)
button2=tk.Button(win,text="INFO",command=info).grid(row=0,column=1)
button3=tk.Button(win,text="WARNING",command=warning).grid(row=0,column=2)

win.mainloop()


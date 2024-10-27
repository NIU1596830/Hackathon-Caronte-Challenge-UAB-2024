import tkinter as tk

def app():
    window = tk.Tk()

    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()

    window.mainloop()
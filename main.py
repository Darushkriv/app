import kivy
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from kivy.app import App
from kivy.uix.button import Button

FILE_NAME = tkinter.NONE


class MyApp(App):
    def build(self):
        return Button(text='Hello World')


def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)


def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()


def save_as():
    out = asksaveasfile(mode='w', defaultextension='txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Error", message="Saving file error")


def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)


def info():
    messagebox.showinfo("Information", "Simple text editor\nby CodeLog")


root = tkinter.Tk()
root.title("Simple reader")

root.minsize(width=350, height=500)
root.maxsize(width=350, height=500)

text = tkinter.Text(root, bg="light yellow", width=700, height=800, wrap="word")
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)

text.pack()
menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Info", command=info)
menuBar.add_cascade(label="Exit", command=root.quit)

root.config(menu=menuBar)

if __name__ == '__main__':
    MyApp().run()
root.mainloop()

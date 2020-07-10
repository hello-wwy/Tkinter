import tkinter as tk
import tkinter.messagebox

class Myframe:
    def __init__(self):
        window.title('second')
        window.geometry('600x400')
        b1.pack()
        b2.pack()
        window.mainloop()

window = tk.Tk()
def exit():
    tk.messagebox.askyesno(title='Confirm Exit',message='确认退出么？')

def select():
    tk.messagebox.showerror(title='error',message='出错了！')
b1 = tk.Button(window,text='退出',command=exit)
b2 = tk.Button(window,text='选择',command=select)
Myframe()

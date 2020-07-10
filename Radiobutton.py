import tkinter as tk

class Myframe:
    def __init__(self):
        window.title('second')
        window.geometry('600x400')
        window.mainloop()

window = tk.Tk()
var = tk.StringVar()
label = tk.Label(window,text='',bg='yellow',width=25)
label.pack()

def select():
    label.config(text='你选择了'+var.get())

# 因为是单选框，选项互斥，同一组内的所有Radiobutton只能共享一个variable选项，并且需要设置不同的value选项值
r1 = tk.Radiobutton(window,text='选项A',variable=var,value='A',command=select)
r1.pack()
r2 = tk.Radiobutton(window,text='选项B',variable=var,value='B',command=select)
r2.pack()
Myframe()
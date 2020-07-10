import tkinter as tk

class Myframe:
    def __init__(self):
        window.title('menubar')
        window.geometry('600x400')
        window.config(menu=menubar)
        l.pack()
        window.mainloop()
num = 0
def do():
    global num
    l.config(text='do '+str(num))
    num += 1
window = tk.Tk()
l = tk.Label(window,text="now it's empty",bg='yellow')
menubar = tk.Menu(window)                         # 创建菜单栏
filemenu = tk.Menu(menubar,tearoff=0)             # 创建一个 filemenu菜单项, tearoff=0表示菜单不能独立出来
menubar.add_cascade(label='file',menu=filemenu)   # 将上面定义的空菜单命名为File，放在菜单栏中
filemenu.add_command(label='New',command=do)
filemenu.add_command(label='Open', command=do)

Myframe()
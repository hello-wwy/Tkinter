'''
grid 是方格, 所有的内容会被放在规律的方格中。
pack()会按照上下左右的方式排列
place(),按坐标定位
'''
import tkinter as tk

class Myframe:
    def __init__(self):
        window.title('second')
        window.geometry('600x400')
        window.mainloop()
window = tk.Tk()
tk.Label(window,text='账号').grid(row=0)
tk.Label(window,text='密码').grid(row=1)

tk.Entry(window).grid(row=0,column=1)
tk.Entry(window).place(x=50,y=100,anchor='nw')

Myframe()

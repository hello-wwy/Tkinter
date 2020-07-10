# 文本写入口，文本区，下拉列表
import tkinter as tk
from tkinter import ttk   # 下拉菜单控件在ttk

window = tk.Tk()
window.title('second')
window.geometry('600x400')

e = tk.Entry(window,show=None)
e.pack()

def insert(*args):   # *args表示可变参数
    var = e.get()
    if com.get()=='insert_end':
        text.insert('end',var)
    else:
        text.insert('insert',var)

com = ttk.Combobox(window)   # 创建下拉菜单
com['value'] = ('insert_end','insert_now')   # 设置下拉菜单中的值
# com.current(0)     # 设置默认值，即默认下拉框中的内容
com.bind('<<ComboboxSelected>>',insert)
com.pack()

text = tk.Text(window)
text.pack()

window.mainloop()
import tkinter as tk

window = tk.Tk()
window.title('first')
window.geometry('600x400')
var = tk.StringVar()   # 跟踪变量的值的变化
label = tk.Label(window,textvariable=var,bg='yellow',width=20,height=2)  # Label标签,使用 textvariable替换text,因为这个是可以变化的,fg 前景色，也就是字体的颜色，bg 背景颜色
label.pack()

onhit = False
def hit():
    global onhit
    if onhit == False:
        onhit = True
        var.set('you hit me!')
    else:
        onhit = False
        var.set('')

button = tk.Button(window,text='Hit !',command=hit)
button.pack()    # 自动调节窗口位置

window.mainloop()
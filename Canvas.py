# Canvas：画布，提供绘图功能(直线、椭圆、多边形、矩形) 可以包含图形或位图，用来绘制图表和图，创建图形编辑器，实现定制窗口部件。
import tkinter as tk
from PIL import ImageTk,Image

class Myframe:
    def __init__(self):
        window.title('second')
        window.geometry('600x400')
        window.mainloop()

window = tk.Tk()

canvas = tk.Canvas(window, bg='green', height=300, width=500)
image_file = ImageTk.PhotoImage(file='D:/6.jpg')    # 可使用PIL打开jpg、png格式图片
image = canvas.create_image(0,0,anchor='nw',image=image_file)   # 图片锚定点（nw表示图片左上角位置）放在画布（0,0）坐标处
x0, y0, x1, y1 = 300,100,350,150
oval = canvas.create_oval(x0, y0, x1, y1, fill='blue')  # 画圆 用黄色填充
canvas.pack()
Myframe()

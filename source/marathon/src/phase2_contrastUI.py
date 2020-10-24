# GUI：tkinter 使用
# 通过调节滚动条改变标签中字体大小
import tkinter as tk

def resize(ev=None):
    '''改变label字体大小'''
    label.config(font='Helvetica -%d bold' % scale.get())

top = tk.Tk()  # 实例化tkinter对象
top.geometry('250x150')  # 设置窗口大小
top.title('滑动设置')  # 设置窗口标题

# Label控件
label = tk.Label(top, text='对比度增强', font='Helvetica -12 bold')
label.pack(fill=tk.Y, expand=1)

# scale滚动条，数值从10到40，水平滑动，回调resize函数
scale = tk.Scale(top, from_=10, to=40, orient=tk.HORIZONTAL, command=resize)
scale.set(25)  # 设置初始值
scale.pack(fill=tk.X, expand=1)

# Button控件
quit_btn = tk.Button(top, text='QUIT', command=top.quit,
                     activeforeground='white', activebackground='red')
quit_btn.pack()

tk.mainloop()

'''
函数绑定
'''
import tkinter as tk 

root= tk.Tk()

def callback(event):
    print(event.x,event.y)

frame = tk.Frame(root,width=200,height=200)
frame.bind('<Button-1>',callback)
#<Key>  组件获得焦点 <Motion>获取鼠标实时位置
frame.pack()
tk.mainloop()
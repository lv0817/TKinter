import tkinter as tk 
root = tk.Tk()

w = tk.Canvas(root,width=400,height=300)
w.pack()

def paint(event):
    x1,y1 = (event.x-1),(event.y-1)
    x2,y2 = (event.x+1),(event.y+1)
    w.create_oval(x1,y1,x2,y1,fill='blue')

tk.Label(root,text='拖动鼠标进行绘制').pack(side=tk.BOTTOM)


w.bind('<B1-Motion>',paint)#绑定鼠标左键事件


tk.mainloop()
'''
text控件
插入按钮组件，插入图片
'''
import tkinter as tk 
root = tk.Tk()

text = tk.Text(root,width=100,height=10)#宽度和高度
text.pack()

#photo = tk.PhotoImage(file = 'g2.gif')

text.insert(tk.INSERT,'hello world')#往光标的位置插入，初始化的时候在左上角
#除了支持插入文本，还支持，图片按钮等

def show():
    print('you have click here')

b1 = tk.Button(text,text='click here',command=show)#在text中插入这个组件
text.window_create(tk.INSERT,window=b1)#窗口显示内容为b1，插入的位置在光标的位置

#def show_pic():
 #   text.image_create('end',image=photo)

#b2 = tk.Button(text,text='insert a pic',command=show_pic)
#text.window_create('end',window=b2)






tk.mainloop()
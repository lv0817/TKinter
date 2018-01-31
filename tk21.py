'''
菜单栏
级联菜单
弹出菜单
'''
import tkinter as tk 

root = tk.Tk()

menubar = tk.Menu(root)



def callback():
    print('hello')

def callback2():
    print('call back 2')

menubar.add_command(label='hello',command=callback)
menubar.add_command(label='quit',command=root.quit)

#可以留意一下tearoff的实现效果，默认是true
filemenu=tk.Menu(menubar,tearoff=False)#注意，这里不是在root下，是在menubar下
filemenu.add_command(label = 'open',command=callback2)
filemenu.add_command(label ='save',command=callback2)
filemenu.add_separator()
filemenu.add_command(label ='quit',command=callback2)
#在menubar下面创建一个级联菜单
menubar.add_cascade(label ='文件',menu=filemenu)#注意这里的从属关系 


#注意，需要吧我们创建好的菜单和root的菜单关联一下
root.config(menu=menubar)



#右键弹出菜单
frame = tk.Frame(root,width=512,height=512)
frame.pack()

def popup(event):
    menubar.post(event.x_root,event.y_root)

frame.bind('<Button-3>',popup)#和鼠标右键进行绑定




tk.mainloop()
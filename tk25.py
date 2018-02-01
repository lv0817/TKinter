'''message组件'''
import tkinter as tk 

root = tk.Tk()

v1 = tk.Message(root,text='----------',width=100)
v1.pack()

v2 = tk.Message(root,text='中的\n高富帅的那个人哈的说法会i哦这份爱哦',width=100)
v2.pack()

'''spinbox,可以用来选择列表或者选择一系列数字'''
root2 = tk.Tk()
w = tk.Spinbox(root2,values=['a','b','c','d','e'])
w.pack()

'''toplevel组件'''
root3 = tk.Tk()
def create():
    top = tk.Toplevel()
    top.title('hello toplevel')

    msg = tk.Message(top,text='aaaaaaaa')
    msg.pack()

tk.Button(root3,text='创建窗口',command=create).pack()



tk.mainloop()



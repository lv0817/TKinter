'''
撤销操作
分布撤销操作
'''
import tkinter as tk 

root = tk.Tk()

text = tk.Text(root,width=50,height=10,undo=True,autoseparators=False)
#undo为撤销操作  auotoseparators 是自动分割
text.pack()

text.insert('insert','hello world')

def callback(event):
    text.edit_separator()

text.bind('<Key>',callback)#绑定一个按键操作,每当有按键操作的时候就自动插入一个分隔符，
'''
请注意，所有绑定的事件操作都要添加一个event
'''

def show():
    text.edit_undo()#撤销操作

tk.Button(root,text='撤销',command=show).pack()

tk.mainloop()




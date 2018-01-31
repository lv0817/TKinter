'''
撤销操作
'''
import tkinter as tk 

root = tk.Tk()

text = tk.Text(root,width=50,height=10,undo=True)#undo为撤销操作
text.pack()

text.insert('insert','hello world')

def show():
    text.edit_undo()#撤销操作

tk.Button(root,text='撤销',command=show).pack()

tk.mainloop()




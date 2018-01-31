'''
option menu
'''
import tkinter as tk 

root = tk.Tk()

variable =tk.StringVar()
variable.set('one')#对字符串型变量这只一个初始值

w = tk.OptionMenu(root,variable,'one','two','three')
w.pack()
tk.mainloop()
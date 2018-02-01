'''标准对话框'''
'''
import tkinter as tk 
import tkinter.messagebox as tk_m


tk_m.askokcancel('demo','test')

tk.mainloop()
'''
'''要注意这里的导入方式，因为messagebox是属于tkinter下面的一个子模块，所以导入的时候
必须要分开'''

from tkinter import messagebox

print(messagebox.askokcancel('demo','hello'))
#按下确定返回true，按下取消返回flase

mainloop()

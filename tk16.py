'''
事件绑定
'''

import tkinter as tk  
import webbrowser

root=tk.Tk()

text = tk.Text(root,width=30,height=5)
text.pack()

text.insert('insert','你将访问 www.baidu.com')

text.tag_add('link','1.5','end')
text.tag_config('link',foreground='blue',underline=True)

#绑定事件一定要有一个event，否则会报错哦
def show_arrow_cursor(event):
    text.config(cursor='arrow')

def show_xterm_cursor(event):
    text.config(cursor='xterm')

def click(event):
    webbrowser.open('http://www.baidu.com')



text.tag_bind('link','<Enter>',show_arrow_cursor)#代表鼠标进入
text.tag_bind('link','<Leave>',show_xterm_cursor)#代表鼠
#绑定事件没有command
#text.tag_bind('link','<Button-1>',command = click)#代表鼠标进入
text.tag_bind('link','<Button-1>',click)#代表鼠标进入






tk.mainloop()
'''
判断一个文本是否发生变化，并给出相应提示
'''
import tkinter as tk 
import hashlib

root = tk.Tk()

text = tk.Text(root,width=10,height=5)
text.pack()

text.insert('insert','you will visit baidu.com') 
contents = text.get('1.0','end')

def getSig(contents):#就是看签名摘要有没有变化
    m = hashlib.md5(contents.encode())
    return m.digest()

sig = getSig(contents)

def check():
    contents = text.get('1.0','end')#通过判断两次内容是否相同来监测是否发生变化
    if sig!= getSig(contents):
        print('the contens has been changed')
    else:
        print('yes,will be closed')

tk.Button(root,text='check',command=check).pack()

tk.mainloop()




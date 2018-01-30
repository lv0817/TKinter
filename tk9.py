import tkinter as tk 
'''
输入练习
'''
root = tk.Tk()
#两个标签
l1 = tk.Label(root,text='账号：',padx=5,pady=5).grid(row=0,column=0)
l2 = tk.Label(root,text='密码：',padx=5,pady=5).grid(row=1,column=0)
v1 = tk.StringVar()
v2 = tk.StringVar()

#两个输入框
'''e1 = tk.Entry(root).grid(row=0,column=1,padx=10)
并不知道为什么这种方法不对
'''
e1 = tk.Entry(root,textvariable=v1)
e1.grid(row=0,column=1,padx=10)
e2 = tk.Entry(root,textvariable=v2,show='*')#隐藏输入信息
e2.grid(row=1,column=1,padx=15)
#两个按钮
def show():
    print('账号： %s'% e1.get())#打印字符串,e1.get
    print('密码： %s'% e2.get())#打印字符串,e1.get


b1 = tk.Button(root,text='获取信息',width=10,command = show)\
.grid(row=3,column=0,sticky='w',padx=5,pady=10)
b2 = tk.Button(root,text='QUIT',width=10,command = root.quit)\
.grid(row=3,column=1,sticky='E',padx=5,pady=10)#退出直接调用跟窗口的quit方法就行


tk.mainloop()
import tkinter

root = tkinter.Tk()

v = tkinter.IntVar()#表示按钮是否被选中,相当于ture or fulse用01表示

c = tkinter.Checkbutton(root,text='test',variable = v)
c.pack()

l = tkinter.Label(root,textvariable = v)#在标签上显示v的结果
l.pack()
root.mainloop()
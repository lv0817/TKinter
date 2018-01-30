from tkinter import *
'''
以后一定要注意多看官方文档
'''
root = Tk()

v = IntVar()

Radiobutton(root,text='one',variable = v,value=2).pack(anchor='w')
Radiobutton(root,text='two',variable = v,value=2).pack(anchor='w')
Radiobutton(root,text='three',variable = v,value=3).pack(anchor='w')
#三个value的值不同，三个按钮才可以互斥
#当选中一个按钮的时候，会吧这个按钮的值交给v（IntVar）,此时，这个v是所有button都共有的
#然后每个按钮将拿到的v和自己的value一对比，一样，就表示选中，否则，就没有选中
#
l = Label(root,textvariable = v)#在标签上显示v的结果
l.pack()

mainloop()
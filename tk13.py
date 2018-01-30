'''
scale组件，可以限定一个数据的范围
'''
import tkinter as tk 

root = tk.Tk()
s1 = tk.Scale(root,from_=0,to=50,tickinterval=10,resolution=6,length=200)#每5个显示一个刻度,精度为3
'''
注意，pack不能直接跟在Scale穿件后面，不然，就变成了pack传给s1
而我们的目标是创建s1位Scale
并对s1 的属性进行修改
'''
s1.pack(side=tk.RIGHT)#垂直方向

#tk.Scale(root,from_=0,to=200,orient=tk.HORIZONTAL).pack()#水平方向
s2 = tk.Scale(root,from_=0,to=200,resolution=3,orient=tk.HORIZONTAL)
s2.pack(side=tk.BOTTOM)#水平方向

#利用get方法获取滑块当前位置
def show():
    print(s1.get(),s2.get())

tk.Button(root,text='get the position',command=show).pack()



tk.mainloop()

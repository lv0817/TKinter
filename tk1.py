import tkinter as tk 

#实例化一个TK，用来容纳整个程序
app =tk.Tk() #顶层窗口 root窗口
app.title('test demo')

#label是一个组件，组件实例化之后赋值给一个对象
theLabel = tk.Label(app,text='my second windows program')#app代表这个组件放到根窗口下面
theLabel.pack()#可以理解为自动调节组件的尺寸

app.mainloop()#窗口的主事件循环，从这一步开始，有tk接管程序
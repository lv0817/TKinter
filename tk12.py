'''
滚动条
'''
import tkinter as tk  

root = tk.Tk()

sb = tk.Scrollbar(root)
sb.pack(side = 'right',fill=tk.Y)

lb = tk.Listbox(root,yscrollcommand=sb.set)
for i in range(100):
    lb.insert(tk.END,i)

lb.pack(side='left',fill=tk.BOTH)
sb.config(command=lb.yview)
#yview是内部设置y方向如何显示，不用我们关心他是如何实现的 
#注意要在其他lb创建好再去配置某个选项，不然lb还没有产生就去设置回出错
'''
修改一个属性，可以使用.config实现
'''


tk.mainloop()
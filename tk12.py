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
sb.config(command=lb.yview)#注意要在其他创建好再去配置某个选项，不然容易出错


tk.mainloop()
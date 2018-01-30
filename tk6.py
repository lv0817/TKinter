import tkinter as tk 

root = tk.Tk()

LANGES = [
('python',1),
('java',2),
('ruby',3),
('c++',4)]

v = tk.IntVar()
v.set(1)

for lang,num in LANGES :
    b=tk.Radiobutton(root,text=lang,variable=v,value=num,indicatoron=False)#最后这个参数代表不使用小圆点形式
    b.pack(anchor='w',fill='x')#表示横向填充

l = tk.Label(root,textvariable = v)#在标签上显示v的结果
l.pack()

tk.mainloop()

import tkinter as tk 
'''
label 框架
'''
root = tk.Tk()

group = tk.LabelFrame(root,text='最好的脚本语言是',padx=5,pady=5)
group.pack(padx=5,pady=5)

LANGES = [
('python',1),
('java',2),
('ruby',3),
('c++',4)]

v = tk.IntVar()
v.set(3)#用set来指定一个初值，当进入for以后便会重建关系，根据用户选择修改

for lang,num in LANGES :
    b=tk.Radiobutton(group,text=lang,variable=v,value=num,indicatoron=False)#最后这个参数代表不使用小圆点形式
    b.pack(anchor='w',fill='x')#表示横向填充

l = tk.Label(root,textvariable = v)#在标签上显示v的结果
l.pack()

tk.mainloop()

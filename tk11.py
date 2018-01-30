import tkinter as tk 
'''
listbox
'''
master = tk.Tk()

theLB = tk.Listbox(master,selectmode=tk.SINGLE)
theLB.pack()

theLB2 = tk.Listbox(master,selectmode='browse')
theLB2.pack()

'''
theLB.insert(0,'hello')
theLB.insert(1,'hello')
theLB.insert('end','aaaa')
'''
'''
别的写法都不行，不知道为什么
'''
for item in ['aaa','bbb','ccc','ddd','eee']:
    theLB.insert('end',item)

for item in ['aaa','bbb','ccc','ddd','eee']:
    theLB2.insert(tk.END,item)

'''
大写找不到是因为没有用tk.啊
'''

'''
theLB.delete(1,'end')#起始位置到阶数位置
'''
#active表示当前选中的值
#lambda ,冒号前面是参数，冒号后面是内容
theButton = tk.Button(master,text='删除指定内容',\
command=lambda x=theLB : x.delete('active'))#x是什么？是那个listboxa

def del_str():
    theLB.delete('active')

theButton2 = tk.Button(master,text='删除指定内容2',\
command=del_str)#x是什么？是那个listboxa
#这里注意，函数后面不可以加括号，不然会有不明不白的错误

theButton.pack()
theButton2.pack()



tk.mainloop()

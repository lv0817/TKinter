'''
menubar中的radiobutton和checkbutton
'''
import tkinter as tk 
root = tk.Tk()

def callback():
    print('callback  1')

menubar = tk.Menu(root)

'''tkinter中的用来存放变量的整形'''
openVar=tk.IntVar()
saveVar = tk.IntVar()
quitVar = tk.IntVar()

filemenu = tk.Menu(menubar,tearoff=False)
file_quit = tk.Menu(filemenu,tearoff=False)

filemenu.add_checkbutton(label='打开',command = callback,variable = openVar)
filemenu.add_checkbutton(label='保存',command=callback,variable=saveVar)
filemenu.add_separator()
filemenu.add_checkbutton(label='退出',command=root.quit,variable=quitVar)
filemenu.add_cascade(label='立即退出',menu=file_quit)
#组织到file下面
file_quit.add_checkbutton(label='打开',command = callback,variable = openVar)
file_quit.add_checkbutton(label='保存',command=callback,variable=saveVar)

menubar.add_cascade(label='文件',menu=filemenu)
#将filemenu中所有的选项组织到 文件 选项卡下面

editVar = tk.IntVar()

editmenu = tk.Menu(menubar,tearoff=False)
editmenu.add_radiobutton(label='剪切',command=callback,variable=editVar,value=1)
editmenu.add_radiobutton(label='拷贝',command=callback,variable=editVar,value=2)
editmenu.add_radiobutton(label='粘贴',command=callback,variable=editVar,value=3)
menubar.add_cascade(label='编辑',menu=editmenu)





#注意，需要吧我们创建好的菜单和root的菜单关联一下
root.config(menu=menubar)




tk.mainloop()
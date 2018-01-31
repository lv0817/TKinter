'''
tags标签
'''
import tkinter as tk 

root = tk.Tk()

text = tk.Text(root,width=30,height=5)
text.pack()

text.insert(tk.INSERT,'abcdefg higklmn')

text.tag_add('tag1','1.1','1.4','1.9')#代表tag1位1.1到1.4和1.9两个位置
text.tag_config('tag1',background='yellow',foreground='red')

#新标签的创建会覆盖掉久标签的内容
text.tag_add('tag2','1.8','1.10')#代表tag1位1.1到1.4和1.9两个位置
text.tag_config('tag2',background='gray',foreground='blue')

tk.mainloop()





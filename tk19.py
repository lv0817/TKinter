'''
canvas组件
'''
import tkinter as tk 
root = tk.Tk()

w=tk.Canvas(root,width=300,height=200,background='white')
w.pack()

line1 = w.create_line(0,0,300,200,fill='yellow',width=5)
line2 = w.create_line(100,0,100,100,fill='red',dash=(4,4))#dash用来设置线型
rect1 = w.create_rectangle(50,25,150,75,fill='blue')
#这三个对象，不出意外的话就会一直保留下去，除非你对他们做出了修改
rect2 = w.create_rectangle(60,35,140,65,fill='white')

oval1 = w.create_oval(60,35,140,65,fill='pink')#椭圆 

w.create_text(100,50,text='hello world')#默认是中间，可以设置东西南北
w.coords(line1,0,30,300,60)
w.itemconfig(rect1,fill='red')
w.delete(line2)

tk.Button(root,text = 'delete all',command = (lambda x=tk.ALL : w.delete(x))).pack()


tk.mainloop()




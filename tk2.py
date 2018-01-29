import tkinter as tk

class APP:
    #通过构造函数设置参数
    def __init__(self,master):#传进来master，这里就是顶层的root
        frame = tk.Frame(master)#框架用于在一个复杂的环境中将组件分组
        frame.pack(side=tk.LEFT,padx=10,pady=15)
        #创建一个按钮组件
        #self.hi_there = tk.Button(self,master=None) #不是放在根，是放在frame
        self.hi_there = tk.Button(frame,text='hello',\
        bg='black',fg='white',command = self.say_hi)
        self.hi_there.pack()

    def say_hi (self):
        print('hello world')

root = tk.Tk()
app=APP(root)

root.mainloop()


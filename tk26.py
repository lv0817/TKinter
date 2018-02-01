import tkinter as tk 


root = tk.Tk()

photo = tk.PhotoImage(file='4.gif')

tk.Label(root,image=photo).grid(row=0,column=2,rowspan=2)#跨行列操作


tk.Label(root,text='user').grid(row=0,column=0,sticky='e')
tk.Label(root,text='paseword').grid(row=1,column=0,sticky='w')

tk.Entry(root).grid(row=0,column=1)
tk.Entry(root).grid(row=1,column=1)

'''跨行列显示'''


tk.mainloop()
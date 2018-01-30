import tkinter as tk 
master = tk.Tk()

def test():
    if e1.get() in (1,2):
        print('yes')
        return True
    else:
        print('no')
        e1.delete(0,-1)
        return False    

v = tk.StringVar()

e1 = tk.Entry(master,textvariable=v,validate='focusout',validatecommand=test)#失去焦点是执行test函数
e2 = tk.Entry(master)

e1.pack(padx=10,pady=10)
e2.pack(padx=10,pady=10)

tk.mainloop()
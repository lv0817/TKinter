import tkinter as tk 

root=tk.Tk()

GIRLS = ['1 lady','2 lady','3 lady','4 lady']

v = []

for girl in GIRLS :
    v.append(tk.IntVar())
    b = tk.Checkbutton(root,text=girl,variable =v[-1])
    b.pack(anchor = 'w' )
    print(v)

tk.mainloop()
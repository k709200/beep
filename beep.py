from tkinter import *
import winsound
root = Tk()
root.title('beep')

def _ps():
    print(ent_hz.get())
    root.title('beeping...')
    winsound.Beep(int(ent_hz.get()), int(ent_t.get())*1000)
    root.title('beep')




lab_hz = Label(root, text='Frequency(Hz):')
lab_hz.pack(side=LEFT)

iv = IntVar()
iv.set(1000)
ent_hz = Entry(root, width=8, textvariable=iv)
ent_hz.textvariable = '1555'
ent_hz.pack(side=LEFT)

lab_n = Label(root, padx=2)
lab_n.pack(side=LEFT)

lab_t = Label(root, text='Time(s):')
lab_t.pack(side=LEFT)

iv = IntVar()
iv.set(1)
ent_t = Entry(root, width=4, textvariable=iv)
ent_t.pack(side=LEFT)

lab_n = Label(root,padx=2)
lab_n.pack(side=LEFT)

btm_p = Button(root, text='Play', width=8, command=_ps)
btm_p.pack(side=RIGHT)

mainloop()

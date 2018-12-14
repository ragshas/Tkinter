from tkinter import *

window=Tk()

def kg_to_others():
    gm = float(e1_value.get())*1000
    pnd = float(e1_value.get())*2.20462
    ounc = float(e1_value.get())*35.274
    t1_gm.insert(END,gm)
    t1_pnd.insert(END, pnd)
    t1_oun.insert(END,ounc)

b1=Button(window, text="Convert", command=kg_to_others)
b1.grid(row=0,column=3)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=2)

label = Label(window, text = "Kg")
label.grid(row=0,column=1)


t1_gm=Text(window, height=1, width=20)
t1_gm.grid(row=1,column=1)

t1_pnd = Text(window, height=1, width=20)
t1_pnd.grid(row=1,column=2)

t1_oun = Text(window, height=1, width=20)
t1_oun.grid(row=1, column=3)



window.mainloop()

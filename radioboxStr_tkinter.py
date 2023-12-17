from tkinter import*
form = Tk()
form.geometry("700x500")
v = StringVar()
v.set(1)
rdm = Radiobutton(form , text = "male",value ="male",variable =v)
rdm.pack()
drf = Radiobutton(form ,text = "female",value ="female",variable =v)
drf.pack()
def f ():
    print(v.get())
Button(form ,text ="OK",command = f).pack()

form.mainloop()

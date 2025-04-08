from tkinter import*
window=Tk()
window.geometry("500x500")
def top():
    tp=Toplevel()
    tp.geometry("100x100")
    l=Label(text="hello")
    l.pack()
    tp.mainloop()
b=Button(text="click me" , command=top)
b.pack()
window.mainloop()
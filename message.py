from tkinter import*
from tkinter import messagebox
window=Tk()
window.geometry("500x500")
def msg():
    messagebox.showinfo("are you sure you want to leave")
   
btn=Button(text="click me",command=msg)
btn.pack()

def mag():
    messagebox.showwarning("dont you want to save your work")
btn1=Button(text="click it",command=mag)
btn1.pack()

def meg():
    messagebox.askquestion("how are you?")
btn2=Button(text="click here",command=meg)
btn2.pack()
window.mainloop()

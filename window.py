from tkinter import*
window=Tk()
window.geometry("500x500")
window.title("library")
l1=Label(text="enter name" ,fg="white" ,bg="black")
l1.place(x=50 ,y=50)
l2=Label(text="enter email" ,fg="white" ,bg="black")
l2.place(x=50 ,y=80)
e1=Entry()
e1.place(x=120 ,y=50)
e2=Entry()
e2.place(x=120 ,y=80)






window.mainloop()
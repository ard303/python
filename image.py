from tkinter import*
from PIL import Image,ImageTk
window=Tk()
window.geometry("1000x1000")
img=Image.open("car.png")
imge=ImageTk.PhotoImage(img)
lb1=Label(image=imge)
lb1.pack()
window.mainloop()
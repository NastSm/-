from tkinter import *

def name():
    p = str(entry.get())
    res = "Привет {}".format(p)  
    label.configure(text=res)  

root=Tk()
root.title('Приложение')
root.geometry('500x300')

entry=Entry(root, width=40,  bg='light gray', fg='black', font='consolas')
entry.place(x=50, y= 30)

button_1 = Button(root, text='Введи имя', width=40, height=2, bg='cyan', command =name)
button_1.place(x=100, y= 55)

label = Label(root, width=30, bg='gray', fg='cyan', font='consolas')
label.place(x=120, y= 190)

root.mainloop()

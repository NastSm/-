from tkinter import *
from random import *
root=Tk()

canvas=Canvas(root, width=500, height=700, bg='white')
canvas.pack()

def figura():
    canvas.delete("all")
    q = choice(['blue', 'green', 'yellow', 'red', 'pink', 'grey'])
    z = randint(1,3)
    x = randint(0, 500)
    y = randint(0, 700)
    x1 = randint(0, 500)
    y1 = randint(0, 700)
    x2 = randint(0, 500)
    y2 = randint(0, 700)
    if z == 1:
        kvadrat = canvas.create_rectangle(x, y, x1, y1, fill=q)
    elif z == 2:
        oval = canvas.create_oval(x, y, x1, y1, fill=q)
    elif z == 3:
        treugolnik = canvas.create_polygon(x, y, x1, y1, x2, y2, fill= q)
        
button = Button ( text='сменить фигуру', command=figura )
button.pack()
root.mainloop()



from tkinter import *

from tkinter import messagebox

top = Tk()

dim = 1500
minSize = 4

def drawGasket(x, y, dim, collerR, collerB, collerY):
    if dim <= minSize:
#        stroke = collerR, collerB, collerY
        print(int('5', 16), int('6', 16), int('7', 16))
        print(hex(5), hex(6), hex(7))
        points = [x+dim/2, y, x, dim+y, dim+x, dim+y]
        poly = C.create_polygon(points, outline='#fff', fill='#ccc', width=0)
    else:
        newDim = dim / 2
        drawGasket(x + dim/4, y, newDim, collerR, collerB + newDim, collerY + newDim/100)
        drawGasket(x, y + newDim, newDim, collerR + newDim/100, collerB, collerY + newDim)
        drawGasket(x + newDim, y + newDim, newDim, collerR + newDim, collerB + newDim/100, collerY)


def draw():
    drawGasket(0, 0, dim, 20, 20, 20)


C = Canvas(top, bg ="#aaaaaa", height = dim, width = dim)

draw()

C.pack()
top.mainloop()



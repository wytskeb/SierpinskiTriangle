

from tkinter import *

from tkinter import messagebox

top = Tk()

dim = 400
minSize = 4

def drawGasket(x, y, dim, collerR, collerG, collerB):
    if dim <= minSize:
#       stroke = collerR, collerB, collerY
        fillcolor = '#' + str(hex(int(collerR/28)))[2:3] + str(hex(int(collerG/28)))[2:3] + str(hex(int(collerB/28)))[2:3]
        print(fillcolor)
        points = [x+dim/2, y, x, dim+y, dim+x, dim+y]
        poly = C.create_polygon(points, outline=fillcolor, fill=fillcolor, width=0)
    else:
        newDim = dim / 2
        drawGasket(x + dim/4, y, newDim, collerR, collerG + newDim, collerB + newDim/100)
        drawGasket(x, y + newDim, newDim, collerR + newDim/100, collerG, collerB + newDim)
        drawGasket(x + newDim, y + newDim, newDim, collerR + newDim, collerG + newDim/100, collerB)


def draw():
    drawGasket(0, 0, dim, 20, 20, 20)


C = Canvas(top, bg ="#aaaaaa", height = dim, width = dim)

draw()

C.pack()
top.mainloop()



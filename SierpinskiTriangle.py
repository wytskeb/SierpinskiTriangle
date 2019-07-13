

from tkinter import *

from tkinter import messagebox

top = Tk()

dim = 1500
minSize = 4

def drawGasket(x, y, dim, collerR, collerB, collerY):
    if dim <= minSize:
#        stroke = collerR, collerB, collerY
        points = [x+dim/2, y, x, dim+y, dim+x, dim+y]
        poly = C.create_polygon(points, outline='#ff1', fill='#fff', width=5)
    else:
        newDim = dim / 2
        drawGasket(x + dim/4, y, newDim, collerR, collerB + newDim, collerY + newDim/100)
        drawGasket(x, y + newDim, newDim, collerR + newDim/100, collerB, collerY + newDim)
        drawGasket(x + newDim, y + newDim, newDim, collerR + newDim, collerB + newDim/100, collerY)


C = Canvas(top, bg ="#aaaaaa", height = dim, width = dim)

def draw():
        drawGasket(0, 0, dim, 20, 20, 20)


#points = [0, 0, 200, 0, 100, 100]
#poly =C.create_polygon(points, outline='#ff1',
#    fill='#131', width=5)


draw()

C.pack()
top.mainloop()



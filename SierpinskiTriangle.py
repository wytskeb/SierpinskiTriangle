

from tkinter import *

from tkinter import messagebox

top = Tk()

dim = 400
minSize = 4
factor = dim*0.07
def drawGasket(x, y, dim, collerR, collerG, collerB):
    if dim <= minSize:
# Het "ei" wordt gelegd met als resultaat het"Sierpinski driehoek"

        fillcolor = '#' + str(hex(int(collerR/factor)))[2:3] + str(hex(int(collerG/factor)))[2:3] + str(hex(int(collerB/factor)))[2:3]
        print(dim, factor)
        points = [x+dim/2, y, x, dim+y, dim+x, dim+y]
        poly = C.create_polygon(points, outline=fillcolor, fill=fillcolor, width=0)

    else:

# het getal dim wordt door twee gedeeld voor een order kleinere driehoeken en als middel om tekontroleren wanneer het programma moet eindigen
        newDim = dim / 2
# functie roept zichzelf aan
        drawGasket(x + dim/4, y, newDim, collerR, collerG + newDim, collerB + newDim/100)
        drawGasket(x, y + newDim, newDim, collerR + newDim/100, collerG, collerB + newDim)
        drawGasket(x + newDim, y + newDim, newDim, collerR + newDim, collerG + newDim/100, collerB)


def draw():
# Roept de recursieve functie voor het eerst aan en is daarmee de start van de rekursie
    drawGasket(0, 0, dim, 20, 20, 20)

# produceert het scherm waarop het resutaat getoond word
C = Canvas(top, bg ="#aaaaaa", height = dim, width = dim)

# start
draw()

C.pack()
top.mainloop()



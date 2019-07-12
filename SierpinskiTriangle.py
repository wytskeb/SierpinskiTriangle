# from numpy import *
import numpy as np
# from pylab import *
import pylab as py

py.figure()

pi = np.pi

a = np.array([0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4, pi])
b = np.array([1, 3, 3, 5])

py.figure()
py.plot(np.sin(a), 'r-^',
        np.sin(2*a), "b-o", label = 'BOE')
py.legend()


py.show()
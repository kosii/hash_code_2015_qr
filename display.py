import numpy
import pylab

def display(R, S, coords):
    mtx = numpy.zeros((R, S))
    for t in coords:
        x = t[0]
        y = t[1]
        mtx[x][y] = 1
    #pylab.imshow(mtx, interpolation='None')
    #pylab.show()
    return mtx
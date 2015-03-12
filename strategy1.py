import parser
import display
import numpy
import pylab
import random

def findPlace(row, place):
    for idx, p in enumerate(row): 
        if (row[idx : idx + place].tolist() == [0] * place):
            return idx
    return -1

def strategy1(machines, datacenter):
    cap_final = cap = [0] * 16
    counter = 0
    group = 0

    for machine in machines:
        min_idx = cap.index(min(cap))
        column = findPlace(datacenter[min_idx], machine[0])
        if column != -1:
            counter += 1

            datacenter[min_idx][column : column + machine[0]] = 0.5

            cap[min_idx] += machine[1]
            cap_final[min_idx] = cap[min_idx]
            #print min_idx, column, group % 45
            group += 1
        else:
            #print 'x'
            cap[min_idx] = 10000000

    print cap_final
    print sum(cap_final)
            

    pylab.imshow(datacenter, interpolation='None')
    pylab.show()


R, S, U, P, M, unavailable, machines = parser.parser('dc.in')
datacenter = display.display(R, S, unavailable)
strategy1(machines, datacenter)
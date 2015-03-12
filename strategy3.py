import numpy
import pylab
import random
import strategy2
import parser
import itertools
from operator import itemgetter

def strategy3(R, S, U, P, M, unavailable, machines):
	machines = strategy2.optimal_server_placements(R, S, U, P, M, unavailable, machines)
	cap = [0] * P
	machines2 = []

	pool_id = 0
	for machine in sorted(machines, key=itemgetter(5, 1)):
		(i, row, s, z, c, col_id) = machine
		if (row != None):
			min_idx = cap.index(min(cap))
			cap[min_idx] += c
			machines2.append((i, row, s, z, c, col_id,min_idx))
			pool_id += 1
			# printMatrix(machines2)
			# if pool_id > 10:
			# 	break
		else:
			machines2.append((i, row, s, z, c, col_id, None))
	fromMachinesTofile(machines2)
	import evaluate
	print evaluate.evaluate(printMatrix(machines2))

def fromMachinesTofile(machines):
	machines = sorted(machines)
	# for machine in machines:
		#print machine
		# if (machine[1] != None):
			# print machine[1], machine[2], machine[6]
		# else:
			# print 'x'

def printMatrix(machines):
	mtx = numpy.zeros((45, 16))
	servers = numpy.zeros((45, 16))
	for machine in machines:
		if (machine[1] != None):
			mtx[machine[6], machine[1]] += machine[4]
			servers[machine[6], machine[1]] += 1


	# for ((row, pool), grouped) in itertools.groupby(sorted(machines, key=itemgetter(1, 5)), itemgetter(1, 5)):
	# 	grouped = list(grouped)
	# 	mtx[row, pool] = sum(map(itemgetter(4), grouped))
	# pylab.gray()
	# pylab.imshow(mtx, interpolation='None')
	# pylab.show()
	print mtx
	print servers
	return mtx
	

if __name__ == '__main__':
	R, S, U, P, M, unavailable, machines = parser.parser('dc.in')
	strategy3(R, S, U, P, M, unavailable, machines)
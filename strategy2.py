import parser
import display
import pylab
import itertools
import operator
import random
from operator import itemgetter
# R, S, U, P, M, unavailable, machines = parser.parser('dc.in')


# mtx = display.display(R, S, unavailable)

# pylab.imshow(mtx, interpolation='None')
# pylab.show()
# return mtx

# def accumulate(iterable, func=operator.add):
#     'Return running totals'
#     # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
#     # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
#     it = iter(iterable)
#     total = next(it)
#     yield total
#     for element in it:
#         total = func(total, element)
#         yield total


# source: http://rosettacode.org/wiki/Knapsack_problem/0-1#Python
try:
    xrange
except:
    xrange = range
 
def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt  += wt
        totval += val
    return (totval, -totwt) if totwt <= 400 else (0, 0)
 
items = (
    ("map", 9, 150), ("compass", 13, 35), ("water", 153, 200), ("sandwich", 50, 160),
    ("glucose", 15, 60), ("tin", 68, 45), ("banana", 27, 60), ("apple", 39, 40),
    ("cheese", 23, 30), ("beer", 52, 10), ("suntan cream", 11, 70), ("camera", 32, 30),
    ("t-shirt", 24, 15), ("trousers", 48, 10), ("umbrella", 73, 40),
    ("waterproof trousers", 42, 70), ("waterproof overclothes", 43, 75),
    ("note-case", 22, 80), ("sunglasses", 7, 20), ("towel", 18, 12),
    ("socks", 4, 50), ("book", 30, 10),
    )
 
def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]
 
    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)
 
    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]
 
        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt
 
    return result
 
 
# bagged = knapsack01_dp(items, 400)
# print("Bagged the following items\n  " +
#       '\n  '.join(sorted(item for item,_,_ in bagged)))
# val, wt = totalvalue(bagged)
# print("for a total value of %i and a total weight of %i" % (val, -wt))

def get_segments(R, S, unavailable):
    segments = []
    for r in xrange(R):
        startS = 0
        for s in xrange(S):
            if (r, s) in unavailable:
                length = s - startS
                if length > 0:
                    segments.append((r, startS, length))
                startS = s + 1
        length = s - startS
        if length > 0:
            segments.append((r, startS, length))
    return segments

# segments = segment(R, S, unavailable)

# print sum(map(lambda s: s[2], segments))
# print sum(map(lambda s: s[0], servers))

# def fill((r, s, l), servers):
#     print list(itertools.takewhile(lambda (z, c): z < l, accumulate(servers, lambda (a,b),(c, d): (a+c, b+d))))
#     return servers
def optimal_server_placements(R, S, U, P, M, unavailable, machines):
    server_placements = []
    segments = get_segments(R, S, unavailable)
    servers = map(lambda (i, (z, c)): (i, z, c), enumerate(machines))
    for (r, s, l) in sorted(segments, key=lambda (r, s, l): l):
        bagged = knapsack01_dp(servers, l)
        offset = 0
        for (i, z, c) in bagged:
            server_placements.append((i, r, s + offset, z, c))
            offset += z
        units_length = sum(map(itemgetter(1), bagged))
        capacities = sum(map(itemgetter(2), bagged))
        # print "hole of length {l} filled with servers of {u} unit of capacity {capacities}".format(l=l, u=units_length, capacities=capacities)
        # capacity_placed += capacities

        # print bagged
        servers = [server for server in servers if server not in bagged]
        # print len(servers)
        # list(fill(segment, servers))
        # break 
    #print len(server_placements)
    #print len(servers)
    all_server = server_placements + map(lambda (i, z, c): (i, None, None, z, c), servers)
    assert len(all_server) == M

    # machines by row
    return list(
        itertools.chain(
            *[[machine + (i, ) for (i, machine) in enumerate(sorted(row_machines, key=itemgetter(2)))] for (row, row_machines) in itertools.groupby(sorted(all_server, key=itemgetter(1)), key=itemgetter(1))]
        )
    )
    return all_server

    return sorted(all_server, key=itemgetter(1))
#R, S, U, P, M, unavailable, machines = parser.parser('dc.in')

#optimal_server_placements(R, S, U, P, M, unavailable, machines)
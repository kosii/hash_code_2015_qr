import display
import parser
import strategy3

R, S, U, P, M, unavailable, machines = parser.parser('dc.in')

#datacenter = display.display(R, S, unavailable)

#print machines
strategy3.strategy3(R, S, U, P, M, unavailable, machines)
#print sorted(machines, key=lambda (a, b): float(b)/a)
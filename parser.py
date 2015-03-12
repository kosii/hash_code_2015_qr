

def parser(input_file_name):
    with open(input_file_name) as input:
        R, S, U, P, M = map(int, input.readline().split())
        unavailable_slots = []
        for i in xrange(U):
            r, s = map(int, input.readline().split())
            unavailable_slots.append((r, s))
        # print unavailable_slots
        servers = []
        for i in xrange(M):
            z, c = map(int, input.readline().split())
            servers.append((z, c))
        return R, S, U, P, M, unavailable_slots, servers
    # for i in xrange()

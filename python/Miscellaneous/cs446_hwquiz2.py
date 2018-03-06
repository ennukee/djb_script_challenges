def solve(paths, lamb):
    incoming = {}
    outgoing = {}
    for k,v in paths:
        if v in incoming.keys():
            incoming[v].append(k)
        else: incoming[v] = [k]

        if k in outgoing.keys():
            outgoing[k].append(v)
        else: outgoing[k] = [v]

    cur_set = [0.25, 0.25, 0.25, 0.25]
    step_n = 0
    while True:
        step_n += 1
        print('Step {}: {}'.format(step_n, cur_set))
        last_set = []
        for i in range(4):
            s = 0
            if incoming.get(i, None):
                for o in incoming[i]:
                    s += cur_set[o] / len(outgoing[o])
            to_app = lamb/4 + (1-lamb) * s
            to_app = int(to_app * 1000) / 1000
            last_set.append(to_app)
        if last_set == cur_set:
            cur_set = last_set
            break
        else:
            cur_set = last_set
    print('Step {}: {}'.format(step_n + 1, cur_set))
    return cur_set

def main():
    graph_1 = [(0,1),(1,2),(2,3)]
    graph_2 = [(0,1),(0,2),(1,3),(2,3)]
    graph_3 = [(0,1),(1,2),(2,3),(3,0)]

    print(solve(graph_1, 0.15))
    print(solve(graph_2, 0.15))
    print(solve(graph_3, 0.15))

if __name__ == '__main__':
    main()

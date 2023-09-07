import itertools
l = [x for x in input()]
k = lambda x: x[0]
q = itertools.groupby(l, k)

for s, t in q:
    #print(f"{s}:{len(list(t))}")
    print(f"({len(list(t))}, {s})", end=" ")


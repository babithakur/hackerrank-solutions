from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))
pr = list(product(A,B))

for i in range(len(pr)):
    print(pr[i], end=" ")

import numpy
n = int(input())
a = []
for i in range(n):
    a.append(list(map(float, input().split())))
print(numpy.linalg.det(a))

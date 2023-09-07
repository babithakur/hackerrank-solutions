import numpy
n, m = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

arr = numpy.array(a)
s = numpy.sum(arr, axis=0)
print(numpy.prod(s))

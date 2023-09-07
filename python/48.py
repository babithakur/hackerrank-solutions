import numpy
rc = list(map(int, input().split()))
a = []
for i in range(rc[0]):
    a.append(list(map(int, input().split())))

arr = numpy.array(a)
mn = numpy.min(arr, axis=1)
print(numpy.max(mn))

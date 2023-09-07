import numpy
t = list(map(int, input().split()))
a = []
for i in range(t[0]):
    a.append(list(map(int, input().split())))
arr = numpy.array(a)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr, axis=None),11))

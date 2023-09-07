import numpy
rc = list(map(int, input().split()))
arr = []
for i in range(rc[0]):
    arr.append(list(map(int, input().split())))

#arr = numpy.array(list(map(int, input().split())))
np_array = numpy.array(arr)
print(numpy.transpose(np_array))
print(np_array.flatten())

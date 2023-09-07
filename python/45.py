import numpy
numpy.set_printoptions(legacy='1.13')
rc = list(map(int, input().split()))
print(numpy.eye(rc[0],rc[1],k=0))

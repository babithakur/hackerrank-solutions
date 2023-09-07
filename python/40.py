import numpy
numpy.set_printoptions(legacy='1.13')
inp = numpy.array(list(map(float, input().split())))
print(numpy.floor(inp))
print(numpy.ceil(inp))
print(numpy.rint(inp))

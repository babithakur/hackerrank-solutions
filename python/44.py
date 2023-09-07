import numpy
t = list(map(int, input().split()))
x, y = [], []
for i in range(t[0]):
    x.append(list(map(int, input().split())))
for i in range(t[0]):
    y.append(list(map(int, input().split())))
a = numpy.array(x)
b = numpy.array(y)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

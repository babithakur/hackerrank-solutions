import numpy
n = list(map(int, input().split()))
N = []
P = []
for i in range(n[0]):
    N.append(list(map(int, input().split())))

for i in range(n[1]):
    P.append(list(map(int, input().split())))

x = numpy.array(N)
y = numpy.array(P)
z = numpy.concatenate((N, P))
print(z)





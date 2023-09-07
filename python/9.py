num = 17
x = oct(17)
y = hex(17)
z = bin(17)
#print(x[2:])
#print(y[2:])
#print(z[2:])

for i in range(1, num+1):
    x = oct(i)
    y = hex(i)
    z = bin(i)
    print(f"{i}\t{x[2:]}\t{(y[2:].upper())}\t{z[2:]}\n")


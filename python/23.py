x = int(input())
y = int(input())
z = int(input())
n = int(input())
combos = [[a, b, c] for a in [x, y, z] for b in [x, y, z] for c in [x, y, z]]
print(combos)

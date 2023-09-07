from itertools import combinations
inp = list(input().split())
a = []
for i in range(int(inp[1])):
    a.append((list(combinations(sorted(inp[0]), i+1))))

for i in range(len(a)):
    for j in range(len(a[i])):
        print("".join(a[i][j]))
#print(a)
#print(len(a))

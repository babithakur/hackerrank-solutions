from itertools import permutations

inp = list(map(str, input().split()))
out = list(permutations(inp[0], int(inp[1])))
result = []
for i in out:
    result.append(f"{''.join(i)}")

result.sort()
for i in range(0, len(result)):
    print(result[i])

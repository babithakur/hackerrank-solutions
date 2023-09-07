a = list(set(map(int, input().split())))
n = int(input())
result = True
for i in range(n):
    b = list(set(map(int, input().split())))
    for j in range(len(b)):
        if b[j] not in a:
            result = False
print(result)

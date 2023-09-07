elm = int(input())
s = set(map(int, input().split()))
n = int(input())
for i in range(n):
    op = list(input().split())
    if "pop" in op:
        s.pop()
    elif "discard" or "remove" in op:
        s.discard(int(op[1]))
    #elif "remove" in op:
        #s.remove(int(op[1]))

print(sum(s))


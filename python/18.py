from collections import deque
num = int(input())
d = deque()

for i in range(num):
    op = input().split()
    if "append" in op:
        d.append(op[1])
    elif "appendleft" in op:
        d.appendleft(op[1])
    elif "pop" in op:
        d.pop()
    elif "popleft" in op:
        d.popleft()

for i in range(len(d)):
    print(d[i], end=" ")
    
    

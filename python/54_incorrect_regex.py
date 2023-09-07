import re
T = int(input())
r = []
for i in range(T):
    r.append(input())
for i in range(T):
    try:
        re.compile(r[i])
        print(True)
    except:
        print(False)

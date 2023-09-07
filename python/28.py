inp = list(input().split())
op = input()
p = eval(op.replace('x', inp[0]))
#print(p)
if p == int(inp[1]):
    print(True)
else:
    print(False)
#print(op.replace('x', inp[0]))


from itertools import combinations_with_replacement

inp = list(input().split())
sorted_inp = ''.join(sorted(inp[0]))
l = list(combinations_with_replacement(sorted_inp, int(inp[1])))

for i in range(len(l)):
    print(''.join(l[i]))

#print(list(combinations_with_replacement('HACK', 2)))
#print(' '.join(sorted('HACK')))

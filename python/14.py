n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

l1 = list(s1.difference(s2))
l2 = list(s2.difference(s1))
l3 = l1 + l2
l3.sort()
for i in range(0, len(l3)):
    print(f"{l3[i]}")



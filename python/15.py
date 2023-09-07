#n1 = int(input())
#s1 = set(map(int, input().split()))

a = int(input())
for i in range(0, a):
    n1 = int(input())
    s1 = set(map(int, input().split()))
    n2 = int(input())
    s2 = set(map(int, input().split()))
    print(s1.issubset(s2))

    

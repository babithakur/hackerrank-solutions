a = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))

total = s1.union(s2)

print(len(total))



    

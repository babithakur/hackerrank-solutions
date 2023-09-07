a = int(input())
eng = set(input().split())
b = int(input())
french = set(input().split())

total = eng.symmetric_difference(french)

print(len(total))

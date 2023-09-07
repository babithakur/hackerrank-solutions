a = int(input())
eng = set(input().split())
b = int(input())
french = set(input().split())

eng_only = eng.difference(french)

print(len(eng_only))

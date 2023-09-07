s = '''HackerRank.com presents "Pythonist 2".'''
a = []
for char in s:
    a.append(char)
for i in range(0, len(a)-1):
    if a[i].islower():
        a[i] = a[i].upper()
    elif a[i].isupper():
        a[i] = a[i].lower()

final = ''.join(a)        
print(final)

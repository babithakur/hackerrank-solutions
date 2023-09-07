n = int(input())
words = list(input().split())
vowels = ["a", "e", "i", "o", "u"]
score = 0
count = 0
for i in range(n):
    for j in range(len(words[i])):
        if words[i][j] in vowels:
            count += 1
    if count%2 == 0:
        score += 2
    else:
        score += 1


print(score)

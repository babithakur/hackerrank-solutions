from collections import Counter
n = int(input("No of shoes: "))
sizes = list(input("Sizes: ").split())
customers = int(input("No of customers: "))
av = Counter(sizes).keys()
'''add = 0
for i in range(customers):
    zibrish = list(input().split())
    if zibrish[0] in av:
        add += int(zibrish[0])*int(zibrish[1])
        av[i] = 0 '''
print(av)

nums = list(map(int, input().split()))
a = []
for i in range(nums[1]):
    a.append(list(map(float, input().split())))

zipped = list(zip(*a))
for i in range(len(zipped)):
    x = sum(zipped[i])/nums[1]
    print("%.1f" % x)


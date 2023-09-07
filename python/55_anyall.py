n = int(input())
nums = list(map(int, input().split()))
all_are_positive = all(i > 0 for i in nums)
if all_are_positive == True:
    if any(str(i) == str(i)[::-1] for i in nums):
        print(True)
    else:
        print(False)


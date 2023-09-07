n = int(input())
nums = list(map(int, input().split()))
s = set(nums)
for i in s:
    r = nums.count(i)
    if r == 1:
        print(i)
        break
    else:
        pass
    

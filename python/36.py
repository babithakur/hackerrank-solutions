n = int(input())
for i in range(n):
    nums = list(input().split())
    try:
        div = int(nums[0])//int(nums[1])
        print(div)
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")

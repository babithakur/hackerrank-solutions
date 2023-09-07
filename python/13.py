def average(array):
    s = set(array)
    arr = list(s)
    sum = 0
    for i in range(0, len(arr)):
        sum += arr[i]
    res = sum/len(arr)
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

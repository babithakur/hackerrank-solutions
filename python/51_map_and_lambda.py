cube = lambda x: x*x*x

def fibonacci(n):
    arr = []
    for i in range(n):
        if i == 0:
            arr.append(0)
        elif i == 1:
            arr.append(1)
        else:
            arr.append(arr[i-1]+arr[i-2])
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    

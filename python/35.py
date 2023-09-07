if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        op = list(input().split())
        if op[0] == "insert":
            a.insert(int(op[1]), int(op[2]))
        elif op[0] == "print":
            print(a)
        elif op[0] == "remove":
            a.remove(int(op[1]))
        elif op[0] == "append":
            a.append(int(op[1]))
        elif op[0] == "pop":
            a.pop()
        elif op[0] == "sort":
            a.sort()
        elif op[0] == "reverse":
            a.reverse()




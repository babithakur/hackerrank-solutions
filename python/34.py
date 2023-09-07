if __name__ == '__main__':
    std = []
    scr = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        std.append([name, score])
        scr.add(score)

    num = sorted(scr)[1]
    sec = []
    for i in range(len(std)):
        if num in std[i]:
            sec.append(std[i][0])
    sec.sort()
    for i in range(len(sec)):
        print(sec[i])

    




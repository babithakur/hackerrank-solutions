if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = float(0)
    for i in range(len(student_marks[query_name])):
        total += float(student_marks[query_name][i])
    avg = total/3
    print('%.2f' %avg)

    

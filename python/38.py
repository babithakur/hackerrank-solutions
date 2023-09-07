import calendar
inp = list(map(int, input().split()))
print(calendar.day_name[calendar.weekday(inp[2],inp[0],inp[1])].upper())


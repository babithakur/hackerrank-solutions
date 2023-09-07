def func():
    s = input("Enter a name:\n")
    name = s.split(" ")
    x = ""
    for i in range(0, len(name)):
        x += name[i].capitalize() + " " 
    
    return x

if __name__ == '__main__':
    q = func()
    print(q)

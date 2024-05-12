for _ in range(int(input())):
    a = 0
    for i in input():
        if i == "U":
            a += 1
        else:
            break
    print(a)
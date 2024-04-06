for _ in range(int(input())):
    r, e, c = map(int, input().split())
    a = e - c
    if r == a:
        print("does not matter")
    elif r > a:
        print("do not advertise")
    else:
        print("advertise")
    
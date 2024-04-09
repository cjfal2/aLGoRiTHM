for _ in range(int(input())):
    a = input()
    if a[-1] == ".":
        print(a)
    else:
        print(a,".", sep="")
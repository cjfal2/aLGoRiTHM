for _ in range(int(input())):
    n = input()
    m = n[-2:]
    if (int(n) + 1) % int(m) == 0:
        print("Good")
    else:
        print("Bye")
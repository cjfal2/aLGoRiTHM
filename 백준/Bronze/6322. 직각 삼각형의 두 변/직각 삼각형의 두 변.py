from math import sqrt


tc = 0
while 1:
    tc += 1
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    print(f"Triangle #{tc}")
    answer = 0
    w = ""
    if c == -1:
        answer = a ** 2 + b ** 2
        w = "c"
    elif a == -1:
        answer = c ** 2 - b ** 2
        w = "a"
    else:
        answer = c ** 2 - a ** 2
        w = "b"
    print(f"{w} = {sqrt(answer):.3f}" if answer > 0 else "Impossible.")

    print()

for _ in range(int(input())):
    a, b = input().split()
    a = float(a)
    if b == "kg":
        a *= 2.2046
        b = "lb"
    elif b == "lb":
        a *= 0.4536
        b = "kg"
    elif b == "l":
        a *= 0.2642
        b = "g"
    elif b == "g":
        a *= 3.7854
        b = "l"
    print(f'{a:.4f}', b)
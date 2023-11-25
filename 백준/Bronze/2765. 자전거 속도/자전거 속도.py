N = 0
while True:
    N += 1
    a, b, c = map(float, input().split())
    if b == 0:
        break

    d = b * 3.1415927*(a/12/5280)
    v = d / (c / 60 / 60)

    print(f"Trip #{N}: {d:.2f} {v:.2f}")

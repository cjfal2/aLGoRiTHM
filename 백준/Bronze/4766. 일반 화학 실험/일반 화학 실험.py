a = float(input())
while 1:
    b = float(input())
    if b == 999:
        break
    c = b - a
    a = b
    print(f'{c:.2f}')
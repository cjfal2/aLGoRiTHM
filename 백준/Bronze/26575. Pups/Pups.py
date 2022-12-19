q = input
for _ in range(int(q())):
    a, b, c = map(float, q().split())
    print(f'${a*b*c:.2f}')
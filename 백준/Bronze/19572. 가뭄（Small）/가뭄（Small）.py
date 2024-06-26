d1, d2, d3 = map(int, input().split())
a = (d1 + d2 - d3) / 2
b = (d1 - d2 + d3) / 2
c = (-d1 + d2 + d3) / 2

if a > 0 and b > 0 and c > 0 and abs(a + b - d1) < 1e-6 and abs(a + c - d2) < 1e-6 and abs(b + c - d3) < 1e-6:
    print(1)
    print(f"{a:.1f} {b:.1f} {c:.1f}")
else:
    print(-1)


def solve(a, b, c, d, e):
    return a * 350.34 + b * 230.90 + c * 190.55 + d * 125.30 + e * 180.90

for _ in range(int(input())):
    print(f'${solve(*list(map(int, input().split()))):.2f}')

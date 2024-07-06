colors = set()
for _ in range(2):
    a, b = input().split()
    colors.add(a)
    colors.add(b)

colors = sorted(colors)
for color1 in colors:
    for color2 in colors:
        print(color1, color2)


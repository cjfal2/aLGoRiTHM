a = [input() for _ in range(6)].count("W")
if a >= 5:
    print(1)
elif a >= 3:
    print(2)
elif a >= 1:
    print(3)
else:
    print(-1)
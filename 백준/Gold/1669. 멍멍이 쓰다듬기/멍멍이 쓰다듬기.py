a, b = map(int, input().split())
if a == b:
    print(0)
    quit()

cha = b - a
N = cha ** 0.5

if N == int(N):
    print(int(N) * 2 - 1)
elif cha < int(N) ** 2 + N:
    print(int(N) * 2)
else:
    print(int(N) * 2 + 1)

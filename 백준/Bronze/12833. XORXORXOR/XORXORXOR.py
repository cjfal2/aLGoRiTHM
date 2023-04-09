a, b, c = map(int, input().split())
print(int(bin(a ^ b), 2)) if c%2 else print(a)
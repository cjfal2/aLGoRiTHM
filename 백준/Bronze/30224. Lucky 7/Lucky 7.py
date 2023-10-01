n=int(input())
print((0 if n%7 else 1) if "7" not in str(n) else (2 if n%7 else 3))
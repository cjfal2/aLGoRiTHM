n = int(input())
k = int(input())
x = k + 60
print(n * 1500 if n <= x else x * 1500 + (n - x) * 3000)

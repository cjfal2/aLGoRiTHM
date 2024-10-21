a, b, c = map(int, input().split())
x, z = max(a, b, c), min(a, b, c)
arr = [a, b, c]
arr.remove(x)
arr.remove(z)
y = arr[0]
print(2*x-y-z)
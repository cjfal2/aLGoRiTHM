arr = list(map(int, input().split()))
a = arr.count(1)
b = arr.count(2)
print(1 if a > b else 2)
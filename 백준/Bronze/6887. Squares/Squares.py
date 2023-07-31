N = int(input())
for i in range(N, 0, -1):
    if i**2 <= N:
        print(f"The largest square has side length {i}.")
        break
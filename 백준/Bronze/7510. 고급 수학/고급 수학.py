N = int(input())
for i in range(1, N+1):
    print(f"Scenario #{i}:")
    arr = sorted(map(int, input().split()))
    a = arr[0] ** 2
    b = arr[1] ** 2
    c = arr[2] ** 2
    print("yes" if a+b == c else "no")

    if i != N:
        print()

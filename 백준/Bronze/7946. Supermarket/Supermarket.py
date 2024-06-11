for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = sorted(map(int, input().split()))
    print(arr[k-1])
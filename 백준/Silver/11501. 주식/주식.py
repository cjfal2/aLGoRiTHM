import sys
input = sys.stdin.readline

tc = int(input().strip())
for t in range(tc):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))[::-1]
    answer = 0
    temp = arr[0]
    for a in range(1, n):
        if temp >= arr[a]:
            answer += temp - arr[a]
        else:
            temp = arr[a]
    print(answer)
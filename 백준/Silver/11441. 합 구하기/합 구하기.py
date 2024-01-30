import sys
input = sys.stdin.readline

N = int(input())
arr = [0]
for a in map(int, input().split()):
    arr.append(arr[-1] + a)
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(arr[b] - arr[a-1])
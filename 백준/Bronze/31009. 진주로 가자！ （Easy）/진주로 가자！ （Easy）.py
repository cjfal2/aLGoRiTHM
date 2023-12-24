N = int(input())
arr = []
temp = 0
for _ in range(N):
    a, b = input().split()
    if a == "jinju":
        temp = int(b)
    arr.append((a, int(b)))
answer = 0
for a, b in arr:
    if a != "jinju" and b > temp:
        answer += 1
print(temp)
print(answer)
        
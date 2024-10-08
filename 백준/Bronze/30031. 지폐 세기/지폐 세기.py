n=int(input())
answer=0
temp = {
    136: 1000,
    142: 5000,
    148: 10000,
    154: 50000,
}
for _ in range(n):
    a, b = map(int, input().split())
    answer += temp[a]
print(answer)
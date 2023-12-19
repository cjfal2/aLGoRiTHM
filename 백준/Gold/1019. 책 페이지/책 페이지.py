N = int(input())
answer = [0 for _ in range(10)]
add = 0
num = 1

while N != 0:
    now = N % 10
    N //= 10

    answer[0] -= num
    for i in range(now):
        answer[i] += (N+1)*num

    answer[now] += N*num + 1 + add
    for k in range(now+1, 10):
        answer[k] += N*num

    add += now*num
    num *= 10
print(*answer)
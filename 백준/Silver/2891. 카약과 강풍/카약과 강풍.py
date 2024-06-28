N, S, R = map(int, input().split())
damage = list(map(int, input().split()))
more = list(map(int, input().split()))
for n in range(1, N+1):
    if n in damage and n in more:
        more.remove(n)
        damage.remove(n)

answer = 0
for n in range(1, N+1):
    if n in damage:
        if n-1 in more:
            more.remove(n-1)
        elif n+1 in more:
            more.remove(n+1)
        else:
            answer += 1
print(answer)
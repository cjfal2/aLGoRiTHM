def solution(brown, red):
    t = 1

    while True:
        k = (brown+4-2*t)/2
        if (t-2)*(k-2) == red:
            break
        t += 1
    k = int(k)
    answer = [max(t, k), min(t, k)]
    return answer


b, r = map(int, input().split())
print(*solution(b, r))

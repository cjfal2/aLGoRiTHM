def solution(number):
    answer = 0
    N = len(number)
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                if number[a] + number[b] + number[c] == 0:
                    answer += 1
    return answer
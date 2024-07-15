

def solve(N, M, L, info):
    info = [0] + sorted(info) + [L]  # 시작과 끝 추가 후 정렬


    def is_possible(mid):
        cnt = 0  # 필요 휴게소 수
        for i in range(1, N + 2):
            cnt += (info[i] - info[i - 1] - 1) // mid
        return cnt <= M


    left, right = 1, L - 1
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer


N, M, L = map(int, input().split())
arr = list(map(int, input().split()))

print(solve(N, M, L, arr))

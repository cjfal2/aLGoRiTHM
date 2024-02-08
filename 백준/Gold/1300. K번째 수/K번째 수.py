# 이분 탐색 함수 정의
def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # mid 이하인 원소의 개수를 구함
        cnt = 0
        for i in range(1, N + 1):
            cnt += min(mid // i, N)

        # cnt가 target보다 크거나 같으면 mid 값을 감소시킴
        if cnt >= target:
            result = mid
            end = mid - 1
        # cnt가 target보다 작으면 mid 값을 증가시킴
        else:
            start = mid + 1

    return result


N = int(input())
k = int(input())

print(binary_search(k, 1, k))

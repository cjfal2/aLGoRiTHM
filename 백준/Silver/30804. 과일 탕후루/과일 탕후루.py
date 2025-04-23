import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))

    # 투 포인터로 최대 길이 계산 (서브배열 연속 구간에서 서로 다른 값 개수 <= 2)
    cnt = [0] * 10
    distinct = 0
    ans = 0
    left = 0

    for right in range(N):
        x = arr[right]
        if cnt[x] == 0:
            distinct += 1
        cnt[x] += 1

        # 서로 다른 과일 종류가 3개 이상이면 left 이동
        while distinct > 2:
            y = arr[left]
            cnt[y] -= 1
            if cnt[y] == 0:
                distinct -= 1
            left += 1

        # 현재 구간 [left..right] 길이 갱신
        cur_len = right - left + 1
        if cur_len > ans:
            ans = cur_len

    print(ans)

if __name__ == '__main__':
    main()

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    H = list(map(int, input().split()))

    total = 0

    # 오른쪽 방향 쌍 찾기 (i < j)
    stack = []
    for i in range(N):
        while stack and H[i] > H[stack[-1]]:
            j = stack.pop()
            # 조건: 사이 키 < min(H[i], H[j]) == H[j]
            total += i - j + 1
        stack.append(i)

    # 왼쪽 방향 쌍 찾기 (i > j)
    stack = []
    for i in range(N - 1, -1, -1):
        while stack and H[i] > H[stack[-1]]:
            j = stack.pop()
            total += j - i + 1
        stack.append(i)

    print(total)

main()

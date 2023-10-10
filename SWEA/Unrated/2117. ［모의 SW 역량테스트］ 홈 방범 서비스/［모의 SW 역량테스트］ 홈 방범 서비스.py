def cal_fee(n):
    return n * n + (n-1) * (n-1)


def diamond(k, i, j):
    global answer
    
    cost = -1 * cal_fee(k)
    houses = 0
    for x in range(i-k-1, i+k):
        for y in range(j-k-1, j+k):
            if N > x >= 0 and N > y >= 0 and (k - 1) >= (abs(x-i) + abs(y-j)) and pan[x][y]:
                cost += M
                houses += 1
                
    if houses <= answer or cost < 0:
        return -1
    
    return houses


tc = int(input())
for test_case in range(1, tc + 1):
    N, M = map(int, input().split())  # N: 도시 크기, M: 집이 지불하는 비용
    pan = [list(map(int, input().split())) for _ in range(N)] # 지도
    
    answer = 0
    # k를 지정해주기
    for a in range(1, N+N):
        for n in range(N):
            for m in range(N):
                h = diamond(a, n, m)
                if h != -1:
                    answer = max(answer, h)
    
    print(f'#{test_case} {answer}')
    
    
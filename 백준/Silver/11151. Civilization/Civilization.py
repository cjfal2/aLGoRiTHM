import sys
input = sys.stdin.readline

def solve():
    T = int(input().strip())
    results = []
    
    for _ in range(T):
        N = int(input().strip())  # 지역 개수
        W, C, F = map(int, input().strip().split())  # 목표 값
        regions = [tuple(map(int, input().strip().split())) for _ in range(N)]  # 지역 정보

        min_regions = float('inf')

        # 모든 부분 집합 탐색 (비트마스킹)
        for bit in range(1, 1 << N):
            total_w = total_c = total_f = 0
            count = 0

            for i in range(N):
                if bit & (1 << i):  # i번째 지역 선택
                    total_w += regions[i][0]
                    total_c += regions[i][1]
                    total_f += regions[i][2]
                    count += 1

            # 목표를 달성했을 때 최소 개수 갱신
            if total_w >= W and total_c >= C and total_f >= F:
                min_regions = min(min_regions, count)

        # 출력 결과 저장
        results.append(str(min_regions) if min_regions != float('inf') else "game over")

    # 최종 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

solve()

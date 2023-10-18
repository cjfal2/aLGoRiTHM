N, L = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]


def road(arr):
    visited = [0 for _ in range(N)]  # 경사로 놓은 곳
    for m in range(1, N):
        # 높이 차이 2 이상이면 그냥 끝냄
        if abs(arr[m-1] - arr[m]) >= 2:
            return False

        # 내리막길이라면
        if arr[m-1] > arr[m]:
            # L 만큼 앞으로 판별 (현재 포함 => 이미 경사로가 있는 곳 일 수도 있기 때문)
            for k in range(L):
                # 설치 불가: 범위 초과
                if m+k >= N:
                    return False

                # 설치 불가: 이미 설치된 곳
                if visited[m+k]:
                    return False

                # 설치 불가: 높이가 다름
                if arr[m] != arr[m+k]:
                    return False

                # 경사로 놓기
                visited[m+k] = 1

        # 오르막 길이라면
        elif arr[m-1] < arr[m]:
            # L 만큼 뒤로 판별 (현재 미포함 => 이미 경사로가 있는 곳 일 수도 있기 때문)
            for k in range(L):
                # 설치 불가: 범위 초과
                if m-1-k < 0:
                    return False

                # 설치 불가: 이미 설치된 곳
                if visited[m-1-k]:
                    return False

                # 설치 불가: 높이가 다름
                if arr[m-1] != arr[m-1-k]:
                    return False

                # 경사로 놓기
                visited[m-1-k] = 1

    return True


answer = 0
for n in range(N):
    answer += road(pan[n])
    answer += road(list(pan[p][n] for p in range(N)))

print(answer)

def check(array):
    visited = [0 for _ in range(N)]
    flag = 0
    for m in range(1, N):
        if visited[m]:
            continue

        if abs(array[m-1] - array[m]) > 1:
            return False

        elif array[m-1] - array[m] == 1:  # 이전이 지금보다 1높은 경우
            if flag:  # 경사로를 지어야하는데 숫자가 다른 경우 컷
                return False

            if m + X - 1 >= N:
                return False

            visited[m] = 1
            flag = 1

        elif array[m-1] - array[m] == -1:  # 이전이 지금보다 1낮은 경우
            for prev in range(m-1, m-X-1, -1):
                if prev < 0:
                    return False

                if visited[prev]:  # 경사로를 못지음 컷
                    return False
                visited[prev] = 1

        else:  # 같은 숫자일 경우
            if flag:  # 근데 경사로를 세워야하는 경우
                visited[m] = 1
                flag += 1
                if flag == X:  # 경사로 완성
                    flag = 0
            else:
                continue
    # print(array, visited)
    return True


test_case = int(input())
for tc in range(1, test_case+1):
    N, X = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_trans = list(map(list, zip(*arr)))
    answer = 0
    for n in range(N):
        # 평지인경우
        if len(set(arr[n])) == 1:
            answer += 1
        # 경사지인 경우
        else:
            answer += check(arr[n])

        if len(set(arr_trans[n])) == 1:
            answer += 1
        else:
            answer += check(arr_trans[n])
    print(f'#{tc} {answer}')

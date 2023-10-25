N, M = map(int, input().split())  # N: 구멍의 수, M: 햄스터 크기
arr = list(map(int, input().split()))  # 구멍의 정보

left, right, hap, answer = 0, 0, arr[0], 0
# 왼포인터, 오른포인터, 합, 답

while 1:  # 오른쪽이 넘어가면 종료할 것임
    if hap <= M:  # 합이 부피보다 작거나 크다면
        answer = max(answer, hap)  # 최대값을 갱신해주고

        right += 1  # 오른쪽 포인터를 먼저옮겨서 끝나는 거랑 합을 체크
        if right == N:  # 넘었다면 끝
            print(answer)
            break

        hap += arr[right]  # 다음 포인터의 합을 저장

    elif hap > M:  # 합이 부피보다 크다면
        hap -= arr[left]  # 맨 왼쪽 부분을 합에서 빼주고
        left += 1  # 왼쪽 포인터를 옮김

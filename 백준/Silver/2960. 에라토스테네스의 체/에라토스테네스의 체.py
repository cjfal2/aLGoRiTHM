def eratosthenes(N, K):
    numbers = [True] * (N + 1)  # True는 아직 지워지지 않은 상태
    cnt = 0  # 지워진 숫자의 개수

    for i in range(2, N + 1):  # 2부터 N까지 순회
        if numbers[i]:  # i가 아직 지워지지 않았다면
            for j in range(i, N + 1, i):  # i의 배수들 순회
                if numbers[j]:  # j가 아직 지워지지 않았다면
                    numbers[j] = False  # j를 지움
                    cnt += 1  # 지운 숫자 개수 증가
                    if cnt == K:  # K번째 지워진 수라면
                        return j  # j를 반환

                    
N, K = map(int, input().split())
print(eratosthenes(N, K))

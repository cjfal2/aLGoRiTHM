import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    W, K = input().strip(), int(input().strip())
    if K == 1:
        print(1, 1)
        continue
    
    # 알파벳 문자별 등장 빈도수 저장
    count_w = [0 for _ in range(26)]
    for what in W:
        count_w[ord(what) - 97] += 1

    long = len(W) # 문자열의 길이
    MIN = long+1 # 최소값
    MAX = -1 # 최대값
    for i in range(long-1): # 처음부터 (끝 - 1) 까지 탐색
        # 빈도수가 K 이상인 문자만 이용
        if count_w[ord(W[i]) - 97] >= K:
            cnt = 0
            for j in range(i, long): # i 부터 끝까지 탐색
                # 연속 문자열의 시작 문자 W[i]가 W[j] 와 같으면 카운팅
                if W[i] == W[j]:
                    cnt += 1

                if cnt == K:  # 카운트 수가 정확히 K와 같으면 길이 업데이트하고 탈출
                    MIN = min(MIN, j - i + 1)
                    MAX = max(MAX, j - i + 1)
                    break

    if MIN == long+1 or MAX == -1: # 변한게 없다면
        print(-1)
    else:
        print(MIN, MAX)

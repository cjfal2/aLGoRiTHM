import sys
input = sys.stdin.readline

string_A = '_'+input().strip()
string_B = '_'+input().strip()

N = len(string_A)
M = len(string_B)

LCS = [[0]*(M) for _ in range((N))]

for i in range(N):
    for j in range(M):
        if i == 0 or j == 0:  # 마진 설정
            LCS[i][j] = 0
        elif string_A[i] == string_B[j]:
            LCS[i][j] = LCS[i - 1][j - 1] + 1
        else:
            LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])

print(LCS[N-1][M-1])
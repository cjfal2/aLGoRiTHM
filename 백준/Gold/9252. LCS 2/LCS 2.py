import sys
input = sys.stdin.readline

string_A = input().strip()
string_B = input().strip()

N = len(string_A)
M = len(string_B)


LCS = [['']*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        if string_A[i-1] == string_B[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + string_A[i-1]
        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]


print(len(LCS[N][M]))
print(LCS[N][M])

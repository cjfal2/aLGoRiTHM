import sys
input = sys.stdin.readline

def mat_add(A, B, M):
    N = len(A)
    return [[(A[i][j] + B[i][j]) % M for j in range(N)] for i in range(N)]

def mat_mul(A, B, M):
    N = len(A)
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for k in range(N):
            if A[i][k]:
                aik = A[i][k]
                row_i = res[i]
                row_bk = B[k]
                for j in range(N):
                    row_i[j] = (row_i[j] + aik * row_bk[j]) % M
    return res

def solve(k):
    # returns (S(k) = A + A^2 + ... + A^k, P(k) = A^k)
    if k == 1:
        return (A_mod, A_mod)
    if k % 2 == 0:
        half_s, half_p = solve(k // 2)
        p_k = mat_mul(half_p, half_p, M)                      # A^(k/2) * A^(k/2) = A^k
        s_k = mat_add(half_s, mat_mul(half_p, half_s, M), M)  # S + A^(k/2)*S
        return (s_k, p_k)
    else:
        prev_s, prev_p = solve(k - 1)
        p_k = mat_mul(prev_p, A_mod, M)                       # A^(k-1) * A = A^k
        s_k = mat_add(prev_s, p_k, M)                         # S(k-1) + A^k
        return (s_k, p_k)

# 입력
N, K, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# **여기서** 반드시 A를 M으로 나눠줍니다!
A_mod = [[x % M for x in row] for row in A]

# 계산
S, _ = solve(K)

# 출력
out = []
for row in S:
    out.append(' '.join(str(x) for x in row))
print('\n'.join(out))

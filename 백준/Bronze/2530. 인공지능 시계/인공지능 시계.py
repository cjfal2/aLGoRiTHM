H, M, S = map(int, input().split())
N = int(input()) 

S += N % 60
N //= 60
if S >= 60:
    S %= 60
    M += 1

M += N % 60
N //= 60
if M >= 60:
    M %= 60
    H += 1

H += N % 24
if H >= 24:
    H %= 24

print(H,M,S)
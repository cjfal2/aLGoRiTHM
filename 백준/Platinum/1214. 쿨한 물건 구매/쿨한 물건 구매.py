D, P, Q = map(int, input().split())

if not D % P or not D % Q:
    print(D)
    quit()

P, Q = max(P, Q), min(P, Q)
MAX = D // P + 1
ans = P * MAX

for i in range(MAX-1, -1, -1):
    A, B = divmod((D - (i * P)), Q)
    if not B:
        print(D)
        quit() 
    K = (i * P) + ((A + 1) * Q)
    if ans == K:
        break
    ans = min(ans, K)
print(ans)
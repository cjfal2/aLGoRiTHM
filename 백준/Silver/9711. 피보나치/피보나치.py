import sys
input = sys.stdin.readline


tc = int(input().strip())
pibo = [0 for _ in range(10001)]
for k in range(tc):
    P, Q = map(int, input().split())
    pibo[0] = pibo[1] = 1
    for i in range(2, P):
        if not pibo[i]:
            pibo[i] = pibo[i-1] + pibo[i-2]
    
    print(f'Case #{k+1}: {pibo[P-1]%Q}')
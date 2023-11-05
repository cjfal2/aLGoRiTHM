pibo = [0 for _ in range(41)]
pibo[0] = pibo[1] = 1
for i in range(2, 41):
    pibo[i] = pibo[i-1] + pibo[i-2]

N = int(input())
answer = 1
idx = 1
for _ in range(int(input())):
    M = int(input())
    answer *= pibo[M-idx]
    idx = M + 1

print(answer * pibo[N-idx+1])
N,L,W,H=map(int,input().split())
start, end = 0, max(L,W,H)
for _ in range(100):
    middle = (start+end)/2
    if (L//middle)*(W//middle)*(H//middle) >= N:
        start = middle
    else:
        end = middle
print(f'{end:.10f}')
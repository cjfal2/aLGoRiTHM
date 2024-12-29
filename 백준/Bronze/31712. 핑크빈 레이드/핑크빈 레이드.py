cu, du = map(int, input().split())
cd, dd = map(int, input().split())
cp, dp = map(int, input().split())
H = int(input())

for h in range(H):
    if h % cu == 0:
        H -= du
    if h % cd == 0:
        H -= dd
    if h % cp == 0:
        H -= dp
    if H <= 0:
        print(h)
        break

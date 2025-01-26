n, k, t = map(int, input().split())
v = list(map(int, input().split()))

v.sort()

start, end, d = 0, n - 1, 0

# start가 범위를 벗어나지 않도록 조건 추가
while start < n and v[start] == 0:
    start += 1
    d += 1

while start <= end:
    if start == end:
        if v[start] >= k:
            d += 1
        break

    need = k - v[end]
    if t < need:
        break

    if start < n and v[start] == need:  # start가 범위 내에 있는지 확인
        t -= need
        end -= 1
        start += 1
        d += 2
    elif start < n and v[start] > need:  # start가 범위 내에 있는지 확인
        v[start] -= need
        t -= need
        end -= 1
        d += 1
    elif start < n and v[start] < need:  # start가 범위 내에 있는지 확인
        v[end] += v[start]
        t -= v[start]
        start += 1
        d += 1

    if t <= 0:
        break

if d >= n:
    print("YES")
else:
    print("NO")

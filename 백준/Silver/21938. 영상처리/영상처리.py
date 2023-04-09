N, M = map(int, input().split())
pixel = []
for _ in range(N):
    j = 0
    temp1 = []
    temp2 = []
    for i in list(map(int, input().split())):
        temp1.append(i)
        j += 1
        if j == 3:
            j = 0
            temp2.append(sum(temp1)/3)
            temp1 = []
    pixel.append(temp2)


K = int(input())
ans = 0
for n in range(N):
    for m in range(M):
        if pixel[n][m] >= K and pixel[n][m] != 256:
            ans += 1
            q = [(n, m)]
            pixel[n][m] = 256
            while q:
                x, y = q.pop(0)
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if N > nx >= 0 and M > ny >= 0 and pixel[nx][ny] >= K and pixel[nx][ny] != 256:
                        pixel[nx][ny] = 256
                        q.append((nx, ny))
                # print(pixel)
print(ans)

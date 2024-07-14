dix = [(-3, -2), (-3, 2), (-2, 3), (2, 3), (3, 2), (3, -2), (2, -3), (-2, -3)]


def inner_check(a, b):
    if 10 > a >= 0 and 9 > b >= 0:
        return True
    return False


def check(direction, i, j):
    if direction == 0:
        i -= 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        
        i -= 1
        j -= 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        i -= 1
        j -= 1
        if not inner_check(i, j):
            return False
        return True

    if direction == 1:
        i -= 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        
        i -= 1
        j += 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        i -= 1
        j += 1
        if not inner_check(i, j):
            return False
        return True

    if direction == 2:
        j += 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        
        i -= 1
        j += 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        i -= 1
        j += 1
        if not inner_check(i, j):
            return False
        return True

    if direction == 3:
        j += 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        
        i += 1
        j += 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        i += 1
        j += 1
        if not inner_check(i, j):
            return False
        return True

    if direction == 4:
        i += 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        
        i += 1
        j += 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        i += 1
        j += 1
        if not inner_check(i, j):
            return False
        return True

    if direction == 5:
        i += 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        
        i += 1
        j -= 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        i += 1
        j -= 1
        if not inner_check(i, j):
            return False
        return True

    if direction == 6:
        j -= 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        
        i += 1
        j -= 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        i += 1
        j -= 1
        if not inner_check(i, j):
            return False
        return True

    if direction == 7:
        j -= 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        
        i -= 1
        j -= 1
        if not inner_check(i, j):
            return False
        if pan[i][j]:
            return False
        i -= 1
        j -= 1
        if not inner_check(i, j):
            return False
        return True


pan = [[0 for _ in range(9)] for _ in range(10)]
visited = [[0 for _ in range(9)] for _ in range(10)]

a, b = map(int, input().split())
q = [(a, b, 0)]
visited[a][b] = 1

a, b = map(int, input().split())
pan[a][b] = 1

answer = -1
while q:
    x, y, move = q.pop(0)
    if pan[x][y]:
        answer = move
        break

    for d in range(8):
        nx, ny = x + dix[d][0], y + dix[d][1]
        if inner_check(nx, ny) and not visited[nx][ny] and check(d, x, y):
            q.append((nx, ny, move+1))
            visited[nx][ny] = 1
            
print(answer)

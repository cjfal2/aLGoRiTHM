A, B, C = map(int, input().split())
q = [(A, B, C)]
visited = set()  # 방문 기록
visited.add((A, B, C))
answer = 0

while q:
    A, B, C = q.pop(0)

    if A == B == C:
        answer = 1
        break

    temp = [A, B, C]
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        x, y = temp[i], temp[j]

        if x == y:
            continue

        if x > y:
            x, y = y, x  # x가 더 작은 값이 되도록 스왑

        x, y = x + x, y - x
        ntemp = temp[:]
        ntemp[i] = x
        ntemp[j] = y
        ntemp = tuple(sorted(ntemp))  # 상태를 정렬하여 방문 기록 관리

        if ntemp not in visited:
            visited.add(ntemp)
            q.append(ntemp)

print(answer)

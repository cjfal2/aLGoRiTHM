A, B, C = map(int, input().split())  # 물통의 크기
total = [A, B, C]
queue = [(0, 0, C)]
visited = set([(0, 0, C)])
answer = set([C])
while queue:
    a, b, c = queue.pop(0)
    if a == 0:
        answer.add(c)  # 답을 위해 c에 남을 물의 양을 추가

    # A->B, A->C, B->A, B->C, C->A, C->B
    for start, end in (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1):
        # start 에서 end로 물을 넘겨 보고 visited를 확인한다.
        # ex A -> B 라고 한다면 A에서는 res_b 만큼 빼주고 b는 A에서 res_b를 뺀 만큼 더해준다.x

        amount = [a, b, c]  # 물을 옮기기위한 리스트
        res = [A - a, B - b, C - c]  # 각 물통에 남은 물의 양

        # start에서 이동할 수 있는 양을 구해야함
        # 남은 양만큼 이동할 수 있고, 
        moved_water_amount = res[end]

        # 마이너스로 가는 것을 막기위해 여기서 조건을 걸어줘야함
        if moved_water_amount <= 0:
            continue
        
        # res보다 start가 작은 경우
        if moved_water_amount > amount[start]:
            moved_water_amount = amount[start]


        new_amount_start = amount[start] - moved_water_amount
        new_amount_end = amount[end] + moved_water_amount

        if 0 > new_amount_start or new_amount_start > total[start]:
            continue

        if 0 > new_amount_end or new_amount_end > total[end]:
            continue

        amount[start] = new_amount_start
        amount[end] = new_amount_end

        amount_tuple = tuple(amount)
        if amount_tuple not in visited:
            queue.append(amount_tuple)
            visited.add(amount_tuple)

print(*sorted(answer))
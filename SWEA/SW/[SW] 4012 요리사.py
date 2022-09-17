for tc in range(int(input())):
    N = int(input())
    foods = [list(map(int, input().split())) for _ in range(N)]
    food_num = list(range(N))
    combi = []
    comfood = []
    for i in range(1 << len(food_num)):
        s = []
        for j in range(len(food_num)):
            if i & (1 << j):
                s.append(food_num[j])
            if len(s) == N//2:
                comfood.append(s)
    for a in comfood:
        res_food = []
        for x in food_num:
            if x not in a:
                res_food.append(x)
        Q1 = []
        Q2 = []
        for x in a:
            for y in a:
                Q1.append(foods[x][y])
        for x in res_food:
            for y in res_food:
                Q2.append(foods[x][y])
        combi.append(abs(sum(Q1) - sum(Q2)))
    print(f'#{tc+1} {min(combi)}')
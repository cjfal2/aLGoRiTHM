max_num = -1
where_h, where_w = 0, 0

for i in range(1, 10):
    j = 0
    for num in list(map(int, input().split())):
        j += 1
        if num >= max_num:
            max_num, where_h, where_w = num, i, j
print(max_num)
print(where_h, where_w)
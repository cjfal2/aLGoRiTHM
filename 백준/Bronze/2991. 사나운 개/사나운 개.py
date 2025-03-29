def is_attacking(t, attack, rest):
    cycle = attack + rest
    in_cycle = t % cycle
    return 1 <= in_cycle <= attack

A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())


for t in [P, M, N]:
    count = 0
    if is_attacking(t, A, B):
        count += 1
    if is_attacking(t, C, D):
        count += 1
    print(count)

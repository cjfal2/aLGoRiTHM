for tc in range(int(input())):
    N = int(input())
    bus = [0 for _ in range(1002)]
    for _ in range(N):
        T, A, B = map(int, input().split())
        if T == 1:
            L = [A] + [i for i in range(A+1, B)] + [B]
            for a in L:
                bus[a] += 1

        elif T == 2:
            L = [A] + [i for i in range(A + 2, B, 2)] + [B]
            for a in L:
                bus[a] += 1

        elif T == 3:
            Q = [i for i in range(A+1, B)]
            L = [A]
            if A % 2:
                for i in Q:
                    if i % 3 == 0 and i % 10 != 0:
                        L.append(i)
            else:
                for i in Q:
                    if i % 4 == 0:
                        L.append(i)
            L += [B]
            for a in L:
                bus[a] += 1

    print(max(bus))

for tc in range(int(input())):
    cont, truck = map(int, input().split())
    cont_w = sorted(list(map(int, input().split())), reverse = True)
    truck_can = sorted(list(map(int, input().split())), reverse = True)

    co = 0
    copycat = cont_w[:]
    while truck_can:
        if not copycat:
            break
        can = truck_can.pop(0)
        while copycat:
            cw = copycat.pop(0)
            if cw <= can:
                co += cw
                break
    print(f'#{tc+1} {co}')



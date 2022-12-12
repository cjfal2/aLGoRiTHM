base = 'abcdefghijklmnopqrstuvwxyz'
for tc in range(int(input())):
    co = 0
    for idx, w in enumerate(input()):
        if base[idx] == w:
            co += 1
        else:
            break
    print(f'#{tc+1} {co}')
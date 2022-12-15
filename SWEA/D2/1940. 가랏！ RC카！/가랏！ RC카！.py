for tc in range(int(input())):
    length = 0
    v = 0
    for _ in range(int(input())):
        value = input().split()
        if value[0] == '0' :
            v = v
            length += v
        elif value[0] == '1' :
            v += int(value[1])
            length += v
        else :
            if int(value[1]) > v :
                v = 0
                length = length
            else :
                v -= int(value[1])
                length += v
    print(f'#{tc+1} {length}')

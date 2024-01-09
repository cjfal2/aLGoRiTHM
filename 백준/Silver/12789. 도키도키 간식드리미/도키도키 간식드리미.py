N = int(input())
origin_line = list(map(int, input().split()))
wait_line = []
number = 1
while origin_line:
    x = origin_line.pop(0)
    if x != number:
        wait_line.append(x)
    else:
        number += 1
    
    while wait_line:
        if wait_line[-1] == number:
            number += 1
            wait_line.pop()
        else:
            break

if wait_line:
    print("Sad")
else:
    print("Nice")
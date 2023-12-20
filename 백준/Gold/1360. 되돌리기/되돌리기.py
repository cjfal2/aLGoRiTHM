N = int(input())
answer = []
text = ''

for _ in range(N):
    command, w, second = input().split()
    
    if command == 'type':
        text += w
        answer.append((int(second), text))
    else:
        w, second = int(w), int(second)
        for i in range(len(answer) - 1, -1, -1):
            if answer[i][0] >= second - w:
                continue

            text = answer[i][1]
            answer.append((second, text))
            break
        else:
            text = ''
            answer.append((second, text))

print(answer[-1][1])

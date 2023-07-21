N = int(input())
crane = sorted(map(int, input().split()), reverse=1)
M = int(input())
boxes = sorted(map(int, input().split()), reverse=1)

if max(crane) < max(boxes):
    print(-1)
    quit()

answer = 0
while boxes:
    for c in crane:
        for b in range(len(boxes)):
            if boxes[b] <= c:
                boxes.pop(b)
                break
    answer += 1
print(answer)
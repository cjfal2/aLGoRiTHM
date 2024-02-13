N, K = map(int, input().split())
str = input()

if K > N // 2:
    K = N // 2

x, y = 0, 0
for _ in range(K):
    for c in str:
        if c == 'U':
            x += 1
        elif c == 'D':
            x -= 1
        elif c == 'L':
            y -= 1
        else:
            y += 1

        if x == 0 and y == 0:
            print("YES")
            quit()
print("NO")

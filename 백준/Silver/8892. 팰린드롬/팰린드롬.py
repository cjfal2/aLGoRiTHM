import sys
input = sys.stdin.readline

def pal(n, w):
    for x in range(n):
        for y in range(n):
            if x != y:
                temp = w[x] + w[y]
                if temp == temp[::-1]:
                    return temp
    return 0

for _ in range(int(input().strip())):
    N = int(input().strip())

    words = [input().strip() for _ in range(N)]
    print(pal(N, words))
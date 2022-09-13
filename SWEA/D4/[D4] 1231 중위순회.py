import sys
sys.stdin = open('s1.txt', 'r')


def inorder(n):
    if n:
        inorder(ch1[n])
        print(words[n], end="")
        inorder(ch2[n])


for tc in range(1, 11):
    print(f'#{tc}', end=" ")
    V = int(input())
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    words = [0] * (V+1)
    for i in range(V):
        L = list(input().split())
        node = int(L[0])
        word = L[1]
        words[node] = word
        if len(L) > 2:
            for j in L[2:]:
                if ch1[node] == 0:
                    ch1[node] = int(j)
                else:
                    ch2[node] = int(j)
    order = []
    inorder(1)
    print()
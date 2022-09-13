def preorder(n):
    if n:
        print(G[n], end="")
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(G[n], end="")
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(G[n], end="")


def trans(w):
    return ord(w)-64


N = int(input())
G = [0] * (N+1)
ch1 = [0] * (N+1)
ch2 = [0] * (N+1)
for i in range(1, N+1):
    a, b, c = input().split()
    G[trans(a)] = a
    if b != '.':
        ch1[trans(a)] = trans(b)
    if c != '.':
        ch2[trans(a)] = trans(c)
preorder(1)
print()
inorder(1)
print()
postorder(1)
print()

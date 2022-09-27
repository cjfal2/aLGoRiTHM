def postorder(n):

    postorder(ch1[n])
    postorder(ch2[n])
    print(n)


def preorder(n):
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])


G = []
while 1:
    try:
        G.append(int(input()))
    except:
        break
print(G)
N = len(G)
num1 = 1
num2 = 1
PRE = [0 for _ in range(N+1)]
POST = [0 for _ in range(N+1)]
U = [0 for _ in range(N+1)]
T = [0 for _ in range(N+1)]
treepre(num1)
treepost(num2)
print(PRE)
print(POST)
for idx, i in enumerate(G, 1):
    a = PRE.index(idx)
    U[a] = i
for idx, i in enumerate(G, 1):
    a = POST.index(idx)
    T[a] = i
print(U)
print(T)

ch1 = [0]*(N+1)
ch2 = [0]*(N+1)



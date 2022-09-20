"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""


def preorder(n):
    if n:
        print(n)
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)


E = int(input())
arr = list(map(int, input().split()))
V = E + 1
root = 1
# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*V
ch2 = [0]*V
for i in range(len(arr)//2):
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0: # 아직 자식이 없으면
        ch1[p] = c
    else:
        ch2[p] = c
print(ch1)
# [0, 2, 4, 5, 7, 8, 10, 12, 0, 0, 0, 13, 0, 0]
print(ch2)
# [0, 3, 0, 6, 0, 9, 11, 0, 0, 0, 0, 0, 0, 0]
print("---전위---")
preorder(root)
"""
1
2
4
7
12
3
5
8
9
6
10
11
13
"""
print("---중위---")
inorder(root)
"""
12
7
4
2
1
8
5
9
3
10
6
13
11
"""
print("---후위---")
postorder(root)
"""
12
7
4
2
8
9
5
10
13
11
6
3
1
"""


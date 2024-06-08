A, B = input().split()

for i, a in enumerate(A):
    if a in B:
        j = B.index(a)  # B에서 a가 처음 등장하는 위치
        break

for k in range(len(B)):
    line = ["."] * len(A)
    if k == j:
        line = list(A)
    line[i] = B[k]
    print("".join(line))

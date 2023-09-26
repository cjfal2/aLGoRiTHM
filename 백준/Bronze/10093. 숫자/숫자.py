A, B = map(int, input().split())

if A == B or A - B == 1 or B - A == 1:
    print(0)
    quit()


A, B = min(A, B), max(A, B)
print(B-A-1)
for i in range(A+1, B-1):
    print(i, end=" ")
print(B-1)
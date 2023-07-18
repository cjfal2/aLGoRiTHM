N = int(input())

if N == 1:
    print("A")
    quit()

L = list(map(int, input().split()))

if N == 2:
    print("A") if L[0] != L[1] else print(L[0])
    quit()

num1, num2, num3 = L[0], L[1], L[2]
temp1 = num2 - num1
a = (num3 - num2) // (num2 - num1) if temp1 != 0 else 0
b = num2 - num1 * a
for n in range(2, N):
    if L[n-1] * a + b != L[n]:
        print("B")
        quit()
print(L[-1] * a + b)

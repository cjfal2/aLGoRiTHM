import sys


def find_min(what):
    result = sys.maxsize
    for i in range(6):
        for j in range(6):
            if i != j and reverse[i] != j:
                if what == 2:
                    result = min(result, L[i]+L[j])
                else:
                    for k in range(6):
                        if k != i and k != j and reverse[i] != k and reverse[j] != k:
                            result = min(result, L[i]+L[j]+L[k])

    return result

reverse = [5, 4, 3, 2, 1, 0]


N = int(input())
L = list(map(int, input().split()))

sml = min(L)
big = max(L)
if N == 1:
    print(sum(L) - big)
    quit()


one = (5 * N * N - 16 * N + 12) * sml
two = (8 * N - 12)  * find_min(2)
sam = 4 * find_min(3)

print(one + two + sam)

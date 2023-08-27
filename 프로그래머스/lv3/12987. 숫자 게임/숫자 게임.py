from collections import deque


def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a, b = 0, 0
    while b < len(A):
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1
    return answer
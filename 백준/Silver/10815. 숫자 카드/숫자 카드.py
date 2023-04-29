import sys
input = sys.stdin.readline


def bi(arr,N,target):
    L = 0
    R = N-1
    while L<=R:
        mid = (L+R)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            R = mid-1
        else:
            L = mid+1
    return 0

N = int(input().strip())
A = list(map(int,input().strip().split()))
A.sort()

M = int(input().strip())
B = list(map(int,input().strip().split()))
F = []
for i in B:
    F.append(bi(A,N,i))
print(*F)
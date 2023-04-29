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

N = int(input())
A = sorted(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
F = []
for i in B:
    F.append(bi(A,N,i))
print(*F)
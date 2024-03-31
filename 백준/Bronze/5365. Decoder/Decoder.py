n = int(input())
arr = input().split()
before = len(arr[0])
answer = arr[0][0]
for a in arr[1:]:
    answer += a[before-1] if len(a) >= before else " "
    before = len(a)
print(answer)

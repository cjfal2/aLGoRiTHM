n = int(input())
nums = list(map(int, input().split()))
answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        answer += abs(nums[i] - nums[j])
print(answer*2)
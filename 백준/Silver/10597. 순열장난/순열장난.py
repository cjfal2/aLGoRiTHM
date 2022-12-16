def dfs(start):
    if start == len(nums):
        print(*s)
        quit()

    num_1 = int(nums[start])
    if not visited[num_1]:
        visited[num_1] = 1
        s.append(num_1)
        dfs(start+1)
        s.pop()
        visited[num_1] = 0

    if start+1 < len(nums):
        num_2 = int(nums[start:start+2])
        if num_2 <= N and not visited[num_2]:
            visited[num_2] = 1
            s.append(num_2)
            dfs(start+2)
            s.pop()
            visited[num_2] = 0


nums = input()
if len(nums) < 10:
    N = len(nums) 
else:
    N = 9 + (len(nums) - 9) // 2
visited = [0 for _ in range(N + 1)]
s = []
dfs(0)
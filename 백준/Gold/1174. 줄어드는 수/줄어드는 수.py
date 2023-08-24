n = int(input())
down = set()
numbers = []

def dfs():
    if numbers:
        num = ""
        for m in numbers:
            num += str(m)
            
        down.add(int(num))

    for i in range(10):
        if not numbers or numbers[-1] > i:
            numbers.append(i)
            dfs()
            numbers.pop()

dfs()

if len(down) >= n:
    print(sorted(down)[n-1])
else:
    print(-1)
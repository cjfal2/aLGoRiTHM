from collections import deque
import sys
input = sys.stdin.readline

queue = deque()
result = []

for _ in range(int(input())):
    command = input().split()
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        result.append(queue.popleft() if queue else -1)
    elif command[0] == "size":
        result.append(len(queue))
    elif command[0] == "empty":
        result.append(1 if not queue else 0)
    elif command[0] == "front":
        result.append(queue[0] if queue else -1)
    elif command[0] == "back":
        result.append(queue[-1] if queue else -1)

sys.stdout.write("\n".join(map(str, result)) + "\n")
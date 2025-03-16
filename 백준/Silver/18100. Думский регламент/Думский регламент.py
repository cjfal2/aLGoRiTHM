import sys
input = sys.stdin.readline

K = int(input().strip())
stack = []

for _ in range(K):
    command = input().strip().split()
    action, party = command[0], command[1]

    if action == "Add":
        stack.append(party)
    elif action == "Vote":
        if not stack or stack[-1] != party:
            print("No")
            exit()
        stack.pop()

print("Yes" if not stack else "No")

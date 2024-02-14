def dfs(x):
    node, depth, _ = x
    print("--"*depth, end="")
    print(node)
    for w in tree[x]:
        dfs(w)


N = int(input())

tree = {0: set()}
for _ in range(N):
    temp = input().split()
    parent_node = 0
    for i in range(1, len(temp)):
        tree[parent_node].add((temp[i], i-1, parent_node))
        parent_node = (temp[i], i-1, parent_node)
        if parent_node not in tree:
            tree[parent_node] = set()

for i in tree:
    tree[i] = sorted(tree[i])

for node in tree[0]:
    dfs(node)

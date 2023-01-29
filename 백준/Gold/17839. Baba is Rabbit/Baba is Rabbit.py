import sys
input = sys.stdin.readline

bababa = {}
for _ in range(int(input().strip())):
    a,b,c = input().strip().split()
    if a not in bababa:
        bababa[a] = [c]
    else:
        bababa[a].append(c)
memo = set()
memo.add("Baba")
q = ["Baba"]
while q:
    w = q.pop(0)
    changes = bababa.get(w)
    if changes:
        for x in changes:
            if x not in memo:
                memo.add(x)
                q.append(x)
memo.remove("Baba")
for i in sorted(memo):
    print(i)

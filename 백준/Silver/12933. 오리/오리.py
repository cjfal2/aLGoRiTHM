ducks = input()
if len(ducks)%5:
    print(-1)
    quit()

duct = {'q': 0,'u': 1,'a': 2,'c': 3,'k': 4}
ori = [0 for _ in range(1000)]
ans = []
for sori in ducks:
    for i in range(1000):
        if ori[i] == duct.get(sori):
            ori[i] += 1
            if ori[i] == 5:
                ori[i] = 0
                ans.append(i)
            break
# print(len(set(ori)))
if len(set(ori)) > 1:
    print(-1)
    quit()
print(len(set(ans))) if len(set(ans)) else print(-1)
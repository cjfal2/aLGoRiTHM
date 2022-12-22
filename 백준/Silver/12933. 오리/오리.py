ducks = input()
if len(ducks)%5:
    print(-1)
    quit()

def duck():
    ductinary = {'q': 0,'u': 1,'a': 2,'c': 3,'k': 4}
    ori = [0 for _ in range(500)]
    ans = []
    for sori in ducks:
        what = ductinary.get(sori)
        for i in range(500):
            if ori[i] == what:
                ori[i] += 1
                if ori[i] == 5:
                    ori[i] = 0
                    if i not in ans:
                        ans.append(i)
                break

    print(len(ans)) if len(ans) and len(set(ori)) == 1 else print(-1)
    return
duck()
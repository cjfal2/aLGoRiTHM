s = input()
if len(s)%5:
    print(-1)
    quit()
def d():
    y={'q':0,'u':1,'a':2,'c':3,'k':4}
    o=[0 for _ in range(500)]
    a=[]
    for r in s:
        w = y.get(r)
        for i in range(500):
            if o[i] == w:
                o[i] += 1
                if o[i] == 5:
                    o[i] = 0
                    if i not in a:
                        a.append(i)
                break
    print(len(a)) if len(a) and len(set(o)) == 1 else print(-1)
    return
d()
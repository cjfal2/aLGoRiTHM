def Z(n, x, y):
    global co
    if x==r and y==c:
        print(co)
        quit()
    if n == 1:
        co += 1
        return
    if not (x<=r<x+n and y<=c<y+n):
        co += n**2
        return
    m = n//2
    Z(m,x,y) # 1 사분면
    Z(m,x,y+m) # 2
    Z(m,x+m,y) # 3
    Z(m,x+m,y+m) # 4
    
    
N, r, c = map(int, input().split())
co = 0
Z(2**N,0,0)
# 배열의 크기를 먼저 넣어주고
# 반씩 줄여가면서 그곳에서 다시 1,2,3,4분면을 확인

w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

news = [[1,1],[1,-1],[-1,-1],[-1,1]]
T = 0
while T!=t:
    
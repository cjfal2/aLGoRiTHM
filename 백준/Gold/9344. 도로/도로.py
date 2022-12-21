import sys
input = sys.stdin.readline

def find_set(x):
    while x != arr[x]:
        x = arr[x]
    return x

for _ in range(int(input().strip())):
   N, M, p, q = map(int, input().strip().split())
   edge = []
   for _ in range(M):
      u, v, w = map(int, input().strip().split())
      edge.append((w, u, v))

   edge.sort()

   arr = [i for i in range(N+1)]

   N = N+1
   cnt = 0
   total = 0
   spann = []
   for w, u, v in edge:
      if find_set(u) != find_set(v):
         spann.append((u, v))
         cnt += 1
         total += w
         arr[find_set(v)] = find_set(u)
         if cnt == N:
               break
   if (p, q) in spann: 
      print('YES')
   else:
      print('NO')

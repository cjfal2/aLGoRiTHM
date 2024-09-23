a, b, c = map(int, input().split())
A, B, C = map(int, input().split())
answer = 0
if a < A:
    answer += A-a

if b < B:
    answer += B-b

if c < C:
    answer += C-c
print(answer)
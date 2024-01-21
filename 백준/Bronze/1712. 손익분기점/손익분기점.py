a, b, c = map(int, input().split())
if b >= c:
    print(-1)
    quit()

print(a//(c-b)+1)
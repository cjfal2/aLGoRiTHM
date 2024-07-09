input()
a = sum(list(map(int, input().split())))
print("Stay" if a == 0 else ("Left" if a < 0 else "Right"))
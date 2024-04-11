apple = 0
banana = 0
for i in range(3, 0, -1):
    c = int(input())
    apple += c*i
for i in range(3, 0, -1):
    c = int(input())
    banana += c*i
if apple > banana:
    print("A")
elif apple < banana:
    print("B")
else:
    print("T")
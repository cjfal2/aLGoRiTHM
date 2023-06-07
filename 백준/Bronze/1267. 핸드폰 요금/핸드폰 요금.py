N = input()
Y = 0
M = 0
for i in list(map(int, input().split())):
    Y += ((i//30+1)*10)
    M += ((i//60+1)*15)
  
if M < Y:
    print("M", M)
elif M > Y:
    print("Y", Y)
else:
    print("Y", "M", M)

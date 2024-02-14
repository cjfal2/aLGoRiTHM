string = input()
for length in range(1, 4):
    temp = string
    num = temp[0:length]
    answer = num
    while temp and temp[:len(num)] == num:
        temp = temp[len(num):]
        num = str(int(num)+1)
    if not temp:
        break
print(answer, int(num)-1)
 
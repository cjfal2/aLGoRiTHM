moonjang = input()
target = input()
i = 0
co = 0
while 1:
    word = ''
    for j in range(len(target)):
        if i+j >= len(moonjang):
            break
        word += moonjang[i+j]
    if word == target:
        i += len(target)
        co += 1
        if i >= len(moonjang) - len(target) + 1:
            break
    else:
        i += 1
        if i >= len(moonjang) - len(target) + 1:
            break
print(co)

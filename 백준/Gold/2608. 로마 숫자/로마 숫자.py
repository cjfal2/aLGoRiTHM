# 로마 숫자를 숫자로 변환하는 딕셔너리
change = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def number_to_roma(num):
    word = ''
    while num >= 1000:
        word += 'M'
        num -= 1000

    if num >= 900:
        word += 'CM'
        num -= 900
    if num >= 500:
        word += 'D'
        num -= 500
    if num >= 400:
        word += 'CD'
        num -= 400
    while num >= 100:
        word += 'C'
        num -= 100

    if num >= 90:
        word += 'XC'
        num -= 90
    if num >= 50:
        word += 'L'
        num -= 50
    if num >= 40:
        word += 'XL'
        num -= 40
    while num >= 10:
        word += 'X'
        num -= 10

    if num >= 9:
        word += 'IX'
        num -= 9
    if num >= 5:
        word += 'V'
        num -= 5
    if num >= 4:
        word += 'IV'
        num -= 4
    while num > 0:
        word += 'I'
        num -= 1

    return word


def roma_to_number(roma_number):
    result = 0
    prev = 0
    for w in roma_number:
        value = change[w]
        if value > prev:
            result += value - 2 * prev
        else:
            result += value
        prev = value
    return result


a = input()
b = input()
number = roma_to_number(a) + roma_to_number(b)
print(number)
print(number_to_roma(number))

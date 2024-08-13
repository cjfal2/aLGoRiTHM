def check_order():
    general_total = 0
    special_total = 0
    service_ordered = False

    for _, order in orders:
        if order in general:
            general_total += general[order]
        elif order in special:
            if general_total >= 20000:
                special_total += special[order]
            else:
                return "No"
        elif order in service:
            if service_ordered:
                return "No"
            if general_total + special_total >= 50000:
                service_ordered = True
            else:
                return "No"

    return "Okay"


A, B, C = map(int, input().split())

general = {}
special = {}
service = set()

for _ in range(A):
    name, price = input().split()
    general[name] = int(price)

for _ in range(B):
    name, price = input().split()
    special[name] = int(price)

for _ in range(C):
    name = input().strip()
    service.add(name)

N = int(input())
orders = []
for _ in range(N):
    food = input()
    if food in general:
        orders.append((1, food))
    elif food in special:
        orders.append((2, food))
    elif food in service:
        orders.append((3, food))
orders.sort()
# 주문 검증
print(check_order())

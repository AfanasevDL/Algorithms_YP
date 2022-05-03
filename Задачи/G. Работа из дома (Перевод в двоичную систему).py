x = int(input())

number = 0
i = 0
while x > 0:
    a = x % 2
    number += a*10**i
    i += 1
    x = x // 2
print(number)

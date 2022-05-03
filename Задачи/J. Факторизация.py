num = int(input())

factors = []
d = 2
m = num
while d * d <= num:
    if num % d == 0:
        factors.append(d)
        num //= d
    else:
        d += 1
factors.append(num)
print(*factors)
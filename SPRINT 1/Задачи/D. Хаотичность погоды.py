n = int(input())
array = list(map(int, input().split()))

days = 0
if n == 1:
    days += 1

if n != 1:
    for i in range(0, n):
        if i == 0:
            if array[0] > array[1]:
                days += 1
        elif i == n - 1:
            if array[n - 1] > array[n - 2]:
                days += 1
        else:
            if array[i] > array[i + 1] and array[i] > array[i - 1]:
                days += 1

print(days)

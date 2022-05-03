array = input().split()
a = int(array[0])
b = int(array[1])
c = int(array[2])

if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    print("WIN")
elif a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
    print("WIN")
else:
    print("FAIL")
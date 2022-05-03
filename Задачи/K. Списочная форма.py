n = int(input())
x_list = list(map(int, input().split()))
k = int(input())

x = "".join(str(i) for i in x_list)
xk = str(int(x) + k)
xk_list = []
for i in xk:
    xk_list.append(i)
print(*xk_list)
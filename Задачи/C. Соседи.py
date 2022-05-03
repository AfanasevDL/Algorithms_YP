n = int(input())
m = int(input())

matrix = []

for k in range(0, n):
    number = list(map(int, input().split()))
    matrix.append(number)

x = int(input())
y = int(input())


def get_adjacent(n, m, x, y):
    adj_list = []
    if x > 0:
        adj_list.append((matrix[x - 1][y]))
    if x + 1 < n:
        adj_list.append((matrix[x + 1][y]))
    if y > 0:
        adj_list.append((matrix[x][y - 1]))
    if y + 1 < m:
        adj_list.append((matrix[x][y + 1]))
    return sorted(adj_list)


print(*get_adjacent(n, m, x, y))

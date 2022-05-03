s = input()
list_s = list(s)
t = input()
list_t = list(t)
for i in list_s:
    list_t.remove(i)

print(*list_t)


n = int(input())
text = input().split()
text.sort(key=len)
text.reverse()
for i in range(0, len(text)):
    first_longest_word = text[i]
    if len(text) == 1:
        break
    elif len(text[0]) == len(text[len(text)-1]):
        first_longest_word = text[len(text)-1]
    elif len(text[i]) <= len(text[i+1]):
        first_longest_word = text[i+1]
    else:
        break

print(first_longest_word)
print(len(first_longest_word))

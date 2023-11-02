word = input("Введіть слово: ")
ascii_sum = 0

for char in word:
    ascii_sum += ord(char)

print("Сума ASCII-кодів символів слова:", ascii_sum)
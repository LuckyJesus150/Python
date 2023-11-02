sentence = input("Введіть речення: ") 
words = sentence.split()
words_with_three_e = []

for word in words:
    if word.count("е") == 3:
        words_with_three_e.append(word)

if words_with_three_e:
    print("Слова з трьома 'е':", words_with_three_e)
else:
    print("У реченні немає слів з трьома 'е'.")
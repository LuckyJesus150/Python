N = int(input("Введіть розмір масиву: "))
array = []

for i in range(N):
    num = int(input(f"Введіть {i + 1}-й елемент масиву: "))
    array.append(num)

sum_of_positive_multiples_of_three = 0

for num in array:
    if num > 0 and num % 3 == 0:
        sum_of_positive_multiples_of_three += num

print("Сума додатніх елементів, кратних трьом:", sum_of_positive_multiples_of_three)

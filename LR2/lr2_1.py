import math
a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
z = math.sin(a - b) * math.sin(a + b)
print("Результат: z =", z)

from lr2_2 import sport
m = float(input("Введіть початкову норму (M): "))
k = float(input("Введіть процент збільшення норми в процентах (10% = 10): "))
sport(m,k)
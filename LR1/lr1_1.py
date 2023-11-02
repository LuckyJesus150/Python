a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))

if a <= 0 or b <= 0:
    print("a та b повинні бути додатніми числами.")
else:
    if a > b: x = a * b + 21
    elif a == b: x = -5
    else: x = 3 * a / b + 1

    print("Значення X:", x)
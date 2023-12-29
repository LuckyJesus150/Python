import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def Y(x):
    return 5 * np.sin(10 * x) * np.sin(3 * x)

# Генерація значень x в діапазоні від 0 до 4
x_values = np.linspace(0, 4, 1000)

# Генерація значень y для відповідних x
y_values = Y(x_values)

# Побудова графіка
plt.plot(x_values, y_values, linestyle='-', color='b', linewidth=2, label='Y(x) = 5*sin(10*x)*sin(3*x)')

# Додавання осей
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Позначення осей
plt.xlabel('X')
plt.ylabel('Y')

# Додавання заголовка графіка
plt.title('Графік функції Y(x)')

# Додавання легенди
plt.legend()

# Відображення графіка
plt.show()

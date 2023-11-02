def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)
    return fib_series

start_index = 5  
end_index = 25 

fib_series = fibonacci(end_index + 1)

for i in range(start_index, end_index + 1):
    print(f"Член {i}: {fib_series[i]}")

count = len(fib_series)
print(f"Кількість членів у ряді: {count-6}")
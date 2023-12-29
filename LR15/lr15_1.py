import pandas as pd

def process_data():
    # Створення словника
    data = {'Name': ['John', 'Alice', 'Bob', 'Alice', 'John'],
            'Age': [25, 30, 35, 30, 25],
            'Salary': [50000, 60000, 70000, 60000, 50000]}

    # Перетворення словника на датафрейм
    df = pd.DataFrame(data)

    # Виведення початкового датафрейму
    print("Initial DataFrame:")
    print(df)

    # Доповнення датафрейму
    new_data = {'Name': ['Charlie', 'David'],
                'Age': [40, 45],
                'Salary': [80000, 90000]}

    # Використання pd.concat для об'єднання двох датафреймів
    df_initial = pd.concat([df, pd.DataFrame(new_data)], ignore_index=True)

    # Виведення датафрейму після доповнення
    print("\nDataFrame after appending new data:")
    print(df_initial)

    # Виклик функції видалення
    value_to_delete = str(input('Enter value to delete: '))
    df_after_delete = delete(df_initial, value_to_delete)

    # Виведення датафрейму після видалення
    print("\nDataFrame after deleting values:")
    print(df_after_delete)

    # Агрегація та групування даних
    aggregated_data = df_after_delete.groupby('Name').agg({'Age': 'mean', 'Salary': 'sum'}).reset_index()

    # Виведення результатів агрегації та групування
    print("\nAggregated and Grouped Data:")
    print(aggregated_data)

def delete(df, value_to_delete):
    # Видалення значень з датафрейму
    df = df[df['Name'] != value_to_delete]
    return df

# Виклик основної функції
process_data()

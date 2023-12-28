import os
import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Помилка: {e}")
        return None

def display_csv_content(data):
    if data:
        for row in data:
            print(', '.join(row))
    print()

def search_and_save_countries(data, search_countries, output_file):
    try:
        with open(output_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            header_written = False  # To write header only once if the file is empty
            for row in data:
                for country in search_countries:
                    if country.lower() in row[2].lower():  # Check 'Country Name' column
                        if not header_written:
                            writer.writerow(row)  # Write the header
                            header_written = True
                        writer.writerow(row)
                        break
                else:
                    continue
    except Exception as e:
        print(f"Помилка при збереженні файлу: {e}")





if __name__ == "__main__":
    # Отримання абсолютного шляху до поточної робочої директорії
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Повний шлях до вхідного та вихідного файлів
    input_file_path = os.path.join(current_directory, "Lab11.csv")
    output_file_path = os.path.join(current_directory, "SearchResults.csv")

    # Читання вмісту CSV файлу
    csv_data = read_csv_file(input_file_path)

    # Виведення вмісту CSV файлу на екран
    display_csv_content(csv_data)

    if csv_data:
        # Введення користувачем назв країн для пошуку
        search_input = input("Введіть назви країн через кому: ")
        search_countries = [country.strip() for country in search_input.split(',')]

        # Пошук та збереження результатів у новий CSV файл
        search_and_save_countries(csv_data, search_countries, output_file_path)

        print(f"Результати пошуку збережено у файлі '{output_file_path}'.")

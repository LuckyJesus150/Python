def display_dictionary(data_dict):
    print("Значення словника:")
    for key, value in data_dict.items():
        print(f"{key}: {value}")

def add_entry(data_dict):
    surname = input("Введіть прізвище: ")
    name = input("Введіть ім'я: ")
    address = input("Введіть адресу: ")
    school = input("Введіть номер школи: ")
    grade = input("Введіть клас: ")

    key = f"{surname}, {name}"
    data_dict[key] = (surname, name, address, school, grade)
    print(f"Запис {key} додано до словника.")

def delete_entry(data_dict):
    key_to_delete = input("Введіть ключ (прізвище, ім'я) для видалення запису: ")
    if key_to_delete in data_dict:
        del data_dict[key_to_delete]
        print(f"Запис {key_to_delete} видалено зі словника.")
    else:
        print(f"Запис з ключем {key_to_delete} не знайдено.")

def display_sorted_keys(data_dict):
    sorted_keys = sorted(data_dict.keys())
    print("Вміст словника за відсортованими ключами:")
    for key in sorted_keys:
        print(f"{key}: {data_dict[key]}")

def get_senior_students_by_school(data_dict, school_number):
    senior_students_list = []
    for key, value in data_dict.items():
        _, _, address, school, grade = value
        if school == school_number and int(grade) >= 10:
            senior_students_list.append((key, value))
    return senior_students_list

def main():
    n = 10  # кількість учнів
    students_data = {
    "Ivanov, Ivan": ("Ivanov", "Ivan", "Sumy", "11", "11"),
    "Petrov, Petro": ("Petrov", "Petro", "Sumy", "10", "11"),
    "Sidorov, Sidr": ("Sidorov", "Sidr", "Sumy", "10", "10"),
    "Fedorov, Fedor": ("Fedorov", "Fedor", "Sumy", "19", "11"),
    "Egorov, Egor": ("Egorov", "Egor", "Sumy", "11", "10"),
    "Olga, Olya": ("Olga", "Olya", "Sumy", "10", "10"),
    }

    while True:
        print("\nМеню:")
        print("1. Вивести на екран всі значення словника")
        print("2. Додати новий запис до словника")
        print("3. Видалити запис зі словника")
        print("4. Перегляд вмісту словника за відсортованими ключами")
        print("5. Знайти старших учнів для вказаної школи (10-11 класи)")
        print("6. Вийти з програми")

        choice = input("Виберіть опцію (1-6): ")

        if choice == '1':
            display_dictionary(students_data)
        elif choice == '2':
            add_entry(students_data)
        elif choice == '3':
            delete_entry(students_data)
        elif choice == '4':
            display_sorted_keys(students_data)
        elif choice == '5':
            school_number = input("Введіть номер школи для пошуку старших учнів (10-11 класи): ")
            senior_students = get_senior_students_by_school(students_data, school_number)
            if senior_students:
                print(f"Старші учні школи {school_number} (10-11 класи):")
                for student in senior_students:
                    print(f"{student[0]}: {student[1]}")
            else:
                print(f"Немає старших учнів для школи {school_number}.")
        elif choice == '6':
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()

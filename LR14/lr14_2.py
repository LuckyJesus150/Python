import json
import os
import matplotlib.pyplot as plt

def add_employee(data):
    print("Add: ")
    Name = input("Name:")
    Surname = input("Surname:")
    Patronymic = input("Patronymic:")
    Adress = input("Adress:")
    School = input("School:")
    Day_in = input("Day_in:")
    data.append({"Name": Name, "Surname": Surname, "Patronymic": Patronymic, "Adress": Adress, "School": School, "Day_in": Day_in})
    return data

def calculate_percentage(students):
    total_students = len(students)
    days_in_subota = sum(1 for student in students if student['Day_in'] == 'Subota')
    days_in_other = total_students - days_in_subota
    return days_in_subota / total_students * 100, days_in_other / total_students * 100

def plot_pie_chart(labels, sizes):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightskyblue'])
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Distribution of Days in Subota vs Other Days')
    plt.show()

def main():
    filename = "data.json"

    # Check if the file exists
    if os.path.exists(filename):
        with open(filename, "rt") as file:
            students = json.loads(file.read())
    else:
        students = []

    while True:
        print("Select an option:\n 1 - Add data\n 2 - View data\n 3 - Find students who came on Subota\n 4 - Plot Pie Chart\n 5 - Exit")
        x = input("Choose an option:\n")
        x = int(x)

        if x == 1:
            students = add_employee(students)
            jsonData = json.dumps(students)
            with open(filename, "wt") as file:
                file.write(jsonData)

        elif x == 2:
            print(*students, sep='\n')

        elif x == 3:
            result = [
                {key: value for key, value in student.items() if key in ['Surname', 'Name', 'Patronymic', 'Adress', 'School', 'Day_in']}
                for student in students if student['Day_in'] == 'Subota'
            ]
            print(*result, sep='\n')

        elif x == 4:
            labels = ['Subota', 'Other Days']
            sizes = calculate_percentage(students)
            plot_pie_chart(labels, sizes)

        elif x == 5:
            break

if __name__ == "__main__":
    main()

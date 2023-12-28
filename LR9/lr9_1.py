def create_file(file_name, content):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"File {file_name} was created!")
    except Exception as e:
        print(f"File {file_name} wasn't created. Error: {e}")

def process_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file_in, open(output_file, 'w', encoding='utf-8') as file_out:
            for line in file_in:
                line = line.strip()
                if len(line) < 20:
                    line = line.ljust(20)
                else:
                    line = line[:20]
                file_out.write(line + '\n')
        print(f"Processing complete. Check {output_file} for results.")
    except Exception as e:
        print(f"Error processing files. Error: {e}")

def print_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            print(f"Content of {file_name}:")
            for line in file:
                print(line.strip())
    except Exception as e:
        print(f"Error reading {file_name}. Error: {e}")

# Завдання (а)
file1_name = "TF9_1.txt"
file1_content = "Я студент\n студент групи ІТ-23-3\n Павлов\n спочатку було яйце чи курка, якщо яйце, то чому\n"
create_file(file1_name, file1_content)

# Завдання (б)
file2_name = "TF9_2.txt"
process_file(file1_name, file2_name)

# Завдання (в)
print_file(file2_name)
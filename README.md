import os 
while True:
    file_path = input("Введіть шлях до файлу: ")
    if not os.path.isfile(file_path):
        print("Файл не найдено")
        continue
    with open(file_path, 'r') as f:
        line_count = 0
        empty_line_count = 0
        z_line_count = 0
        z_count = 0
        and_line_count = 0
        for line in f:
            line_count += 1
            line = line.strip()
            if len(line) == 0:
                empty_line_count += 1
            if "z" in line:
                z_line_count += 1
            z_count += line.count("z")
            if "and" in line:
                and_line_count += 1
        print("Кількість рядків: ", line_count) 
        print("Кількість порожніх рядків: ", empty_line_count)
        print("Кількість  рядків з літерою 'z': ", z_line_count)
        print("Кількість літер 'z' у файлі: ", z_count)
        print("Кількість рядків з групою символів 'and': ", and_line_count)   
    choice = input("Хочете проаналізувати ще один файл? (y/n): ")
    if choice.lower() != "y":
        break

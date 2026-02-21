try:
    with open("students.txt", "r", encoding="utf-8") as f:
        pass
except FileNotFoundError:
    print("Создаю файл students.txt с тестовыми данными...")
    with open("students.txt", "w", encoding="utf-8") as f:
        f.write("Иванов Иван:5,4,3,5\n")
        f.write("Петров Петр:4,3,4,4\n")
        f.write("Сидорова Мария:5,5,5,5\n")
        f.write("Козлов Дмитрий:3,4,3,4\n")
        f.write("Смирнова Анна:5,5,4,5\n")
    print("Файл создан.")

students = {}
try:
    with open("students.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and ":" in line:
                name, grades_str = line.split(":", 1)
                grades = []
                for grade in grades_str.split(","):
                    grade = grade.strip()
                    if grade and grade.isdigit():
                        grades.append(int(grade))
                if grades:
                    students[name.strip()] = grades
except Exception as e:
    print(f"Ошибка при чтении файла: {e}")
    exit()

if not students:
    print("Файл students.txt пуст или содержит некорректные данные.")
    print("Добавьте данные в формате: Имя Фамилия:5,4,3,5")
    exit()

averages = {}
print("Список студентов и их средние баллы:")
for name, grades in students.items():
    avg = sum(grades) / len(grades)
    averages[name] = avg
    print(f"- {name}: оценки {grades}, средний балл {avg:.2f}")

with open("result.txt", "w", encoding="utf-8") as f:
    print("\nСтуденты со средним баллом > 4.0:")
    found = False
    for name, avg in averages.items():
        if avg > 4.0:
            f.write(f"{name}: {avg:.2f}\n")
            print(f"- {name}: {avg:.2f}")
            found = True

    if not found:
        f.write("Нет студентов со средним баллом > 4.0\n")
        print("Нет студентов со средним баллом > 4.0")

if averages:
    top_student = max(averages, key=averages.get)
    top_avg = averages[top_student]

    print(f"Студент с наивысшим средним баллом:")
    print(f"{top_student} - {top_avg:.2f}")

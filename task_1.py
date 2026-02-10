print("Введите 5 строк текста для записи в файл text.txt:")
lines = []
for i in range(5):
    line = input(f"Строка {i + 1}: ")
    lines.append(line)

with open("text.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

print("Файл text.txt создан и заполнен текстом.")

try:
    with open("text.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("Файл пуст.")
    else:
        lines = [line.strip() for line in lines]

        line_count = len(lines)

        word_count = 0
        for line in lines:
            words = line.split()
            word_count += len(words)

        longest_line = ""
        for line in lines:
            if len(line) > len(longest_line):
                longest_line = line

        print(f"Количество строк в файле: {line_count}")
        print(f"Количество слов в файле: {word_count}")
        print(f"Самая длинная строка: '{longest_line}'")

except FileNotFoundError:
    print("Ошибка: Файл text.txt не найден.")
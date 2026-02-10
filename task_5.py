import json
import os

JSON_FILE = "library.json"

if not os.path.exists(JSON_FILE):
    print(f"Создаю файл {JSON_FILE} с тестовыми данными...")
    initial_data = [
        {
            "id": 1,
            "title": "Мастер и Маргарита",
            "author": "Булгаков",
            "year": 1967,
            "available": True
        },
        {
            "id": 2,
            "title": "Преступление и наказание",
            "author": "Достоевский",
            "year": 1866,
            "available": False
        }
    ]
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(initial_data, f, ensure_ascii=False, indent=4)
    print("Файл создан.")

def load_books():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_books(books):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


print("СИСТЕМА УЧЕТА КНИГ В БИБЛИОТЕКЕ")

while True:
    print("\nМеню:")
    print("1. Просмотр всех книг")
    print("2. Поиск по автору/названию")
    print("3. Добавление новой книги")
    print("4. Изменение статуса доступности")
    print("5. Удаление книги по ID")
    print("6. Экспорт доступных книг в файл")
    print("7. Выход")

    choice = input("Выберите действие (1-7): ")

    if choice == "1":
        books = load_books()
        if not books:
            print("Библиотека пуста.")
        else:
            print(f"\nВсего книг в библиотеке: {len(books)}")
            for book in books:
                status = "ДОСТУПНА" if book["available"] else "ВЫДАНА"
                print(f"ID: {book['id']}")
                print(f"  Название: {book['title']}")
                print(f"  Автор: {book['author']}")
                print(f"  Год: {book['year']}")
                print(f"  Статус: {status}")

    elif choice == "2":
        search_term = input("\nВведите автора или название для поиска: ").lower()
        books = load_books()
        found_books = []

        for book in books:
            if (search_term in book["title"].lower() or
                    search_term in book["author"].lower()):
                found_books.append(book)

        if found_books:
            print(f"\nНайдено книг: {len(found_books)}")
            for book in found_books:
                status = "ДОСТУПНА" if book["available"] else "ВЫДАНА"
                print(f"ID: {book['id']} | {book['title']} | {book['author']} | {book['year']} | {status}")
        else:
            print("Книги не найдены.")

    elif choice == "3":
        books = load_books()

        print("\nДобавление новой книги:")
        title = input("Введите название книги: ")
        author = input("Введите автора: ")

        while True:
            try:
                year = int(input("Введите год издания: "))
                if year > 0:
                    break
                else:
                    print("Год должен быть положительным числом.")
            except:
                print("Введите корректный год!")

        if books:
            new_id = max(book["id"] for book in books) + 1
        else:
            new_id = 1

        new_book = {
            "id": new_id,
            "title": title,
            "author": author,
            "year": year,
            "available": True
        }

        books.append(new_book)
        save_books(books)
        print(f"\nКнига '{title}' успешно добавлена с ID: {new_id}")

    elif choice == "4":
        books = load_books()

        try:
            book_id = int(input("\nВведите ID книги для изменения статуса: "))
            found = False

            for book in books:
                if book["id"] == book_id:
                    found = True
                    old_status = "доступна" if book["available"] else "выдана"
                    book["available"] = not book["available"]
                    new_status = "доступна" if book["available"] else "выдана"

                    save_books(books)
                    print(f"Статус книги '{book['title']}' изменен: {old_status} → {new_status}")
                    break

            if not found:
                print(f"Книга с ID {book_id} не найдена.")

        except ValueError:
            print("Введите корректный ID (число)!")

    elif choice == "5":
        books = load_books()

        try:
            book_id = int(input("\nВведите ID книги для удаления: "))
            original_count = len(books)
            books = [book for book in books if book["id"] != book_id]

            if len(books) < original_count:
                save_books(books)
                print(f"Книга с ID {book_id} удалена.")
            else:
                print(f"Книга с ID {book_id} не найдена.")

        except ValueError:
            print("Введите корректный ID (число)!")

    elif choice == "6":
        books = load_books()
        available_books = [book for book in books if book["available"]]

        if not available_books:
            print("Нет доступных книг для экспорта.")
        else:
            with open("available_books.txt", "w", encoding="utf-8") as f:
                f.write("СПИСОК ДОСТУПНЫХ КНИГ\n")
                f.write(f"Всего доступно: {len(available_books)} книг\n")

                for book in available_books:
                    f.write(f"ID: {book['id']}\n")
                    f.write(f"Название: {book['title']}\n")
                    f.write(f"Автор: {book['author']}\n")
                    f.write(f"Год издания: {book['year']}\n")

            print(f"Экспортировано {len(available_books)} доступных книг в файл 'available_books.txt'")

    elif choice == "7":
        print("Выход из программы. Все изменения сохранены.")
        break

    else:
        print("Неверный выбор. Попробуйте снова.")
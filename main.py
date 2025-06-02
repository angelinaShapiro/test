# Получаем количество дел от пользователя
n = int(input("Сколько дел у вас запланировано на сегодня? "))

# Создаем пустой список для хранения дел
todo = []

# Запрашиваем дела у пользователя и добавляем их в список
for i in range(n):
    task = input(f"Введите дело номер {i + 1}: ")
    todo.append(task)

# Выводим список дел на экран
print("\nВаши дела на сегодня:")
for i, task in enumerate(todo):
    print(f"{i + 1}. {task}")

# Редактирование дела
if todo:  # Проверяем, что список не пустой
    try:
        edit_index = int(input("\nВведите номер дела, которое хотите отредактировать: ")) - 1  # Вычитаем 1, так как нумерация с 1, а индексы с 0
        if 0 <= edit_index < len(todo):  # Проверяем корректность введенного номера
            new_task = input("Введите новое описание дела: ")
            todo[edit_index] = new_task
            print("\nСписок дел после редактирования:")
            for i, task in enumerate(todo):
                print(f"{i + 1}. {task}")
        else:
            print("Неверный номер дела.")
    except ValueError:
        print("Ошибка: Введите корректный номер дела.")

# Удаление дела
if todo:  # Проверяем, что список не пустой
    try:
        delete_index = int(input("\nВведите номер дела, которое хотите удалить: ")) - 1  # Вычитаем 1, так как нумерация с 1, а индексы с 0
        if 0 <= delete_index < len(todo):  # Проверяем корректность введенного номера
            deleted_task = todo.pop(delete_index)
            print(f"\nДело '{deleted_task}' удалено.")
            print("\nСписок дел после удаления:")
            for i, task in enumerate(todo):
                print(f"{i + 1}. {task}")
        else:
            print("Неверный номер дела.")
    except ValueError:
        print("Ошибка: Введите корректный номер дела.")

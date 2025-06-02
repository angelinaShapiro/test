# Инициализация ежедневника (двумерный массив)
todo_list = [
    ['', '', ''],  # Понедельник (утро, день, вечер)
    ['', '', ''],  # Вторник
    ['', '', ''],  # Среда
    ['', '', ''],  # Четверг
    ['', '', ''],  # Пятница
    ['', '', ''],  # Суббота
    ['', '', '']   # Воскресенье
]

# Дни недели для удобства пользователя
days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
time_of_day = ["Утро", "День", "Вечер"]

# Заполнение ежедневника делами от пользователя
print("Заполните свой ежедневник:")
for day_index, day in enumerate(days_of_week):
    print(f"\n{day}:")
    for time_index, time in enumerate(time_of_day):
        task = input(f"  Введите дело на {time}: ")
        todo_list[day_index][time_index] = task

# Удаление записи
try:
    delete_day_index = int(input("\nВведите номер дня недели (1-7), из которого хотите удалить дело: ")) - 1
    delete_time_index = int(input("Введите номер времени суток (1-3), из которого хотите удалить дело (утро, день, вечер): ")) - 1
    if 0 <= delete_day_index < 7 and 0 <= delete_time_index < 3:
        deleted_task = todo_list[delete_day_index][delete_time_index]
        todo_list[delete_day_index][delete_time_index] = ""  # Удаление: просто заменяем на пустую строку
        print(f"Дело '{deleted_task}' удалено.")
    else:
        print("Неверный ввод для удаления.")
except ValueError:
    print("Ошибка: Введите корректные номера дня и времени суток.")

# Добавление записи (редактирование существующей или добавление новой)
try:
    add_day_index = int(input("\nВведите номер дня недели (1-7), в который хотите добавить/отредактировать дело: ")) - 1
    add_time_index = int(input("Введите номер времени суток (1-3), в которое хотите добавить/отредактировать дело (утро, день, вечер): ")) - 1
    if 0 <= add_day_index < 7 and 0 <= add_time_index < 3:
        new_task = input("Введите новое дело: ")
        todo_list[add_day_index][add_time_index] = new_task
    else:
        print("Неверный ввод для добавления/редактирования.")
except ValueError:
    print("Ошибка: Введите корректные номера дня и времени суток.")

# Вывод ежедневника
print("\nВаш ежедневник:")
for day_index, day in enumerate(days_of_week):
    print(f"\n{day}:")
    for time_index, time in enumerate(time_of_day):
        print(f"  {time}: {todo_list[day_index][time_index]}")
import random

def golf():
    """
    Текстовая игра в гольф.
    """

    distance_to_hole = random.randint(150, 250)  # Случайное расстояние до лунки
    print("Добро пожаловать в текстовый гольф!")
    print(f"До лунки {distance_to_hole} метров.")
    shots = 0

    while distance_to_hole > 0:
        try:
            power = int(input("Введите силу удара (1-100): "))
            if not 1 <= power <= 100:
                print("Сила удара должна быть от 1 до 100.")
                continue
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue

        shots += 1
        # Шум добавляет случайность
        shot_distance = int(power + random.randint(-10, 10))
        distance_to_hole -= shot_distance

        print(f"Удар на {shot_distance} метров.")

        if distance_to_hole <= 0:
            print("Вы в лунке!")
            print(f"Партия завершена за {shots} ударов.")
        else:
            print(f"Осталось {distance_to_hole} метров.")

if __name__ == "__main__":
    golf()
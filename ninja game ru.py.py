import random
import time

def ninja_game():
    """
    Простая текстовая игра про ниндзя.
    """

    player_health = 100
    enemy_health = 80
    player_name = input("Введите имя своего ниндзя: ")
    enemy_name = "Злой Самурай"

    print(f"\nДобро пожаловать, {player_name}, в мир ниндзя!")
    print(f"Твоя цель: победить {enemy_name}!")

    while player_health > 0 and enemy_health > 0:
        print(f"\n--- {player_name} ({player_health} HP) vs. {enemy_name} ({enemy_health} HP) ---")
        print("Выберите действие:")
        print("1. Атаковать мечом (урон 10-20)")
        print("2. Бросить сюрикен (урон 5-15)")
        print("3. Защищаться (уменьшает урон врага на 5)")
        print("4. Использовать дымовую шашку (пропустить ход врага)")

        try:
            action = int(input("Ваш выбор: "))
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 4.")
            continue

        if action not in [1, 2, 3, 4]:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 4.")
            continue

        # Ход игрока
        if action == 1:
            damage = random.randint(10, 20)
            print(f"Вы атакуете мечом и наносите {damage} урона!")
            enemy_health -= damage
        elif action == 2:
            damage = random.randint(5, 15)
            print(f"Вы бросаете сюрикен и наносите {damage} урона!")
            enemy_health -= damage
        elif action == 3:
            print("Вы защищаетесь!")
            defense = 5
        elif action == 4:
            print("Вы используете дымовую шашку!")
            enemy_turn = False
            time.sleep(1.5) # небольшая задержка для реалистичности
        else:
            continue # Никогда не должно произойти, но на всякий случай

        if enemy_health <= 0:
            print(f"\nВы победили {enemy_name}!")
            break

        # Ход врага (пропуск хода, если использована дымовая шашка)
        if action != 4:
            enemy_action = random.randint(1, 3) # Враг не использует дымовую шашку
            if enemy_action == 1:
                damage = random.randint(8, 18)
                if action == 3:
                    damage -= defense # Уменьшаем урон, если игрок защищался
                    if damage < 0:
                        damage = 0
                print(f"{enemy_name} атакует мечом и наносит {damage} урона!")
                player_health -= damage
            elif enemy_action == 2:
                damage = random.randint(3, 12)
                if action == 3:
                    damage -= defense
                    if damage < 0:
                        damage = 0
                print(f"{enemy_name} бросает сюрикен и наносит {damage} урона!")
                player_health -= damage
            elif enemy_action == 3:
                print(f"{enemy_name} защищается!")
                # Враг может защищаться, но это пока не влияет на игру
        else:
             print(f"{enemy_name} дезориентирован дымом!")

        if player_health <= 0:
            print(f"\nВы проиграли {enemy_name}!")
            break

    print("\nИгра окончена.")

if __name__ == "__main__":
    ninja_game()
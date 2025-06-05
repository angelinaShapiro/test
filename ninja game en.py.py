import random
import time

def ninja_game():
    """
    A simple text-based ninja game.
    """

    player_health = 100
    enemy_health = 80
    player_name = input("Enter your ninja's name: ")
    enemy_name = "Evil Samurai"

    print(f"\nWelcome, {player_name}, to the world of ninjas!")
    print(f"Your goal: defeat the {enemy_name}!")

    while player_health > 0 and enemy_health > 0:
        print(f"\n--- {player_name} ({player_health} HP) vs. {enemy_name} ({enemy_health} HP) ---")
        print("Choose your action:")
        print("1. Attack with sword (damage 10-20)")
        print("2. Throw shuriken (damage 5-15)")
        print("3. Defend (reduces enemy damage by 5)")
        print("4. Use smoke bomb (skips enemy's turn)")

        try:
            action = int(input("Your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if action not in [1, 2, 3, 4]:
            print("Invalid choice. Please select an action from 1 to 4.")
            continue

        # Player's turn
        if action == 1:
            damage = random.randint(10, 20)
            print(f"You attack with your sword and deal {damage} damage!")
            enemy_health -= damage
        elif action == 2:
            damage = random.randint(5, 15)
            print(f"You throw a shuriken and deal {damage} damage!")
            enemy_health -= damage
        elif action == 3:
            print("You defend!")
            defense = 5
        elif action == 4:
            print("You use a smoke bomb!")
            time.sleep(1.5) # Add a short delay for realism
        else:
            continue # Should never happen, but just in case

        if enemy_health <= 0:
            print(f"\nYou have defeated the {enemy_name}!")
            break

        # Enemy's turn (skip turn if smoke bomb was used)
        if action != 4:
            enemy_action = random.randint(1, 3) # Enemy does not use smoke bomb
            if enemy_action == 1:
                damage = random.randint(8, 18)
                if action == 3:
                    damage -= defense # Reduce damage if the player defended
                    if damage < 0:
                        damage = 0
                print(f"The {enemy_name} attacks with his sword and deals {damage} damage!")
                player_health -= damage
            elif enemy_action == 2:
                damage = random.randint(3, 12)
                if action == 3:
                    damage -= defense
                    if damage < 0:
                        damage = 0
                print(f"The {enemy_name} throws a shuriken and deals {damage} damage!")
                player_health -= damage
            elif enemy_action == 3:
                print(f"The {enemy_name} defends!")
        else:
            print(f"The {enemy_name} is disoriented by the smoke!")

        if player_health <= 0:
            print(f"\nYou have been defeated by the {enemy_name}!")
            break

    print("\nGame Over.")

if __name__ == "__main__":
    ninja_game()
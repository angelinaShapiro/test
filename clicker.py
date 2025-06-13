import time
import random

def endless_clicker():
    """
    The "Endless Clicker with a Story" game.
    """
    points = 0
    click_power = 1
    level = 1
    event_chance = 0.1  # Chance of an event happening on each click

    def click():
        nonlocal points
        nonlocal event_chance  # We're changing the event chance

        points += click_power
        print(f"You clicked! You have {points} points.")

        if random.random() < event_chance:  # Event check
            trigger_event()

    def upgrade_click_power():
        nonlocal click_power
        nonlocal points

        upgrade_cost = click_power * 10  # Upgrade cost increases

        if points >= upgrade_cost:
            points -= upgrade_cost
            click_power += 1
            print(f"You upgraded your click power! It is now {click_power}.")
            print(f"You have {points} points remaining.")
        else:
            print("Not enough points to upgrade!")

    def trigger_event():
        nonlocal points
        nonlocal level
        nonlocal event_chance  # Making this nonlocal again.

        event_type = random.choice(["bonus", "penalty", "minigame", "story"])

        if event_type == "bonus":
            bonus_amount = random.randint(10, 50) * level
            points += bonus_amount
            print(f"You got lucky! You received a bonus of {bonus_amount} points!")
            event_chance = max(0.01, event_chance - 0.02) # Reducing event chance after bonus

        elif event_type == "penalty":
            penalty_amount = random.randint(5, 25) * level
            points = max(0, points - penalty_amount)  # Prevent negative points
            print(f"Bad luck! You lost {penalty_amount} points!")
            event_chance += 0.05  # Increasing event chance after penalty (compensation)

        elif event_type == "minigame":
            minigame_result = play_minigame()
            points += minigame_result
            print(f"You played the minigame and earned {minigame_result} points!")

        elif event_type == "story":
            tell_story()
            level += 1
            print(f"You reached level {level}!")
            event_chance = 0.1 # Resetting event chance to normal

        else:
            print("Error in event selection.")

    def play_minigame():
        """
        Placeholder for a minigame (number guessing). Can be expanded.
        """
        secret_number = random.randint(1, 10)
        attempts = 3
        print("Minigame: Guess the number from 1 to 10 in 3 tries!")

        while attempts > 0:
            try:
                guess = int(input(f"Attempt {4 - attempts}: "))
                if guess == secret_number:
                    print("You guessed it!")
                    return 50 * level  # Reward for winning
                elif guess < secret_number:
                    print("The number is higher.")
                else:
                    print("The number is lower.")
                attempts -= 1
            except ValueError:
                print("Please enter an integer.")

        print(f"You didn't guess the number. The number was {secret_number}.")
        return 0

    def tell_story():
        """
        Tells a part of an absurd story. Can be expanded.
        """
        stories = [
            "You clicked so hard, you broke your finger. Luckily, an extra clicker grew out of the broken finger!",
            "While clicking, you discovered a portal to another world where clicking is the currency.",
            "Your clicks have attracted the attention of aliens who want to learn this art.",
            "Clicking has caused a local economic boom. People are willing to pay you for every click!",
            "You accidentally discovered that every click brings you closer to solving the mystery of the universe. But at what cost?",
            "Suddenly, all the cats in the world start clicking with you, accelerating the process a hundredfold!", # Fun theme
            "Click! You found the philosopher's stone! But what is it doing in a clicker?", # Strange twist
            "During a click, a voice appears in your head and offers you a deal. Click a million more times and all your wishes will come true. But at what price?"
        ]
        print(random.choice(stories))


    # Main game loop:
    while True:
        action = input("Choose an action: (c) click, (u) upgrade, (q) quit: ").lower()

        if action == "c":
            click()
        elif action == "u":
            upgrade_click_power()
        elif action == "q":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action. Try again.")

# Run the game:
endless_clicker()
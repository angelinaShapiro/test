import random
import time

def dating_sim():
    """
    Simple text-based dating simulator.
    """

    player_name = input("Enter your name: ")

    # List of potential partners
    partners = [
        {"name": "Aiko", "trait": "Intelligent", "interest": "Programming", "flirt_success": 0.7},
        {"name": "Kenji", "trait": "Athletic", "interest": "Sports", "flirt_success": 0.6},
        {"name": "Sakura", "trait": "Artistic", "interest": "Painting", "flirt_success": 0.8},
        {"name": "Hiroshi", "trait": "Kind", "interest": "Reading", "flirt_success": 0.5}
    ]

    print(f"\nWelcome, {player_name}, to the Dating Sim!")
    print("Your goal: Find love!")

    chosen_partner = random.choice(partners)
    print(f"\nYou met {chosen_partner['name']}! They are {chosen_partner['trait']} and interested in {chosen_partner['interest']}.")

    relationship_level = 0  # Start at 0

    while relationship_level < 5:  # 5 is the "dating" stage
        print(f"\n--- Dating {chosen_partner['name']} (Relationship Level: {relationship_level}) ---")
        print("Choose your action:")
        print("1. Compliment them (small chance of success)")
        print("2. Talk about their interests (moderate chance of success)")
        print("3. Give them a gift (high chance of success, but costs money)")
        print("4. Do nothing (chance to lose relationship points)")

        try:
            action = int(input("Your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if action not in [1, 2, 3, 4]:
            print("Invalid choice. Please select an action from 1 to 4.")
            continue

        # Player's action
        if action == 1:
            if random.random() < chosen_partner['flirt_success'] / 2:
                print(f"{chosen_partner['name']} blushes! You gained a relationship point!")
                relationship_level += 1
            else:
                print(f"{chosen_partner['name']} seems unimpressed...")
                relationship_level -= 1 # Add possibility to lose relationship
        elif action == 2:
            if random.random() < chosen_partner['flirt_success']:
                print(f"{chosen_partner['name']} is engaged in the conversation! You gained a relationship point!")
                relationship_level += 1
            else:
                print(f"{chosen_partner['name']} seems bored...")
                relationship_level -= 1

        elif action == 3:
             if random.random() < 0.9: # high chance of success
                print(f"{chosen_partner['name']} is delighted with your gift! You gained 2 relationship points!")
                relationship_level += 2
             else:
                print(f"{chosen_partner['name']} is not happy with the gift... You didn't choose well!")
                relationship_level -= 2
        elif action == 4:
            if random.random() < 0.3:
                print(f"{chosen_partner['name']} feels neglected... You lost a relationship point!")
                relationship_level -= 1
            else:
                print("You spend some quiet time together.")
        else:
            continue

        #Cap and floor the level
        if relationship_level < 0:
            relationship_level = 0

        if relationship_level >=5:
           print (f"Congratulations {player_name}! You and {chosen_partner['name']} are dating!")
           break

    if relationship_level < 5:
        print (f"Unfortunately, it did not workout between you and {chosen_partner['name']}")

    print("\nGame Over.")

if __name__ == "__main__":
    dating_sim()
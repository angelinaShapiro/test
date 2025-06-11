import random
import time

def slow_print(text, delay=0.03):
    """Prints text character by character with a slight delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def support_program():
    """A program to offer support during difficult moments."""

    # List of uplifting quotes
    quotes = [
        "This too shall pass.",
        "Every cloud has a silver lining.",
        "Even the darkest night will end and the sun will rise.",
        "You are stronger than you think.",
        "Every new day is a chance to start over.",
        "Don't be afraid of change, it often leads to something better.",
        "You deserve happiness.",
        "Believe in yourself, even when no one else does.",
        "Difficulties are opportunities disguised as problems.",
        "Never give up.",
        "You are not alone.",
        "It's important to remember your worth, regardless of external circumstances.",
        "Your mistakes don't define you.",
        "Focus on what you can control.",
        "Small steps still move you forward."
    ]

    # List of reflection prompts
    reflection_prompts = [
        "What good happened today, even if it was hard?",
        "What can you be grateful for right now?",
        "What strengths have helped you cope with difficulties in the past?",
        "What small step can you take to feel better?",
        "What can you let go of to make room for something better?"
    ]

    # List of simple calming practices
    calming_practices = [
        "Take a few deep breaths.",
        "Listen to your favorite music.",
        "Drink a cup of warm tea.",
        "Take a walk outside (if possible).",
        "Give yourself a hug (it works!).",
        "Engage in a favorite activity (drawing, reading, etc.).",
        "Write down everything you're feeling and then tear up the paper."
    ]

    slow_print("Hello! I'm here to support you.")
    slow_print("I'm so sorry you're going through a difficult time. Remember that you're not alone.")

    while True:
        slow_print("\nWhat would you like right now?")
        slow_print("1. Receive an inspiring quote")
        slow_print("2. Reflect on something positive")
        slow_print("3. Calm your nerves")
        slow_print("4. Exit the program")

        choice = input("> ")

        if choice == "1":
            chosen_quote = random.choice(quotes)
            slow_print("\nHere's a quote for you:")
            slow_print(chosen_quote)

        elif choice == "2":
            chosen_prompt = random.choice(reflection_prompts)
            slow_print("\nThink about this:")
            slow_print(chosen_prompt)

        elif choice == "3":
            chosen_practice = random.choice(calming_practices)
            slow_print("\nTry this:")
            slow_print(chosen_practice)

        elif choice == "4":
            slow_print("\nRemember that you can reach out for help at any time.")
            slow_print("Things will get better. Goodbye!")
            break

        else:
            slow_print("\nPlease choose one of the options.")


# Run the program
if __name__ == "__main__":
    support_program()
import random

class StoryGenerator:
    def __init__(self):
        self.characters = ["a brave knight", "a mischievous wizard", "a clever detective", "a friendly dragon", "a mysterious stranger"]
        self.settings = ["in a dark forest", "on a distant planet", "in a bustling city", "in an ancient castle", "by a shimmering lake"]
        self.problems = ["a lost artifact", "a strange disappearance", "a looming threat", "a forgotten secret", "a magical curse"]
        self.resolutions = ["they found a hidden map", "they solved a cryptic riddle", "they confronted the villain", "they learned a valuable lesson", "they discovered a powerful artifact"]

    def generate_story(self):
        character = random.choice(self.characters)
        setting = random.choice(self.settings)
        problem = random.choice(self.problems)
        resolution = random.choice(self.resolutions)

        story = (
            f"Once upon a time, there was {character} {setting}. "
            f"One day, they encountered {problem}. "
            f"After a long journey, {resolution}. "
            f"And they lived happily ever after."
        )

        return story

    def customize_story(self, character=None, setting=None, problem=None, resolution=None):
        """
        Generates a story with custom elements.  If an element is not provided,
        a random one is selected.
        """
        character = character if character else random.choice(self.characters)
        setting = setting if setting else random.choice(self.settings)
        problem = problem if problem else random.choice(self.problems)
        resolution = resolution if resolution else random.choice(self.resolutions)

        story = (
            f"In a realm beyond imagination, {character} {setting}. "
            f"Their peaceful existence was shattered by {problem}. "
            f"With courage and determination, {resolution}, bringing balance back to the world. "
            f"The tale of their bravery will be told for generations to come."
        )

        return story


    def interactive_story(self):
        print("Let's create a story together!")
        character = input("Choose a character (or leave blank for a random one): ")
        setting = input("Choose a setting (or leave blank for a random one): ")
        problem = input("Choose a problem (or leave blank for a random one): ")
        resolution = input("Choose a resolution (or leave blank for a random one): ")

        story = self.customize_story(character, setting, problem, resolution)
        return story


if __name__ == "__main__":
    story_generator = StoryGenerator()

    while True:
        print("\nChoose an option:")
        print("1. Generate a random story")
        print("2. Generate a story with custom elements")
        print("3. Interactive story creation")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nYour story:\n", story_generator.generate_story())
        elif choice == "2":
             print("\nYour customized story:\n", story_generator.customize_story(
                character="a robot",
                setting="on mars",
                problem="a broken circuit",
                resolution="it repaired itself"

            ))
        elif choice == "3":
            print("\nYour interactive story:\n", story_generator.interactive_story())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
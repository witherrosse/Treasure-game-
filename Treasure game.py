def print_intro():
    """Display the game introduction."""
    print("""
 Welcome to Treasure Island.
Your mission is to find the hidden treasure.
    """)


def choose_path():
    """First decision: left or right."""
    choice = input("You're at a crossroad. Where do you want to go? (left/right): ").strip().lower()
    return choice


def choose_action():
    """Second decision: swim or wait."""
    choice = input(
        "You've come to a lake. There is an island in the middle.\n"
        "Do you want to swim or wait for a boat? (swim/wait): "
    ).strip().lower()
    return choice


def choose_door():
    """Final decision: choose a door color."""
    choice = input(
        "You arrive at the island unharmed.\n"
        "There is a house with 3 doors: one red, one yellow, and one blue.\n"
        "Which color do you choose? "
    ).strip().lower()
    return choice


def start_game():
    """Main game logic controller."""
    print_intro()

    if choose_path() != "left":
        print(" You fell into a hole. Game Over.")
        return

    if choose_action() != "wait":
        print(" You were attacked by trout. Game Over.")
        return

    door = choose_door()

    if door == "yellow":
        print(" You found the treasure! You Win!")
    elif door == "red":
        print(" Burned by fire. Game Over.")
    elif door == "blue":
        print(" Eaten by beasts. Game Over.")
    else:
        print(" Invalid choice. Game Over.")


if __name__ == "__main__":
    start_game()
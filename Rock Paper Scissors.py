import random

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

CHOICES = [ROCK, PAPER, SCISSORS]

WINNING_CASES = {
    ROCK: SCISSORS,     # Rock beats Scissors
    SCISSORS: PAPER,    # Scissors beats Paper
    PAPER: ROCK         # Paper beats Rock
}


def get_user_choice():
    """Prompt user for a valid choice."""
    choice = input("Choose rock, paper, or scissors: ").strip().lower()
    if choice not in CHOICES:
        print("❌ Invalid choice.")
        return None
    return choice


def get_computer_choice():
    """Randomly select computer choice."""
    return random.choice(CHOICES)


def determine_winner(user, computer):
    """
    Determine game result.
    Returns: 'win', 'lose', or 'draw'
    """
    if user == computer:
        return "draw"
    if WINNING_CASES[user] == computer:
        return "win"
    return "lose"


def print_result(user, computer, result):
    """Display game result."""
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if result == "win":
        print("🏆 You win!")
    elif result == "lose":
        print("💀 You lose!")
    else:
        print("🤝 It's a draw!")


def start_game():
    """Main game controller."""
    user_choice = get_user_choice()
    if not user_choice:
        return

    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    print_result(user_choice, computer_choice, result)


if __name__ == "__main__":
    start_game()
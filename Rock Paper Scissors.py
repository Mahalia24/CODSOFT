import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Game loop
while True:
    # User Input
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice, please try again.")
        continue  # Restart loop if input is invalid

    # Computer Choice
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")

    # Determine Winner
    result = determine_winner(user_choice, computer_choice)
    print(result)

    # Play Again?
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break


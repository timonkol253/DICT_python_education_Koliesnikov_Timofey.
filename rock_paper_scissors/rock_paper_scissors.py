import random
import os

def get_user_name():
    """Prompts the user for their name and greets them."""
    name = input("Enter your name: ")
    print(f"Hello, {name}")
    return name

def load_user_rating(name):
    """Reads the user's score from the file if it exists."""
    rating = 0
    if os.path.isfile("rating.txt"):
        with open("rating.txt", "r") as file:
            for line in file:
                file_name, score = line.split()
                if file_name == name:
                    rating = int(score)
                    break
    return rating

def get_game_options():
    """Takes a list of game options from the user and validates them."""
    while True:
        user_input = input()
        options = user_input.split(",") if user_input else ["rock", "paper", "scissors"]

        if len(options) < 3:
            print("You must enter at least three options.")
            continue
        if len(options) % 2 == 0:
            print("The number of options must be odd.")
            continue

        print("Okay, let's start")
        return options

def determine_result(player_choice, computer_choice, options):
    """Compares player and computer choices and returns the result."""
    if player_choice == computer_choice:
        return "draw"
    index = options.index(player_choice)
    losing_to = options[index + 1:] + options[:index]
    winning_choices = losing_to[:len(losing_to) // 2]
    if computer_choice in winning_choices:
        return "win"
    return "lose"

def save_rating(name, rating):
    """Updates or adds the user's rating in the file."""
    lines = []
    if os.path.isfile("rating.txt"):
        with open("rating.txt", "r") as file:
            lines = file.readlines()
    updated = False
    with open("rating.txt", "w") as file:
        for line in lines:
            file_name, score = line.split()
            if file_name == name:
                file.write(f"{name} {rating}\n")
                updated = True
            else:
                file.write(line)
        if not updated:
            file.write(f"{name} {rating}\n")

def start_game():
    """Runs the main game logic and handles user input."""
    name = get_user_name()
    rating = load_user_rating(name)
    game_options = get_game_options()

    while True:
        user_choice = input()
        if user_choice == "!exit":
            print("Bye!")
            break
        if user_choice == "!rating":
            print(f"Your rating: {rating}")
            continue
        if user_choice not in game_options:
            print("Invalid input")
            continue

        computer_choice = random.choice(game_options)
        result = determine_result(user_choice, computer_choice, game_options)

        if result == "draw":
            print(f"There is a draw ({computer_choice})")
            rating += 50
        elif result == "win":
            print(f"Well done. The computer chose {computer_choice} and failed")
            rating += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")

    save_rating(name, rating)

if __name__ == "__main__":
    start_game()

# Import random, art, game data
import random
from Art import logo, vs
from GameData import data



def format_data(account):
    """Takes the account data and returns a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

    # Display Art


print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make game repeatable
# Generate a random account
while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()
    # Compare/Check if user is correct

    # Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # Use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #clear()
    print(logo)
    # Give feedback on user guess & Score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"You're wrong. Final score: {score}")

    # Clear screen between rounds
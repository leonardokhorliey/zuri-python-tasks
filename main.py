import random

choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}

def print_choices():
    k = ''
    for i in choices:
        k = k + i + ' for ' + choices[i] + '\n'

    return k


def user_win_decider(user_choice, computer_choice):
    win_cases = ['SP', 'PR', 'RS']

    if user_choice + computer_choice in win_cases:
        return True

    return False



while True:
    user_input = input(f"Please enter a selection:\n {print_choices()}")
    computer_choice = random.choice([i for i in choices])

    try:
        print(f"Player ({choices[user_input]}) : Computer ({choices[computer_choice]})")

        if user_input == computer_choice:
            print("There is a Tie. Play again")
            continue

        print("You won" if user_win_decider(user_input, computer_choice) else "Computer won")
        break

    except KeyError:
        print("You entered an invalid selection. Please try again")
        continue
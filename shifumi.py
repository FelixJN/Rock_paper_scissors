import random

options = ["rock", "paper", "scissors"]
error_message = "Invalid weapon." \
                "Please choose rock, paper or scissors.\n"
wrong_answer = False
want_play_again = True


def player_choices():
    global wrong_answer
    choice_cpu = random.choice(options)
    choice_player = input("Pick your weapon.\n")

    if choice_player == choice_cpu:
        print(f"The computer picked {choice_cpu}.")
        return "It's a draw."
    elif choice_cpu == "rock" and choice_player == "scissors":
        print(f"The computer picked {choice_cpu}.")
        return "Rock > scissors, you lose."
    elif choice_cpu == "rock" and choice_player == "paper":
        print(f"The computer picked {choice_cpu}.")
        return "Paper > rock, you win."
    elif choice_cpu == "paper" and choice_player == "rock":
        print(f"The computer picked {choice_cpu}.")
        return "Paper > rock, you lose."
    elif choice_cpu == "paper" and choice_player == "scissors":
        print(f"The computer picked {choice_cpu}.")
        return "Scissors > paper, you win."
    elif choice_cpu == "scissors" and choice_player == "rock":
        print(f"The computer picked {choice_cpu}.")
        return "Rock > scissors, you win."
    elif choice_cpu == "scissors" and choice_player == "paper":
        print(f"The computer picked {choice_cpu}.")
        return "Scissors > paper, you lose."
    else:
        wrong_answer = True
        return error_message


while want_play_again:
    if not wrong_answer:
        print(player_choices())

        if not wrong_answer:
            play_again_question = input("Play again?\n")

            if play_again_question != "yes":
                want_play_again = False
        else:
            wrong_answer = False
    else:
        wrong_answer = False
        print(player_choices())

else:
    print("\nThanks for playing!")

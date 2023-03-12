from  code import *
balance=deposit()


def choose_game():
    vr = input("Please choose game you want to play:\n"
               "1\t for SPIN THE MACHINE\n"
               "2\t for GUESS THE NUMBER\n"
               "3\t for SPINNING THE CUBE\n"
               "6\t for LUCKY SIX\n"
               "Q\t tp QUIT\n\n")

    if vr == "1":
        main(balance)
    elif vr == "2":
        guess_number(balance)

choose_game()
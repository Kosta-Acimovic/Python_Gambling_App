from login import *


def choose_game(value):
    if value == 1 or value == 2:
        user, pas, balance = login()
        balance = float(balance)
    else:
        balance = deposit()
    vr = 0

    while balance > 0 and vr != "Q":
        vr = input("Please choose game you want to play:\n"
                   "1\t for SPIN THE MACHINE\n"
                   "2\t for GUESS THE NUMBER\n"
                   "3\t to ROLL THE DICE\n"
                   "6\t for LUCKY SIX\n"
                   "Q\t tp QUIT\n\n")
        if vr == "1":
            balance = main(balance)
        elif vr == "2":
            balance = guess_number(balance)
        elif vr == "3":
            balance = roll_dice(balance)
        elif vr == "6":
            balance = lucky_six(balance)
        elif vr == "Q":
            print(f"Your balance after this whole game is {balance}$\n")
            if value != 3:
                chang_balance(user, pas, balance)
                break
        else:
            print("You have entered unexciting value please try again\n")
    if balance <= 0:
        print("You have no more money\n")
        if value != 3:
            chang_balance(user, pas, balance)

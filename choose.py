from login import *
from custom import *


def choose_game(value):
    if value == 1 or value == 2:
        lista = []
        lista = login()
        user = lista[0]
        pas = lista[1]
        balance = lista[2]
        balance=float(balance)

    else:
        balance = deposit()
    vr = 0

    while balance > 0 and vr != "Q":
        vr = input("Please choose game you want to play:\n"
                   "1\t for SPIN THE MACHINE\n"
                   "2\t for GUESS THE NUMBER\n"
                   "3\t to ROLL THE DICE\n"
                   "6\t for LUCKY SIX\n"
                   "S\t for SETTINGS\n"
                   "Q\t to QUIT\n\n")
        if vr == "1":
            balance = main(balance)
        elif vr == "2":
            balance = guess_number(balance)
        elif vr == "3":
            balance = roll_dice(balance)
        elif vr == "6":
            balance = lucky_six(balance)
        elif vr == "S":
            customize(user, pas, balance)
        elif vr == "Q":
            print(f"Your balance after this whole game is {balance}$\n")
            if value != 3:
                chang_balance(user, pas, balance)
                break
        else:
            print("You have entered unexciting value please try again\n")
    while balance <= 0:
        print("You have no more money\n")
        balance = input("Enter how much money you want to deposit:\t")
        balance1=balance.isdigit()
        if not balance1:
            print("Bad value\n"
                  "Goodbye\n")
            break
        balance=int(balance)
        if balance <= 0:
            if value != 3:
                chang_balance(user, pas, balance)
                break
        else:
            choose_game(balance)
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 7,
    "/": 4
}
symbol_value = {
    "A": 50,
    "B": 7,
    "C": 5,
    "D": 3,
    "/": 1
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_spins(rows, cols, symbols):
    all_symbols = []
    for symbol, symbolCount in symbols.items():
        for _ in range(symbolCount):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        curr_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(curr_symbols)
            curr_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()


def deposit():
    while True:
        amount = input("Enter what would you like to deposit?\t$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount


def num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on each line between (1~ " + str(MAX_LINES) + ")?\t")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines


def get_bet():
    while True:
        bet = input(
            "Enter the value you want to bet on each line, between (" + str(MIN_BET) + " ~ " + str(MAX_BET) + ")?\t$")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number")
    return bet


def spin(balance):
    lines = num_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(
                f"\nYou do not have enough to bet that amount, your current balance is: ${balance}"
                f" and minimum balance for this bet is {total_bet}\n")
        else:
            break
    print(f"You are betting {bet}$ on {lines} lines.\n"
          f"Your total bet is equal to: {total_bet}$")
    slots = get_spins(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}$")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet


def main(balance):
    while True:
        print(f"Current balance is {balance}$")
        answer = input("Enter   P to play spin game.\n"
                       "Enter   Q to quit\n")
        if answer == "Q":
            print(f"You left with {balance}$")
            return None
        elif answer == "P":
            balance += spin(balance)
        else:
            print("U pressed bad key, please try again")


def dn_prize(balance):
    print("You have to choose amount of bet, if you win you will get SIX times that amount")
    bet = get_bet()
    bet1 = 6 * bet
    print(f"Every wrong guess costs {bet}$\n"
          f"Win brings you {bet1}$\n")
    lista = []
    for i in range(0, 101):
        lista.append(i)
    value = random.choice(lista)
    vrr = input("\nIf you want to stop playing at any time just press Q\n"
                "PRESS ANY OTHER KEY TO START\n\n")

    vr = 0
    while balance >= 10 and vr != "Q":
        vr = input("Guess the number to win\n")
        if vr == "Q":
            print(f"Your current balance after the game is {balance}$")
            break
        vr1 = vr.isdigit()
        if not vr1:
            while not vr1:
                print("Please enter valid number\n\n")
                vr = input("Guess the number to win\n")
                vr1 = vr.isdigit()
        vr = int(vr)
        if vr == value:
            balance += 80
            print(f"Congratulations you won {bet1}$, now your balance is {balance}$")
            return balance
        else:
            if vr > value:
                balance -= 10
                print(f"Number is lower than value you entered {vr}\n")
            else:
                balance -= 10
                print(f"Number is greater than value you entered {vr}\n")

    return balance


def guess_number(balance):
    while True:
        print(f"Current balance is {balance}$")
        answer = input("Enter   P to play game of guessing numbers.\n"
                       "Enter   Q to quit\n")
        if answer == "Q":
            print(f"You left with {balance}$")
            return None
        elif answer == "P":
            balance = dn_prize(balance)
        else:
            print("U pressed bad key, please try again")





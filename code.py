import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def get_spins(rows, cols, symbols):
    all_symvols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symvols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        curr_symblos = all_symvols[:]
        for _ in range(rows):
            value = random.choice(curr_symblos)
            curr_symblos.remove(value)
            column.append(value)

        columns.append(column)
    return columns
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


def getBet():
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


def main():
    balance = deposit()
    lines = num_of_lines()
    while True:
        bet = getBet()
        total_bet = lines * bet

        if total_bet > balance:
            print(
                f"\nYou do not have enough to bet that amount, your current balance is: ${balance} and minimum balance for this bet is {total_bet}\n")
        else:
            break
    print(f"You are betting {bet}$ on {lines} lines.\n"
          f"Your total bet is equal to: {total_bet}$")


main()

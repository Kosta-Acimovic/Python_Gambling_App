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


def check_value():
    value = input("Enter number between 1 and 48 including both of them, without repeating.\t")
    value1 = value.isdigit()
    value = int(value)
    while not value1 or value < 1 or value > 48:
        print("Please enter number between 1 and 48\n")
        value = check_value()
    return value


def sortGeneralAsc(lista):
    c = 5
    c1 = 0
    while c >= c1:

        n = 5
        n1 = 0
        n2 = n1 + 1
        for _ in lista:
            for _ in lista:
                if n2 <= n:
                    if lista[n1] > lista[n2]:
                        pom = lista[n1]
                        lista[n1] = lista[n2]
                        lista[n2] = pom
                    n2 += 1
                n1 += 1

        c1 += 1
    print(lista)
    return lista


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
    answer = input("Enter Q whenever you want to QUIT\n"
                   "Press any other key to play\n")
    while balance >= 1 and answer != "Q":
        print(f"Current balance is {balance}$")
        answer = input("\nPRESS ANY KEY\n")
        if answer == "Q":
            print(f"You left with {balance}$")
            break
        else:
            balance += spin(balance)
    return balance


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

    while balance >= 10 and vrr != "Q":
        vrr = input("Guess the number to win\n")
        if vrr == "Q":
            print(f"Your current balance after the game is {balance}$")
            return balance, vrr
        vr1 = vrr.isdigit()
        if not vr1:
            while not vr1:
                print("Please enter valid number\n\n")
                vrr = input("Guess the number to win\n")
                vr1 = vrr.isdigit()
        vrr = int(vrr)
        if vrr == value:
            balance += bet1
            print(f"Congratulations you won {bet1}$, now your balance is {balance}$")
            return balance, vrr
        else:
            if vrr > value:
                balance -= 10
                print(f"Number is lower than value you entered {vrr}\n")
            else:
                balance -= bet
                print(f"Number is greater than value you entered {vrr}\n")

    return balance, vrr


def guess_number(balance):
    vr = 0
    while balance > 0 and vr != "Q":
        print(f"Current balance is {balance}$")
        answer = input("Enter   Q to quit\n"
                       "PRESS ANY OTHER KEY TO PLAY\n")
        if answer == "Q":
            print(f"You left with {balance}$")
            break
        else:
            balance, vr = dn_prize(balance)

    return balance


def lucky_six(balance):
    bet = get_bet()
    lista = []
    for i in range(1, 49):
        lista.append(i)
    new_lista = lista[:]
    win_vr = []
    your_vr = []
    for i in range(0, 6):
        value = check_value()
        while your_vr.__contains__(value):
            print(f"You have already entered number {value}")
            value = check_value()
        your_vr.append(value)
    your_vr = sortGeneralAsc(your_vr)

    for i in range(0, 6):
        value = random.choice(new_lista)
        win_vr.append(value)
        new_lista.remove(value)
    win_vr = sortGeneralAsc(win_vr)
    win = 0
    for i in your_vr:
        for j in win_vr:
            if i == j:
                win += 1

    print(f"You have guessed right {win} numbers")
    if win == 0:
        balance -= bet
    if win == 1:
        balance = balance - (0.5 * bet)
    if win == 2:
        balance = balance - (0.25 * bet)
    if win == 3:
        balance = balance
    if win == 4:
        balance += bet
    if win == 5:
        balance = balance + (2.5 * bet)
    else:
        balance = balance + (5 * bet)
    return balance


def roll_dice(balance):
    vr = 0
    while balance > 0 and vr != "Q":
        lista = [1, 2, 3, 4, 5, 6]
        value = random.choice(lista)
        vr = input("Press Q to quite\n"
                   "Press any other key to roll the dice\n\n")

        if vr == "Q":
            print(f"\nYour balance after this game is {balance}")
            break
        else:
            bet = get_bet()
            print(f"You rolled number {value}\n")
            if value == 1:
                balance -= bet
            elif value == 2:
                balance = balance - (0.5 * bet)
            elif value == 3:
                balance = balance - (0.25 * bet)
            elif value == 4:
                balance = balance + (0.25 * bet)
            elif value == 5:
                balance = balance + (0.5 * bet)
            else:
                balance += bet
            print(f"Your new balance is {balance}$\n\n")

    return balance

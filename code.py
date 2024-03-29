import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 3,
    "B": 4,
    "C": 5,
    "D": 6,
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
    if not value1:
        value = 0
    value = int(value)
    while not value1 or value < 1 or value > 48:
        print("Please enter number between 1 and 48\n")
        value = check_value()
        break
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
            amount = float(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.\n")
        else:
            print("Please enter a number.\n")
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
            "Enter the value you want to bet, between (" + str(MIN_BET) + " ~ " + str(MAX_BET) + ")?\t$")
        print("\n")
        if bet.isdigit():
            bet = float(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.\n")
        else:
            print("Please enter a number\n")
    return bet


def get_bet_line():
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
        if balance < 1:
            break
        bet = get_bet_line()
        total_bet = lines * bet

        if total_bet > balance:
            print(
                f"\nYou do not have enough to bet that amount, your current balance is: ${balance}"
                f" and minimum balance for this bet is {total_bet}\n")
            continue
        else:
            print(f"You are betting {bet}$ on {lines} lines.\n"
                  f"Your total bet is equal to: {total_bet}$\n")
            slots = get_spins(ROWS, COLS, symbol_count)
            print_slot_machine(slots)
            winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
            print(f"You won {winnings}$")
            print(f"You won on lines: ", *winning_lines)
            balance = balance + winnings - total_bet
            return balance
    return balance


def main(balance):
    while True:
        print(f"Current balance is {balance}$")
        if balance < 1:
            break
        answer = input("\nPRESS ANY KEY\n")
        if answer == "Q":
            print(f"You left with {balance}$")
            break
        else:
            balance = spin(balance)
    return balance


def dn_prize(balance, bet):
    bet1 = 5 * bet
    print(f"Every wrong guess costs {bet}$\n"
          f"Win brings you {bet1}$\n")
    lista = []
    for i in range(0, 101):
        lista.append(i)
    value = random.choice(lista)
    print("\nIf you want to stop playing at any time just press Q\n")

    while True:
        vrr = input("Guess the number to win between 0 and 100 including both\t")
        if vrr == "Q":
            print(f"Your current balance after the game is {balance}$\n")
            break
        vr1 = vrr.isdigit()
        if not vr1:
            while not vr1:
                print("Please enter valid number\n")
                vrr = input("Guess the number to win\n")
                vr1 = vrr.isdigit()
        vrr = int(vrr)
        if vrr == value:
            balance += bet1
            print(f"Congratulations you won {bet1}$, now your balance is {balance}$\n")
            break
        else:
            if vrr > value:
                balance -= 10
                print(f"Number is lower than value you entered {vrr}\n")
                if balance < bet:
                    break
            else:
                balance -= bet
                print(f"Number is greater than value you entered {vrr}\n")
                if balance < bet:
                    break

    return balance


def guess_number(balance):
    while True:
        if balance < 1:
            print("\nYou don`t have enough money, please deposit some amount to play\n")
            break
        while True:
            bet = get_bet()
            if balance < bet:
                print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
                continue
            else:
                break

        print(f"Current balance is {balance}$\n")
        answer = input("Enter   Q to quit\n"
                       "Any other key to play\n")
        if answer == "Q":
            print(f"Your balance after this game is {balance}$\n")
            break
        else:
            balance = dn_prize(balance, bet)
            if balance == 0:
                print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
                break
    return balance


def lucky_six(balance):
    c = input("If you want to go back press Q\n"
              "Press any other key to play\n")
    if c == "Q":
        print(f"Your balance after this game is {balance}$\n")
        return balance
    while True:
        bet = get_bet()
        if balance < bet:
            print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
            continue
        else:
            break
    lista = []
    for i in range(1, 49):
        lista.append(i)
    new_lista = lista[:]
    win_vr = []
    your_vr = []
    for i in range(0, 6):
        value = check_value()
        while your_vr.__contains__(value):
            print(f"You have already entered number {value}\n")
            value = check_value()
        your_vr.append(value)
    print("\nYour combination is:\n"
          f"{your_vr}\n")

    for i in range(0, 35):
        value = random.choice(new_lista)
        win_vr.append(value)
        new_lista.remove(value)
    print("Winning combination is:\n"
          f"{win_vr}\n")
    win = 0
    for i in your_vr:
        for j in win_vr:
            if i == j:
                win += 1

    print(f"You have guessed right {win} numbers\n")
    if win == 0:
        balance -= bet
    elif win == 1:
        balance = balance - (0.5 * bet)
    elif win == 2:
        balance = balance - (0.25 * bet)
    elif win == 3:
        balance = balance
    elif win == 4:
        balance += bet
    elif win == 5:
        balance = balance + (2.5 * bet)
    else:
        balance = balance + (5 * bet)
    print(f"Your balance after this game is {balance}$\n")
    return balance


def roll_dice(balance):
    while True:
        if balance < 1:
            print("\nYou don`t have enough money, please deposit some amount to play\n")
            break

        lista = [1, 2, 3, 4, 5, 6]
        value = random.choice(lista)
        vr = input("Press Q to quit\n"
                   "Press any other key to roll the dice\n")

        if vr == "Q":
            print(f"\nYour balance after this game is {balance}$\n")
            break
        else:
            bet = get_bet()
            if bet > balance > 0:
                print(f"Please enter another bet, because your current balance is {balance}$ and your bet is {bet}$\n")
                continue
            elif balance < bet and balance < 1:
                return balance

            if balance < 1:
                return balance

            if balance < bet:
                print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
                continue
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
            print(f"Your balance after this game is {balance}$\n")

    return balance


def russian_roulette(balance):
    while True:
        lista = [1, 2, 3, 4, 5, 6]
        value = random.choice(lista)
        if balance < 1:
            print("\nYou don`t have enough money, please deposit some amount to play\n")
            break

        vr = input("\nEnter one out of two options: \n"
                   "1\t to be first\n"
                   "2\t to be second\n"
                   "Q\t to quit\n")
        vr1 = vr.isdigit()
        if vr == "Q":
            print(f"Your balance after this game is {balance}$\n")
            break
        if not vr1:
            print("Please enter one of those two values\n")
            continue
        else:
            vr = int(vr)
            bet = get_bet()
            if balance < bet:
                print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
                continue
            if vr == 1:
                if value % 2 == 1:
                    print(f"You are dead, and bullet number {value} killed you\n")
                    balance -= bet
                    continue
                else:
                    print(f"You are alive, your opponent is dead, bullet number {value} killed him\n")
                    balance += bet
                continue
            elif vr == 2:
                if value % 2 == 0:
                    print(f"You are dead, and bullet number {value} killed you\n")
                    balance -= bet
                    continue
                else:
                    print(f"You are alive, your opponent is dead, bullet number {value} killed him\n")
                    balance += bet
                continue
            else:
                print("Please enter valid number\n")
                continue

    return balance


def check_better_card(vr1, vr2, vr):
    vv1 = "Jack"
    vv2 = "Queen"
    vv3 = "King"
    vv4 = "Ace"
    if vr1 == 11:
        vr1 = vv1
        vr = vr1 + vr2
        return vr
    elif vr1 == 12:
        vr1 = vv2
        vr = vr1 + vr2
        return vr
    elif vr1 == 13:
        vr1 = vv3
        vr = vr1 + vr2
        return vr
    elif vr1 == 14:
        vr1 = vv4
        vr = vr1 + vr2
        return vr
    else:
        return vr


def better_card(balance):
    bet = 0
    while True:
        if balance < 1:
            print("\nYou don`t have enough money, please deposit some amount to play\n")
            break
        while True:
            lista1 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            vr11 = random.choice(lista1)
            vr12 = random.choice(lista1)
            vr111 = str(vr11)
            vr122 = str(vr12)
            lista2 = [" \u2764\ufe0f", " \U0001F340", " \u2666", " \u2663\uFE0F"]
            vr21 = random.choice(lista2)
            vr22 = random.choice(lista2)
            vr1 = vr111 + vr21
            vr2 = vr122 + vr22

            if vr1 == vr2:
                continue
            else:
                break
        if balance < 1:
            print("You don`t have enough money, please deposit some amount to play\n")
            break
        ch = input("Choose which card do you want\n"
                   "1\t for first one\n"
                   "2\t for second one\n"
                   "Q\t to quit\n")

        if ch == "1":

            bet = get_bet()
            if balance < bet:
                print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
                continue

            if vr11 > vr12:
                vr1 = check_better_card(vr11, vr21, vr1)
                vr2 = check_better_card(vr12, vr21, vr2)
                print("\nYour card\t" + vr1 + "\nIs better than enemy card\t" + vr2 + "\n")
                balance += bet
            elif vr11 < vr12:
                vr1 = check_better_card(vr11, vr21, vr1)
                vr2 = check_better_card(vr12, vr21, vr2)
                print("\nEnemy card\t" + vr2 + "\nIs better than your card\t" + vr1 + "\n")
                balance -= bet
            else:
                print("\nThese cards have same value\t" + vr1 + "\t" + vr2 + "\n")
        elif ch == "2":

            bet = get_bet()
            if balance < bet:
                print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
                continue

            if vr12 > vr11:
                vr1 = check_better_card(vr11, vr21, vr1)
                vr2 = check_better_card(vr12, vr21, vr2)
                print("\nYour card\t" + vr2 + "\nIs better than enemy card\t" + vr1 + "\n")
                balance += bet
            elif vr12 < vr11:
                vr1 = check_better_card(vr11, vr21, vr1)
                vr2 = check_better_card(vr12, vr21, vr2)
                print("\nEnemy card\t" + vr1 + "\nIs better than your card\t" + vr2 + "\n")
                balance -= bet
            else:
                print("\nThese cards have same value\t" + vr1 + "\t" + vr2 + "\n")
        elif ch == "Q":
            print(f"Your balance after this game is {balance}$\n")
            break
        if bet > balance > 0:
            print(
                f"Please enter another bet in next game, because your current balance is {balance}$ and your last bet "
                f"is {bet}$\n")
            continue
    return balance


def check_roulette(tr, trc, trn, op, troe, balance, bet1):
    v = 37
    if op == "A":
        v = 38
    for i in trc:
        if tr.__contains__(i):
            if i == "red" or i == "black":
                balance = balance + (0.5 * bet1)
            else:
                balance += bet1
        else:
            balance = balance - (0.5 * bet1)

    for j in troe:
        if tr.__contains__(j):
            balance += bet1
        else:
            balance -= bet1

    for k in trn:
        if tr.__contains__(k):
            balance += bet1
        else:
            balance = balance - ((1 / v) * bet1)

    return balance


def roulette(balance):
    tr = []
    tr1 = []
    trc = []
    trn = []
    troe = []
    while True:
        if balance < 1:
            print("\nYou don`t have enough money, please deposit some amount to play\n")
            break
        ch = input("Do you want to play\n"
                   "Q + Enter to quit\n"
                   "Any other key or/and Enter to play\n")
        if ch == "Q":
            print(f"Your balance is {balance}$\n")
            break
        else:
            bet = get_bet()
            if bet > balance:
                print(f"You have entered {bet}$ while you have {balance}$\n")
                continue
            lista = []
            lista_red = [1, 27, 25, 12, 19, 18, 21, 16, 23, 14, 9, 30, 7, 32, 5, 34, 3, 36]
            lista_black = [10, 29, 8, 31, 6, 33, 4, 35, 2, 28, 26, 11, 20, 17, 22, 15, 24, 13]
            while True:
                op = input("Choose which roulette you want to play\n"
                           "E\t for European\n"
                           "A\t for American\n")
                if op == "E":
                    lista.append(0)
                    break
                elif op == "A":
                    print("Instead having 0 and 00, this roulette will have 0 and 37 (this number will be the same as "
                          "00)\n")
                    lista.append(0)
                    lista.append(37)
                    break
                else:
                    print("Please enter valid option\n")
                    continue
            for i in lista_red:
                lista.append(i)
            for j in lista_black:
                lista.append(j)
            if balance < 1:
                print("You don`t have enough money, please deposit some amount to play\n")
                break
            value = random.choice(lista)
            if lista_black.__contains__(value):
                color = "black"
            elif lista_red.__contains__(value):
                color = "red"
            else:
                color = "green"

            if value % 2 == 0:
                oe = "even"
            else:
                oe = "odd"
            while True:
                r = input("You can choose from multiple choices now:\n"
                          "C\t to bet on COLOR\n"
                          "PO\t to bet on PARITY/ODDITY\n"
                          "N\t to bet on color NUMBER\n"
                          "F\t when you are finished\n")

                if r == "F":
                    break
                elif r == "C":
                    c = input("Choose color you want to bet on\n"
                              "R\t for Red\n"
                              "B\t for Black\n"
                              "G\t for Green\n")
                    if c == "R":
                        if trc.__contains__("red"):
                            print("You can`t chose same option more times\n")
                            continue
                        else:
                            trc.append("red")
                            tr.append("red")
                            print("Your choice is saved\n")
                            continue
                    elif c == "B":
                        if trc.__contains__("black"):
                            print("You can`t chose same option more times\n")
                            continue
                        else:
                            trc.append("black")
                            tr.append("black")
                            print("Your choice is saved\n")
                            continue
                    elif c == "G":
                        if trc.__contains__("green"):
                            print("You can`t chose same option more times\n")
                            continue
                        else:
                            trc.append("green")
                            tr.append("green")
                            print("Your choice is saved\n")
                            continue
                    else:
                        print("Please enter valid option\n")
                        continue
                elif r == "PO":
                    c = input("Choose on what you want to bet on\n"
                              "O\t for Odd number\n"
                              "E\t for Even number\n")
                    if c == "O":
                        if troe.__contains__("odd"):
                            print("You can`t chose same option more times\n")
                            continue
                        else:
                            troe.append("odd")
                            tr.append("odd")
                            print("Your choice is saved\n")
                            continue
                    elif c == "E":
                        if troe.__contains__("even"):
                            print("You can`t chose same option more times\n")
                            continue
                        else:
                            troe.append("even")
                            tr.append("even")
                            print("Your choice is saved\n")
                            continue
                    else:
                        print("Please enter valid option\n")
                        continue
                elif r == "N":
                    c = input("Choose Number you want to bet on\t")
                    c1 = c.isdigit()
                    if not c1:
                        print("Please enter valid number\n")
                        continue
                    else:
                        c = int(c)
                        if c < 0 or c > 37:
                            print("Please enter number between 0 and 37\n")
                            continue
                        else:
                            if trn.__contains__(c):
                                print("You can`t chose same option more times\n")
                                continue
                            else:
                                trn.append(c)
                                tr.append(c)
                                print("Your choice is saved\n")
                                continue
        print(f"Your choices are {tr}\n")
        ka = len(tr)
        bet1 = bet / ka
        tr1.append(value)
        tr1.append(oe)
        tr1.append(color)
        balance = check_roulette(tr1, trc, trn, op, troe, balance, bet1)
        print("Winning combination is:\n"
              f"Winning number is:\t {value}\n"
              f"Number is:\t {oe}\n"
              f"Color of this number is\t {color}\n"
              f"Your balance now is\t {balance}\n")
    return balance


def r_p_s_value(vr):
    if vr == "rock":
        vr = "\U0001FAA8"
    elif vr == "paper":
        vr = "\U0001F4C3"
    else:
        vr = "\U00002702"
    return vr


def r_p_s(balance):
    while True:
        if balance < 1:
            print("\nYou don`t have enough money, please deposit some amount to play\n")
            break
        while True:
            lista = ["rock", "paper", "scissors"]
            vr = random.choice(lista)
            k = r_p_s_value(vr)
            if balance < 1:
                print("You don`t have enough money, please deposit some amount to play\n")
                break
            ch = input("Choose which option do you want\n"
                       "R\t for the ROCK\n"
                       "P\t for the PAPER\n"
                       "S\t for the SCISSORS\n"
                       "Q\t to quit\n")
            if ch == "Q":
                print(f"Your balance after this game is {balance}$\n")
                break
            elif ch == "R":
                bet = get_bet()
                if balance < bet:
                    print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
                    continue
                vr1 = "rock"
                k1 = r_p_s_value(vr1)
                if vr == vr1:
                    print("Match ended as a draw, both contestants chose , " + k + "\n")
                    balance = balance
                    continue
                elif vr == "paper":
                    print("You lost, you have " + k1 + " while your enemy have " + k + "\n")
                    balance -= bet
                    continue
                else:
                    print("You won, you have " + k1 + " while your enemy have " + k + "\n")
                    balance += bet
                    continue
            elif ch == "P":
                bet = get_bet()
                if balance < bet:
                    print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
                    continue
                vr1 = "paper"
                k1 = r_p_s_value(vr1)
                if vr == vr1:
                    print("Match ended as a draw, both contestants chose , " + k + "\n")
                    balance = balance
                    continue
                elif vr == "scissors":
                    print("You lost, you have " + k1 + " while your enemy have " + k + "\n")
                    balance -= bet
                    continue
                else:
                    print("You won, you have " + k1 + " while your enemy have " + k + "\n")
                    balance += bet
                    continue
            elif ch == "S":
                bet = get_bet()
                if balance < bet:
                    print(f"You don`t have enough money, bet is {bet}$ and you have {balance}$\n")
                    continue
                vr1 = "scissors"
                k1 = r_p_s_value(vr1)
                if vr == vr1:
                    print("Match ended as a draw, both contestants draw, " + k + "\n")
                    balance = balance
                    continue
                elif vr == "rock":
                    print("You lost, you have " + k1 + " while your enemy have " + k + "\n")
                    balance -= bet
                    continue
                else:
                    print("You won, you have " + k1 + " while your enemy have " + k + "\n")
                    balance += bet
                    continue
            else:
                print("Please enter a valid option\n")
                continue
        return balance

def poker(balance):
    print("Coming Soon")
    return balance

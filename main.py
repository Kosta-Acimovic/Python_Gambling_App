from choose import *


def gambling():
    while True:
        print("\n\nWelcome to KOSTABET, we hope that you will have great time with us\n\n")
        vr = input("Please type one of the following:\n"
                   "1\t if you already have an account\n"
                   "2\t if you want to create an account\n"
                   "3\t if you want to continue as guest\n"
                   "Q\t to quit\n")
        if vr == "1":
            value = 1
            choose_game(value)
            break
        elif vr == "2":
            value = 2
            sign_up()
            print("From now on you can use your account but please log in now\n")
            choose_game(value)
            break
        elif vr == "3":
            value = 3
            choose_game(value)
            break
        elif vr == "Q":
            break
        else:
            print("Try valid option\n")
            continue


gambling()

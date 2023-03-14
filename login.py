from code import *


def login():
    f = open("login.txt", "r")
    b = 0
    u = ""
    p = ""
    us = input("Please enter your username:\t")
    ps = input("Please enter your password:\t")
    for i in f:
        if i.__contains__(us):
            lista = i.split()
            u = lista[0]
            p = lista[1]
            b = lista[2]
            break
    if u == "" or p == "":
        print("Please try again")
        u, p, b = login()
    f.close()
    if us == u and ps == p:
        b = float(b)
        print(f"Your balance is {b}$\n")
        return u, p, b
    else:
        print("Please try again")
        u, p, b = login()
    return u, p, b


def list_out_of_file():
    f = open("login.txt", "r")
    lista = []
    for i in f:
        if i == "\n" or i == "":
            continue
        k = i.split()
        k = k[0]
        lista.append(k)
    f.close()
    return lista


def chang_balance(u, p, bal):
    vl = "\n"
    f = open("login.txt", "r")
    k = u + " " + p + " "
    lista = []
    bal = float(bal)
    for i in f:
        if i != vl:
            lista.append(i)
    for j in lista:
        if j.__contains__(k):
            lista.remove(j)
            c = k + str(bal) + "\n"
            lista.append(c)
    f.close()
    p = open("login.txt", "w")
    for h in lista:
        p.write(h)
    p.close()


def add_user(st):
    f = open("login.txt", "r")
    lista = []
    for i in f:
        if i == "\n" or i == "":
            continue
        lista.append(i)
    else:
        lista.append(st)
    f.close()
    p = open("login.txt", "w")
    for h in lista:
        p.write(h)
    p.close()


def sign_up():
    dec = "'"
    dec2 = '"'
    balance = 0
    print("Thank you for visiting our app, please make your own account\n"
          "Considering it, you will need specific name, password and to deposit some money\n"
          "Username needs to be at least 6 characters long"
          f"Password need to be at least 8 characters long and you cannot use {dec}, {dec2} or blank space\n"
          "Lastly you need to enter deposit greater than 0$\n")

    lista = list_out_of_file()

    # FOR USERNAME

    while True:
        user = input("Enter what username you want to have\t")
        ds = len(user)
        if lista.__contains__(user):
            print("This username is already taken\n")
            continue
        else:
            if user.__contains__(" ") or user.__contains__(dec) or user.__contains__(dec2):
                print("Error in typing username\n")
                continue
            else:
                if ds < 6:
                    print("Username is too short\n")
                    continue
                else:
                    print("This username is valid\n")
                    break
    # FOR PASSWORD
    while True:
        pas = input("Enter what password you want to have\t")
        d = len(pas)
        if d < 8 or pas.__contains__(dec) or pas.__contains__(dec2) or pas.__contains__(" "):
            print("This password is not valid\n")
            continue
        else:
            balance = deposit()
            break

    st = "\n" + user + " " + pas + " " + str(balance)
    add_user(st)
    print("Your account is set\n")

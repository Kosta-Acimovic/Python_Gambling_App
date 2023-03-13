from login import *


def check_name(lista):
    while True:
        dec = "'"
        dec2 = '"'
        u1 = input("Which username do you want to use\t")
        ds = len(u1)
        if lista.__contains__(u1):
            print("This username is already taken\n")
            continue
        else:
            if u1.__contains__(" ") or u1.__contains__(dec) or u1.__contains__(dec2):
                print("Error in typing username\n")
                continue
            else:
                if ds < 6:
                    print("Username is too short\n")
                    continue
                else:
                    print("This username is valid, change will happen after next log in\n")
                    return u1


def check_pas():
    dec = "'"
    dec2 = '"'
    while True:
        pas = input("Enter what password you want to have\t")
        d = len(pas)
        if d < 8 or pas.__contains__(dec) or pas.__contains__(dec2) or pas.__contains__(" "):
            print("This password is not valid\n")
            continue
        else:
            print("Password is valid\n")
            return pas


def list_txt():
    f = open("login.txt", "r")
    lista = []
    for i in f:
        lista.append(i)
    f.close()
    return lista


def change_name(lista):
    lista1 = login()
    u = lista1[0]
    p = lista1[1]
    bal = lista1[2]
    bal = float(bal)
    u1 = check_name(lista)
    if u == u1:
        print("These usernames are the same\n")
        return
    f = open("login.txt", "r")
    k = u + " " + p + " " + str(bal)
    k1 = u1 + " " + p + " " + str(bal)
    lista = []
    for i in f:
        lista.append(i)
    for j in lista:
        if j.__contains__(k):
            lista.remove(j)
            lista.append(k1)
    f.close()
    p = open("login.txt", "w")
    for h in lista:
        p.write(h)
    p.close()


def change_pas():
    lista1 = login()
    u = lista1[0]
    p = lista1[1]
    bal = lista1[2]
    bal = float(bal)
    p1 = check_pas()

    if p == p1:
        print("These passwords are the same\n")
        return
    f = open("login.txt", "r")
    k = u + " " + p + " " + str(bal)
    k1 = u + " " + p1 + " " + str(bal)
    lista = []
    for i in f:
        lista.append(i)
    for j in lista:
        if j.__contains__(k):
            lista.remove(j)
            lista.append(k1)
    f.close()
    p = open("login.txt", "w")
    for h in lista:
        p.write(h)
    p.close()


def change_bal1():
    lista1 = login()
    u = lista1[0]
    p = lista1[1]
    bal = lista1[2]
    bal = float(bal)
    bal1 = deposit()
    f = open("login.txt", "r")
    k = u + " " + p + " " + str(bal)
    k1 = u + " " + p + " " + str(bal1)
    lista = []
    for i in f:
        lista.append(i)
    for j in lista:
        if j.__contains__(k):
            lista.remove(j)
            lista.append(k1)
    f.close()
    p = open("login.txt", "w")
    for h in lista:
        p.write(h)
    p.close()


def customize():
    lista = list_txt()
    while True:
        ch = input("\n\nEnter what do you want to do?\n"
                   "N\t to change name\n"
                   "P\t to change password\n"
                   "M\t to deposit more money\n"
                   "Q\t to quit\n\n")
        if ch == "N":
            change_name(lista)
            break
        elif ch == "P":
            change_pas()
            break
        elif ch == "M":
            print("M")
            break
        elif ch == "Q":
            break
        else:
            print("Bad value, please try again\n")
            continue

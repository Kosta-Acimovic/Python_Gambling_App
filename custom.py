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
                    print("This username is valid\n")
                    return u1


def list_txt():
    f = open("login.txt", "r")
    lista = []
    for i in f:
        lista.append(i)
    f.close()
    return lista


def change_name(u, p, bal, lista):
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


def customize(u, p, b):
    lista = list_txt()
    st = u + " " + p + " " + str(b)
    print(st)
    while True:
        ch = input("\n\nEnter what do you want to do?\n"
                   "N\t to change name\n"
                   "P\t to change password\n"
                   "M\t to deposit more money\n\n")
        if ch == "N":
            change_name(u, p, b, lista)
            break
        elif ch == "P":
            print("P")
            break
        elif ch == "M":
            print("M")
            break
        elif ch == "Q":
            print("Q")
            break
        else:
            print("Bad value, please try again\n")
            continue

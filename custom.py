def customize(u, p, b):
    st = u + " " + p + " " + str(b)
    print(st)

    ch = input("\n\nEnter what do you want to do?\n"
               "1\t to change name\n"
               "2\t to change password\n"
               "3\t to deposit more money\n\n")
    return u, p, b
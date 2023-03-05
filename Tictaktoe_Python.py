def tictac(p):
    msg = """       {0}   |   {1}   |   {2}   
    ------------------------
       {3}   |   {4}   |   {5}    
    ------------------------
       {6}   |   {7}   |   {8}   
       """.format(*p[1], *p[2], *p[3], *p[4], *p[5], *p[6], *p[7], *p[8], *p[9])
    print(msg)


def win(p):
    if p[1] == p[2] and p[1] == p[3] and p[1] != " ":
        print("Победникот е " + p[1])
        return 42
    elif p[4] == p[5] and p[4] == p[6] and p[4] != " ":
        print("Победникот е " + p[4])
        return 42
    elif p[7] == p[8] and p[7] == p[9] and p[7] != " ":
        print("Победникот е " + p[7])
        return 42
    elif p[1] == p[4] and p[1] == p[7] and p[1] != " ":
        print("Победникот е " + p[1])
        return 42
    elif p[2] == p[5] and p[2] == p[8] and p[2] != " ":
        print("Победникот е " + p[2])
        return 42
    elif p[3] == p[6] and p[3] == p[9] and p[3] != " ":
        print("Победникот е " + p[3])
        return 42
    elif p[1] == p[5] and p[1] == p[9] and p[1] != " ":
        print("Победникот е " + p[1])
        return 42
    elif p[3] == p[5] and p[3] == p[9] and p[3] != " ":
        print("Победникот е " + p[3])
        return 42


def check(x):
    if x.isdigit():
        return True
    return False


print("""   1   |   2   |   3   
------------------------
   4   |   5   |   6    
------------------------
   7   |   8   |   9   """)

count = 0
p = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
while True:
    y = input("Одберете место од 1 до 9\n")
    if check(y):
        x = int(y)
    else:
        print("Не е број!")
        continue
    if x > 9 or x < 1:
        y = input("Бројот што го внесовте не е меѓу 1 и 9!\n")
        if check(y):
            x = int(y)
            continue
        else:
            print("Не е број!")
            continue
    elif p[x] == " ":
        if count % 2 == 0:
            p[x] = 'X'
        elif count % 2 == 1:
            p[x] = 'O'
    else:
        y = input("Местото е веќе зафатено!\nОдберете ново место.\n")
        if check(y):
            x = int(y)
            continue
        else:
            print("Не е број!")
            continue
    tictac(p)
    W = win(p)
    if W == 42:
        break
    if count == 8:
        print("Нема Победник!")
        break
    count += 1
input('Press ENTER to exit')

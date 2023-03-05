def printBoard(spaces):
    print("""       {}   |   {}   |   {}   
    ------------------------
       {}   |   {}   |   {}    
    ------------------------
       {}   |   {}   |   {}   
       """.format(*spaces[0], *spaces[1], *spaces[2], *spaces[3], *spaces[4], *spaces[5], *spaces[6], *spaces[7], *spaces[8]))

def win(spaces):
    if spaces[0] == spaces[1] and spaces[0] == spaces[2] and spaces[0] != " ":
        print("Победникот е " + spaces[0])
        return True
    elif spaces[3] == spaces[4] and spaces[3] == spaces[5] and spaces[3] != " ":
        print("Победникот е " + spaces[3])
        return True
    elif spaces[6] == spaces[7] and spaces[6] == spaces[8] and spaces[6] != " ":
        print("Победникот е " + spaces[6])
        return True
    elif spaces[0] == spaces[3] and spaces[0] == spaces[6] and spaces[0] != " ":
        print("Победникот е " + spaces[0])
        return True
    elif spaces[1] == spaces[4] and spaces[1] == spaces[7] and spaces[1] != " ":
        print("Победникот е " + spaces[1])
        return True
    elif spaces[2] == spaces[5] and spaces[2] == spaces[8] and spaces[2] != " ":
        print("Победникот е " + spaces[2])
        return True
    elif spaces[0] == spaces[4] and spaces[0] == spaces[8] and spaces[0] != " ":
        print("Победникот е " + spaces[0])
        return True
    elif spaces[2] == spaces[4] and spaces[2] == spaces[8] and spaces[2] != " ":
        print("Победникот е " + spaces[2])
        return True
    return False

print("""   1   |   2   |   3   
------------------------
   4   |   5   |   6    
------------------------
   7   |   8   |   9   """)

turn = 'X'
spaces = [" "] * 9
while True:
    print("Одберете место од 1 до 9")
    while True:
        position = input()
        if not position.isdigit():
            print("Не е број!")
            continue
        position = int(position)
        if position > 9 or position < 1:
            print("Бројот што го внесовте не е меѓу 1 и 9!")
            continue
        if spaces[position - 1] == " ":
            if turn.__eq__('X'):
                spaces[position-1] = 'X'
                turn = 'O'
            else:
                spaces[position-1] = 'O'
                turn = 'X'
        else:
            print("Местото е веќе зафатено!\nОдберете ново место.")
            continue
        break
    printBoard(spaces)
    if win(spaces):
        break
    if not spaces.__contains__(" "):
        print("Нема Победник!")
        break
input('Press ENTER to exit')

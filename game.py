
from constants import MENU_COMMANDS, GAME_KEYBOARD, p1points, p2points
from menu import menu

def turn1(message, t):
    key = input(message)  # type '1' to win, d for draw

    while key in MENU_COMMANDS:
        menu(key)
        key = input("Player 1, choose a column between A and G  ")
    if validity1(key, t) is False:  # why 'is' and not '==' ?
        print("False from validity1")
        return False

    t = t + 1
    print("t is ", t)

    if conditions1(key) is True:
        # print("True from conditions1")
        return True

    message_n("2", 2, t)


def turn2(message, t):
    key = input(message)  # type '1' to win, d for draw

    while key in MENU_COMMANDS:
        menu(key)
        key = input("Player 2, choose a column between A and G  ")
    if validity2(key, t) is False:
        return False

    t = t + 1
    print("t is ", t)

    if conditions2(key) is True:
        return True

    message_n("1", 2, t)


def validity1(key, t):
    if key not in GAME_KEYBOARD:
        message_n("1", 4, t)
        return False


def validity2(key, t):
    if key not in GAME_KEYBOARD:
        message_n("2", 4, t)
        return False


def conditions1(key):
    # print(p1points)
    if key == "1":
        # print(p1points)
        # p1points = update_score(p1points)
        victory1()
        return True
    elif key == "d":
        draw("2")
        return True
    # elif key == "q":
    #     return quit_confirm()


def conditions2(key):
    if key == "1":
        update_score(p2points)
        victory2()
        return True
    elif key == "d":
        draw("1")
        return True
    # elif key == "q":
    #     return quit_confirm()


def victory1():
    print("Player 1 has", p1points, "points")
    again = input("Player 1 wins! Play again? y / n  ")
    if again == "y":
        reset("2", 6)
        # message_n("2", 6, 0)
    elif again == "n":
        end()
    else:
        victory1()


def victory2():
    print("Player 2 has", p2points, "points")
    again = input("Player 2 wins! Play again? y / n  ")
    if again == "y":
        reset("1", 6)
        # message_n("1", 6, 0)
    elif again == "n":
        end()
    else:
        victory2()


def draw(n):
    again = input("Draw! play again? y / n  ")
    if again == "y":
        reset(n, 5)
        # message_n(n, 5, 0)
    elif again == "n":
        end()
    else:
        draw(n)


def message_n(n, source, t, column = None):
    if source == 1:
        message = "Player " + n + ", you start. Choose a column between A and G  "
    elif source == 2:
        message = "Player " + n + ", your turn. Choose a column between A and G  "
    elif source == 3:
        message = "Column " + column + "is full, player " + n + ". Try another  "
    elif source == 4:
        message = "Invalid choice, player " + n + ". Choose a column between A and G  "
    elif source == 5:
        message = "That was close! Player " + n + ", choose a column between A and G  "
    elif source == 6:
        message = "Let's beat them this time, player " + n + "! Choose a column between A and G  "
    else:
        message = "Player " + n + ", choose a column between A and G  "

    if n == "1":
        turn1(message, t)
    elif n == "2":
        turn2(message, t)





def update_score(points):  # Victory Points
    points = points + 1
    return points

    #     print(p2points)
    #     print(winner, "in")
    # if winner == 1:
    #     pass  # p1points = p1points + 1
    # elif winner == 2:
    #     pass  # p2points = p2points + 1
    # print(p1points)
    # show_score()  # not necessary



def reset(n, source):
    message_n(n, source, 0)


def start():
    t = 0
    # p1points = 0
    # p2points = 0
    # update_score()
    print()
    print("Welcome to Connect Four!")
    print("The objective of the game is to form a horizontal, vertical, or diagonal line of four of one's own discs.")
    print("GLHF!")
    print()
    message_n("1", 1, t)


def quit_confirm():  # in what file should this function be?
    confirm = input("Are you sure you want to quit? y / n  ")
    if confirm == "y":
        end()
        return True
    elif confirm == "n":
        pass
    else:
        quit_confirm()
      

def end():
    # # print("Bye Bye!")
    # print("XOXO! GG!")
    print()  # remember to change back to original message after testing
    print("!!!BYE!!!")  # remember to change back to original message after testing
    # return True  # maybe remove return True from here?

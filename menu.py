
from constants import MENU_COMMANDS, GAME_KEYBOARD, p1points, p2points


def menu(key, outer = True):

    if outer:
        print("entering menu")

    if key == 'resume':
        print("exiting menu")
        return True

    if key == 'menu':  # if or elif?
        key = input("type 'goal' to show the objective of the game, 'score' to show the score, "
                    "'quit' to quit the game, or 'resume' to resume the game  ")
    elif key == 'goal':
        print("the objective of the game is .... ")
        key = input("type 'resume' to close menu, or 'menu' to show all menu commands  ")
    elif key == 'score':
        print("showing score ....")  # show the score
        key = input("type 'resume' to close menu, or 'menu' to show all menu commands  ")
    elif key == 'quit':
        pass  # print("quitting game ....")  # quit the game
        return True  # remember to fix that
    else:
        key = input("type 'resume' to close menu, or 'menu' to show all menu commands  ")

    menu(key, False)


def show_score(p1points, p2points):
    pass
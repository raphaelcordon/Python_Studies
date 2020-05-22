def losing_message(secrect_word):
    print("You were hanged!")
    print(f'The word was {secrect_word}')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def winning_message():
    print("  Congrats, you win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def draw_hangman(chances):
    print("  _______     ")
    print(" |/      |    ")

    if chances == 8:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if chances == 7:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if chances == 6:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if chances == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if chances == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if chances == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if chances == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    if chances == 1:
        print(" E X T R A   C H A N C E")
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    print(" |            ")
    print("_|___         ")


def blue(head):  # Bold Blue Letters
    return f'\033[1:34m{head}\033[m'


def bold(head):  # Bold Letters
    return f'\033[1:m{head}\033[m'


def red(head):  # Bold Red Letters
    return f'\033[1:31m{head}\033[m'

from Hangman.drawings import losing_message, winning_message, draw_hangman, blue, red, bold
from Hangman.sort_words import intro_e_sort_words


def play():
    secret_word = intro_e_sort_words()

    chances = 9
    list = []  # List of letters in secret word
    list_used = []  # List of letters not in secret word
    for i in range(len(secret_word)):
        list.append('_')

    while True:
        if '_' not in list or chances == 0:  # break 'while' if complete the word
            break
        print(blue(f"You have {red(chances)} {blue('more chances')}"))

        if list_used:
            print(bold(f'Used letters: {red(list_used)}'))

        letter = str(input('   Type a letter: ')).strip().lower()
        while True:
            if letter in list_used or letter in list:
                letter = str(input(f"{red('Repeated letter.')}Type a letter: ")).strip().lower()
            else:
                break

        if letter not in secret_word:
            chances -= 1
            list_used.append(letter)
            print(draw_hangman(chances))
        for i in secret_word:
            cont = 0
            for n, p in enumerate(secret_word):  # Includes letter in list
                if p == letter[0]:
                    list[n] = letter[0]
            cont += 1
        print(bold(list))
    print("End game")
    if '_' not in list:
        winning_message()
    else:
        losing_message(secret_word)


if(__name__ == "__main__"):
    play()

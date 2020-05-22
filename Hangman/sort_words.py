from Hangman.drawings import blue, bold, red
import pandas as pd
from random import randrange


def intro_e_sort_words():
    print(blue("***************************"))
    print(blue("*        Hangman!         *"))
    print(blue("***************************"))

    words = pd.read_excel('hangman_dic.xlsx')
    top_head = list(words.columns)
    random_tip = (randrange(0, len(top_head)))
    tip = words.columns[random_tip]

    secret_word = words[tip][randrange(0, len(words[tip]))]
    print(bold(f'The word has {red(len(secret_word))} letters'))
    print(f'From the word bank: {red(tip)}')
    return secret_word

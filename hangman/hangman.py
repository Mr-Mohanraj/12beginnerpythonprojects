import random
from words import main_words_list
import string


def get_valid_word(words):
    word = random.choice(words)
    while ' ' in word or '_' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid_word(main_words_list)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:

        print('you have used these letters: ', ' '.join(word_letters))

        words_list = [letter if letter in used_letters else '_' for letter in word]
        print('current word is ', ' '.join(words_list))
        user_letter = input('Guess letter : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("please choose other one")
        else:
            print('invalid character')

# print(get_valid_word(words_list))
hangman()

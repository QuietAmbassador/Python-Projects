import random
from words import words # importing the words variable from the python file words.py
import string
def get_valid_word(words):
    word = random.choice(words) # randomly choosese word from the list 'Words'
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()
def hangman():
    chosen_word = get_valid_word(words)
    word_letters = set(chosen_word) # creates set for the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()# what the user has guessed

    lives = 6

    while len(word_letters) > 0 and lives > 0:
    # letters used
        print('You have', lives, 'lives left\n' 'You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in chosen_word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1  # takes away a life if wrong
                print('Wrong answer muahaha, minus one life. ')

        elif user_letter in used_letters:
            print('You have already guess that, dweeb! GO AGAIN!')

        else:
            print('Invalid Character. WTF was that?')

    if lives == 0:
                print('You have lost,loser!', chosen_word)
    else:
        print('You guess the word!? HOW?! I SHALL NOT BE DEFEATED.', chosen_word)

hangman()
from random import randint
welcome = print('Welcome to Dom\'s number guessing game!')
randy_num = randint(1,100)

def number_guesser():
    lives = 10
    while lives > 0:
        user_inp = int(input('Please select a number between 1 and 100!\n'))
        if user_inp > randy_num:
            lives -= 1
            print('That is too high. Try again! You have', lives,'lives remaining.')
        elif user_inp < randy_num:
            lives -=1
            print('That is too low. Try again! You have', lives, 'lives remaining')
        elif user_inp == randy_num:
            print('Wow, you got it right? LIT!')
        if lives == 0:
            print('You are out of lives. Try again next time.')


number_guesser()

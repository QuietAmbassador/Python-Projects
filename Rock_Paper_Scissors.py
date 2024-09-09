import random

def play():
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        computer = random.choice(['r','s','p'])
        if user == computer:
            return 'It\'s a tie'
        if is_win(user, computer):
            return 'You won!'
        if is_lose(computer, user):
                return 'You Lost!'
def is_win(player, opponent):
        # return true if player wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def is_lose(opponent, player):
    #return if play loses
    if (opponent == 'r' and player == 's') or (opponent == 's' and player == 'p') or (opponent == 'p' and player == 'r'):
        return  True

print(play())

while True:
    print(play())


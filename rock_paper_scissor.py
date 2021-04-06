# Rock Paper Scissor

import random

def play():
    
    computer = random.choice(['r', 'p', 's'])
    print(computer)
    user = input("'R' for rock, 'P' for paper, S' for scissor: ")
    
    if user == computer:
        return 'It\'s a draw!'
    
    if is_win(user, computer):
        return 'You Win!'
        
    return 'You Lose!'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    
print(play())
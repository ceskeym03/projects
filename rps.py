import random
def game():
    l =int(input("How many games should it last"))
    game = ['rock','paper','scissors']
    game_log=[]

    for n in range(l):
        x = random.randint(0,2)
        user_input = input("Rock, Paper, Scissors")
        ai = game[x]
        print('You:' ,user_input,'\nComputer:',ai)
        
        if user_input not in game:
            game_log.append('Lose')
        elif user_input == ai:
            game_log.append('Draw')
        elif user_input == 'rock' and ai == 'scissors':
            game_log.append('Win')
        elif user_input == 'rock' and ai == 'paper':
            game_log.append('Lose')
        elif user_input == 'paper' and ai == 'rock':
            game_log.append('Win')
        elif user_input == 'paper' and ai == 'scissors':
            game_log.append('Lose')
        elif user_input == 'scissors' and ai == 'rock':
            game_log.append('Lose')
        elif user_input == 'scissors' and ai == 'paper':
            game_log.append('Win')    
        
    user_wins = game_log.count('Win')
    computer_wins = game_log.count('Lose')

    if user_wins > computer_wins:
        print("\nUser wins overall with", user_wins, "wins", game_log)
    elif computer_wins > user_wins:
        print("\nComputer wins overall with", computer_wins, "wins", game_log)
    elif computer_wins == user_wins:
        print("\nDraw, play again", game_log)
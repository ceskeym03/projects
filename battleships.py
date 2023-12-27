import numpy as np
import random


## Creation of AI's battleship formation
possible_formations=[]
def generate_random_matrix(rows, cols, num_ones):
    # Create a zero matrix of the specified size
    matrix = np.zeros((rows, cols))

    # Generate random indices for the ones
    indices = np.random.choice(np.arange(rows*cols), replace=False, size=num_ones)

    # Place ones at the selected indices
    np.put(matrix, indices, 1)

    return matrix

for n in range(1280):
    possible_formations.append(generate_random_matrix(6,6,6))

    
def number_of_ships(formation):
    number=[]
    for i in range(len(formation)):
        for j in range(len(formation)):
            if formation[i,j] == 1:
                number.append(formation[i,j])
    return len(number)


def game(formation):
    formation 
    r = np.random.randint(0,len(possible_formations))
    ai = possible_formations[r] 
    game_board = np.matrix([['0' for n in range(6)] for k in range(6)])
    
    
    while number_of_ships(ai) != 0 and number_of_ships(formation) != 0:
        x = int(input("What is the preferred row number"))
        y = int(input("What is the preferred column number?"))

        if ai[x-1,y-1] != 0.:
            game_board[x-1,y-1] = 'X'
        if game_board[x-1,y-1] == 'X':
            ai[x-1,y-1] = 0
        else:
            game_board[x-1,y-1] = 'M'
        
        l = random.choice([1,2,3,4,5,6])
        q = random.choice([1,2,3,4,5,6])

        if formation[l-1,q-1] != 0:
            formation[l-1,q-1] = 2
        print("Game board\n", game_board,"\nFormation\n",formation,"\nGuess",x,y,'Computer guess',l,q)
    
    
    if number_of_ships(ai) == 0:
        print("User wins")
    
    elif number_of_ships(formation) == 0:
        print("Computer wins")
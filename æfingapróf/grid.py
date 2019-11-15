# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def display_grid(grid):
    ''' Display the board, printing it one row in each line '''
    for i in range(DIM):
        for j in range(DIM):
            print(grid[i][j], end = " ")
        print()
    print()

def new_position(row,col,move):
    def add(value):
        if value < DIM -1 :
            value += 1
        else:
            value = 0
        return value

    def subtract(value):
        if value > DIM -1:
            value -= 1
        else:
            value = DIM -1
        return value

    if move == RIGHT:
        col = add(col)
    elif move == LEFT:
        col = subtract(col)
    elif move == UP:
        row = subtract(row)
    elif move == DOWN:
        row = add(row)
    
    return row,col

def make_move(grid,row,col,move):
    grid [row][col] = EMPTY
    row,col = new_position(row,col,move)
    grid[row][col] = POSITION
    return row,col

def main():
    row,col = 0,0
    grid = initialize_grid()
    display_grid(grid)
    move = get_move()

    while move != QUIT:
        row,col = make_move(grid,row,col,move)
        display_grid(grid)
        move = get_move()
        


main()


# Skrifið Python forrit sem gerir notanda kleift að spila leikinn "Sliding Puzzle"
# Um er að ræða 4x4 borð þar sem hver reitur (fyrir utan einn) ber númer frá 1 upp í 15. 
# Einn af reitunum er auður og er táknaður með núlli. Upphafsstaðan er lesin inn af lyklaborði, t.d.:

 

# 5 3 13 7 14 10 0 11 1 4 6 8 12 9 2 15

 

# sem táknar þá eftirfarandi upphafsstöðu:

# 5	3	13	7
# 14	10		11
# 1	4	6	8
# 12	9	2	15

# Í sérhverri umferð í leiknum slær notandinn inn eina tölu á bilinu 0-15. Ef talan er 0 þá hættir forritið keyrslu en allar aðrar tölur tákna færslu viðkomandi reits yfir í auða plássið. Ef notandi slær t.d. inn 10 í upphafsstöðunni að ofan þá færist reiturinn merktur 10 í auða plássið til hægri. Næsta staða verður þá:

# 5	3	13	7
# 14		10	11
# 1	4	6	8
# 12	9	2	15

# Ef slegin er inn tala sem getur ekki haft í för með sér færslu á reit (t.d. 5 í upphafsstöðunni) þá skal birta fyrri stöðu óbreytta. Markmið leiksins er að raða tölunum í hækkandi röð, þ.e. að ná eftirfarandi lokastöðu:

# 1	2	3	4
# 5	6	7	8
# 9	10	11	12
# 13	14	15

#  
# English description
# Write a Python program which allows a user to play "Sliding Puzzle" which contains a 4x4 board of numbered tiles from 1-15. One of the cells is empty (denoted by a zero) and does not contain a tile. The initial position is input from the keyboard, for example:


# 5 3 13 7 14 10 0 11 1 4 6 8 12 9 2 15

 

# ... which denotes the following initial position:

# 5	3	13	7
# 14	10		11
# 1	4	6	8
# 12	9	2	15

# In each round of the game, the user inputs a single number in the range 0-15. If the number is 0 the program quits, while all other numbers denote a slide for the given cell into the empty space. For example, if a user inputs 10 in the initial position above then that cell slides into the empty cell to the right. The next position will thus become:

# 5	3	13	7
# 14		10	11
# 1	4	6	8
# 12	9	2	15
 


# If a number is input which cannot be translated into a sliding move (e.g. 5 in the initial position) then the previous position shall be shown unchanged. The purpose of the game is to arrange the numbers in ascending order, i.e. to achieve the following final position:

# 1	2	3	4
# 5	6	7	8
# 9	10	11	12
# 13	14	15
 


# Dæmi um inntak/úttak / Example of input/output:


# 5 3 13 7 14 10 0 11 1 4 6 8 12 9 2 15

# 5       3       13      7
# 14      10              11
# 1       4       6       8
# 12      9       2       15

# 10

# 5       3       13      7
# 14              10      11
# 1       4       6       8
# 12      9       2       15

# 14

# 5       3       13      7
#         14      10      11
# 1       4       6       8
# 12      9       2       15

# 1

# 5       3       13      7
# 1       14      10      11
#         4       6       8
# 12      9       2       15

# 4

# 5       3       13      7
# 1       14      10      11
# 4               6       8
# 12      9       2       15

# 14

# 5       3       13      7
# 1               10      11
# 4       14      6       8
# 12      9       2       15

# 3

# 5               13      7
# 1       3       10      11
# 4       14      6       8
# 12      9       2       15

# 5

#         5       13      7
# 1       3       10      11
# 4       14      6       8
# 12      9       2       15

# 1

# 1       5       13      7
#         3       10      11
# 4       14      6       8
# 12      9       2       15

# 0

# Í dæminu hér að ofan er fyrsta lína inntak (upphafsstaðan) og línur sem samanstanda aðeins af einni tölu
#  eru líka inntak. 
# Annað er úttak. Athugið að dálkastafur (e. tab) er á milli talna þegar staða leiksins er sýnd.

# Athugið/Note: Tvö föll og fastar eru gefnir í "Starter Code" sem þið EIGIÐ að nota 


# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input("Enter the numbers 0-15 in any order: ").split()
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()

def find_zero (puzzle_board):
    for index, line in enumerate(puzzle_board):
        for index_element, element in enumerate(line):
            if element == 0:
                return index,index_element

def find_target(puzzle_board, next_move):
    for index, line in enumerate(puzzle_board):
        for index_element, element in enumerate(line):
            if element == next_move:
                return index,index_element


def move(puzzle_board,next_move):
    zero_x, zero_y = find_zero(puzzle_board)
    target_x , target_y = find_target(puzzle_board, next_move)
    if zero_x == target_x and abs(zero_y - target_y) == 1:
        puzzle_board[zero_x][zero_y] = next_move
        puzzle_board[target_x][target_y] = 0
    elif zero_y == target_y and abs(zero_x - target_x) == 1:
        puzzle_board[zero_x][zero_y] = next_move
        puzzle_board[target_x][target_y] = 0
    display(puzzle_board)
    return puzzle_board


def main():
    the_board = initialize_board()
    display(the_board)
    next_input = int(input("What you gonna move: "))
    while next_input != QUIT:
        move(the_board,next_input)
        next_input = int(input())

main()

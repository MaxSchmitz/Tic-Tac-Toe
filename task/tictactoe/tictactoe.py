
def str_to_board(string):

    spots = list(string)
    #print(spots)
    board = [[],[],[]]
    board[0] = [i for i in spots[:3]]
    board[1] = [i for i in spots[3:6]]
    board[2] = [i for i in spots[6:9]]

    #print(board)
    return board

def new_board():
    rows, cols = (3, 3)
    board = [['_' for i in range(cols)] for j in range(rows)]
    return(board)

def print_board(s):
    #takes a 2D-array and prints out tic tac toe board
    print(f"""
    ---------
    | {s[0][0]} {s[0][1]} {s[0][2]} |
    | {s[1][0]} {s[1][1]} {s[1][2]} |
    | {s[2][0]} {s[2][1]} {s[2][2]} |
    ---------""")
def check_win(board):
    # check if a winning condition exists
    #
    winner = []
    # check rows
    if board[0][0] == board[0][1] == board[0][2] != "_":
        winner += board[0][0]
    if board[1][0] == board[1][1] == board[1][2] != "_":
        winner += board[1][0]
    if board[2][0] == board[2][1] == board[2][2] != "_":
        winner += board[2][0]
    # check columns
    if board[0][0] == board[1][0] == board[2][0] != "_":
        winner += board[0][0]
    if board[0][1] == board[1][1] == board[2][1] != "_":
        winner += board[0][1]
    if board[0][2] == board[1][2] == board[2][2] != "_":
        winner += board[0][2]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "_":
        winner += board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "_":
        winner += board[0][2]
    return winner

def check_draw(board):
    if game_finished(board) and not check_win(board):
        return True
    else:
        return False
    pass

def game_finished(board):
    # Returns True if the game is finished
    # Returns False if game is not finished

    #print(f'{not check_win(s)} check wins')
    #print(f'{"_" in s} underscore in board')
    spaces_remaining = sum(['_' in x for x in board])
    if not check_win(board) and spaces_remaining >= 1:
        return False
    else:
        return True
    pass

def check_impossible(board):
    if len(check_win(board)) > 1:
        return True
    elif abs(board.count('X') - board.count('O')) > 1:
        return True
    else:
        return False
    pass

def find_state(board):
    if check_impossible(board):
        print('Impossible')
    elif check_win(board):
        winner = check_win(board)
        print(f'{winner[0]} wins')
    elif not game_finished(board):
        #print('Game not finished')
        make_move(board)
    elif check_draw(board):
        print('Draw')
    pass

def read_coordinates():
    print("Enter the coordinates: ")
    coord = []
    coord = input()
    coord = coord.split()
    if coord[0].isdigit() and coord[1].isdigit():
        #print(coord[0])
        #print(coord[1])
        if int(coord[0]) in [1, 2, 3] and int(coord[1]) in [1, 2, 3] :
            return coord
        #print(f'coords are {coord}')
        else:
            print('Coordinates should be from 1 to 3!')
            pass
    else:
        print("You should enter numbers!")
        pass


    #cord_new = [i - 1 for i in coord]
    #print(f' the cords are here{coord}')



def map_coordinates(coordinates):
    #maps user entered coordinates to proper index
    #eg input: 1 1 maps to 2 0
    # 1 3 maps to 0 0
    # 3 1 maps to 2 2
    # 3 2 maps to 1 2
    #print(f'orig: {coordinates}')

    #print(f'split: {coordinates}')
    #print(coordinates[0])
    #print(coordinates[1])

    converted_coordinates = [0, 0]
    converted_coordinates[1] = abs(int(coordinates[0])-1)
    converted_coordinates[0] = abs(int(coordinates[1])-3)
    return converted_coordinates

def make_move(board):
    user_input = read_coordinates()
    while user_input is None:
        user_input = read_coordinates()
    coordinates = map_coordinates(user_input)
    if board[coordinates[0]][coordinates[1]] == '_':
        if turn % 2 == 1:
            board[coordinates[0]][coordinates[1]] = 'X'
        elif turn % 2 == 0:
            board[coordinates[0]][coordinates[1]] = 'O'
    elif board[coordinates[0]][coordinates[1]] in ['X', 'O']:
        print('This cell is occupied! Choose another one!')
        make_move(board)
    return board

def menu():
    print('welcome to tictactoe')
    print('1:new game, 2:quit, 3:existing game')
    choice = int(input())
    if choice == 1:
        my_board = new_board()
        print_board(my_board)
        find_state(my_board)
    elif choice== 2:
        print('thanks for playing')
        exit()
    elif choice == 3:
        print('enter position like X_X_O____')
        starting_board = input()
        my_board = str_to_board(starting_board)
        print_board(my_board)
        find_state(my_board)
    else:
        print('please select 1,2,or3')
        menu()
    pass

def game(board):
    print_board(board)
    find_state(board)

    #print_board(board)
    #move = map_coordinates(read_coordinates())
    pass

new_game = new_board()
turn = 1
#print(check_win(new_game) == [])
while not game_finished(new_game):
    #print(turn)
    game(new_game)
    turn += 1
print_board(new_game)
find_state(new_game)
#coord = input()
#coord = coord.split()
#print(int(coord[0]) in [1, 2, 3])
#print(int(coord[1]) in [1, 2, 3])

#print(read_coordinates())
#start = new_board()
#print(start)
#print_board(start)
#input = str_to_board('X_X_O____')
#cord = '3 2'
#print(map_coordinates(cord))
#print(f'input:  {input}')
#print(f'not check_win: {not check_win(input)}')
#print(f'game is finished?: {game_finished(input)}')

#print(f"spaces in board: {sum(['_' in x for x in input]) >= 1}")

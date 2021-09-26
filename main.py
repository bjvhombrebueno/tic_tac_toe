# write your code here
def print_board(cells):
    #cells.split()
    print("")
    print("---------")
    print("| "+cells[0]+" "+cells[1]+" "+cells[2]+" |")
    print("| "+cells[3]+" "+cells[4]+" "+cells[5]+" |")
    print("| "+cells[6]+" "+cells[7]+" "+cells[8]+" |")
    print("---------")


# cells = list(input("Enter cells:"))
#cells = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
cells = ['_', '_', '_','X', 'O', 'X', 'O', 'X', 'O' ]
#cells.split()

player = 'X'
def changeplayer():
    global player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'

print_board(cells)
while(1):



    if ((cells[0] == 'X' and cells[1] == 'X' and cells[2]== 'X') or (cells[3] == 'X' and cells[4] == 'X' and cells[5]== 'X') or (cells[6] == 'X' and cells[7] == 'X' and cells[8]== 'X') or (cells[0] == 'X' and cells[3] == 'X' and cells[6]== 'X') or (cells[1] == 'X' and cells[4] == 'X' and cells[7]== 'X') or (cells[2] == 'X' and cells[5] == 'X' and cells[8]== 'X') or (cells[0] == 'X' and cells[4] == 'X' and cells[8]== 'X') or (cells[2] == 'X' and cells[4] == 'X' and cells[6]== 'X')) and ((cells[0] == 'O' and cells[1] == 'O' and cells[2]== 'O') or (cells[3] == 'O' and cells[4] == 'O' and cells[5]== 'O') or (cells[6] == 'O' and cells[7] == 'O' and cells[8]== 'O') or (cells[0] == 'O' and cells[3] == 'O' and cells[6]== 'O') or (cells[1] == 'O' and cells[4] == 'O' and cells[7]== 'O') or (cells[2] == 'O' and cells[5] == 'O' and cells[8]== 'O') or (cells[0] == 'O' and cells[4] == 'O' and cells[8]== 'O') or (cells[2] == 'O' and cells[4] == 'O' and cells[6]== 'O')):
        print("Impossible")
        break
    elif (cells[0] == 'X' and cells[1] == 'X' and cells[2]== 'X') or (cells[3] == 'X' and cells[4] == 'X' and cells[5]== 'X') or (cells[6] == 'X' and cells[7] == 'X' and cells[8]== 'X') or (cells[0] == 'X' and cells[3] == 'X' and cells[6]== 'X') or (cells[1] == 'X' and cells[4] == 'X' and cells[7]== 'X') or (cells[2] == 'X' and cells[5] == 'X' and cells[8]== 'X') or (cells[0] == 'X' and cells[4] == 'X' and cells[8]== 'X') or (cells[2] == 'X' and cells[4] == 'X' and cells[6]== 'X'):
        print("X wins")
        break
    elif (cells[0] == 'O' and cells[1] == 'O' and cells[2]== 'O') or (cells[3] == 'O' and cells[4] == 'O' and cells[5]== 'O') or (cells[6] == 'O' and cells[7] == 'O' and cells[8]== 'O') or (cells[0] == 'O' and cells[3] == 'O' and cells[6]== 'O') or (cells[1] == 'O' and cells[4] == 'O' and cells[7]== 'O') or (cells[2] == 'O' and cells[5] == 'O' and cells[8]== 'O') or (cells[0] == 'O' and cells[4] == 'O' and cells[8]== 'O') or (cells[2] == 'O' and cells[4] == 'O' and cells[6]== 'O'):
        print("O wins")
        break
    elif ('_' in cells) and (abs(cells.count('X') - cells.count('O')) <= 1):
        # print("Game not finished")
        pass
    elif (abs(cells.count('X') - cells.count('O')) >= 2):
        print("Impossible")
        break
    elif '_' not in cells:
        print("Draw")
        break

    print("Enter the coordinates:")

    move = input().split()
    if move[0].isdigit() and move[1].isdigit() and ('1' <= move[0] <= '3') and ('1' <= move[1] <= '3') :
        if move[0] == '1' and move[1] == '1' and cells[0] == '_':
            cells[0] = player
            changeplayer()
        elif move[0] == '1' and move[1] == '2' and cells[1] == '_':
            cells[1] = player
            changeplayer()
        elif move[0] == '1' and move[1] == '3' and cells[2] == '_':
            cells[2] = player
            changeplayer()
        elif move[0] == '2' and move[1] == '1' and cells[3] == '_':
            cells[3] = player
            changeplayer()
        elif move[0] == '2' and move[1] == '2' and cells[4] == '_':
            cells[4] = player
            changeplayer()
        elif move[0] == '2' and move[1] == '3' and cells[5] == '_':
            cells[5] = player
            changeplayer()
        elif move[0] == '3' and move[1] == '1' and cells[6] == '_':
            cells[6] = player
            changeplayer()
        elif move[0] == '3' and move[1] == '2' and cells[7] == '_':
            cells[7] = player
            changeplayer()
        elif move[0] == '3' and move[1] == '3' and cells[8] == '_':
            cells[8] = player
            changeplayer()
        else:
            print("This cell is occupied! Choose another one!")
    elif (move[0] > '3') or (move[1] > '3') or move[0] == '0' or move[1] == '0':
        print("Coordinates should be from 1 to 3!")
        continue
    else:
        print("You should enter numbers!")
        continue

    print_board(cells)

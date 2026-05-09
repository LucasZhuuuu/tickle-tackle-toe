# tickle tackled my toe
# t t t 
# tung tung tung
# sung sung sung tahur
# t
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1_win = False
player2_win = False

board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

def display():
    # for each row in the board
    print("-" *13)
    for row in board:
        print("| ", end="")
        # for each individual cell in the board
        for cell in row:

            # prints the cell
            # keeps the cells on the same line
            print(cell, end=" | ")
        print()
        print("-" *13)

display()

def check_win(mark):
    for row in board:
        if row[0] == row[1] == row[2] == mark:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True 
    return False

while player1_win == False and player2_win == False:
    print("player 1 choose a square, from 1-9")
    move1 = int(input())

    # check if player inputs number NOT displayed on board
    if move1 < 1 or move1 >9:
        print("Out of range, choose a square form 1-9")
        move1 = int(input())
    else:
        row = (move1 - 1) // 3
        col = (move1 - 1) % 3

        if board[row][col] != " " and board[row][col] not in numbers:
            print("Occupied")
            move1 = int(input())

            row = (move1 - 1) // 3
            col = (move1 - 1) % 3
            board[row][col] = "X"
        else: 
            board[row][col] = "X"

    if check_win("X"):
        print("Player1 wins!")
        display()
        break

    display()

    print("Player 2 moves. 1-9")
    move2 = int(input())

    if move2 < 1 or move2 >9:
        print("Out of range, choose a square form 1-9")
        move2 = int(input())
    else:
        row = (move2 - 1) // 3
        col = (move2 - 1) % 3

        if board[row][col] != " " and board[row][col] not in numbers:
            print("Occupied")
            move2 = int(input())

            row = (move2 - 1) // 3
            col = (move2 - 1) % 3

            board[row][col] = "O"
        else: 
            board[row][col] = "O"
    if check_win("O"):
        print("Player 2 wins!")
        display()
        break
    display()




    


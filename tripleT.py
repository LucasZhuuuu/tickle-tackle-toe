# tungtungtung? nah tic tac toe

# print("Hi what's ur name?")
# name = input()
# print(f"ok hi {name} let's play tic tac toe!")


board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

def display():

    # for each row in the board
    print(" ----" *3)
    for row in board:
        print(" | ", end="")
        # for each individual cell in the board
        for cell in row:

            # prints the cell
            # keeps the cells on the same line
            print(cell, end=" | ")
        print()
        print(" ----" *3)


display()

# print("Choose a square")
# move = input()




    


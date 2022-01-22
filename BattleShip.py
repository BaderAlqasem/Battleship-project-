from random import randint

print("Note: row and column start at 0. Top left coordinate is (0, 0)")
print("You have eight guesses. Good luck.")

board = []

for x in range(0, 5):
    board.append(["O"] * 5)
    
def addBoard(board):
    for row in board:
        print(" ".join(row))
        
addBoard(board)

def randRow(board):
    return randint(0, len(board) - 1)

def randCol(board):
    return randint(0, len(board [0]) - 1)

shipRow = randRow(board)
shipCol = randCol(board)

for yourTurn in range (9):
    print("Turn: ", yourTurn + 1)
    guessRow = int(input("Guess Row: "))
    guessCol = int(input("Guess Col: "))
    if guessRow == shipRow and guessCol == shipCol:
        print("You Sank my Battleship!")
        break
    else:
        if guessRow not in range(5) or guessCol not in range(5):
            print("Coordinates inaccessible")
            
        elif board[guessRow][guessCol] == "X":
            print("Coordinates Already Guessed")
        else:
            print("Incorrect Guess")
            board[guessRow][guessCol] = "X"
        if yourTurn == 7:
            print("Game over")
            print("Correct coordinate were: ", shipRow, ",", shipCol)
            break
        addBoard(board)

from random import randint

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
  return randint(0, len(board[0]) - 1)

shipRow = randRow(board)
shipCol = randCol(board)

for yourTurn in range(9):
  print("Turn: ", yourTurn + 1)
  guessRow = int(input("Guess Row: "))
  guessCol = int(input("Guess Col: "))

  if guessRow == shipRow and guessCol == shipCol:
    print("Congratulations! You sank my battleship!")
    break
  else:
    if guessRow not in range(5) or \
      guessCol not in range(5):
      print("Oops, that's not even in the ocean.")
    elif board[guessRow][guessCol] == "X":
      print( "You guessed that one already." )

    else:
      print("You missed my battleship!")
      board[guessRow][guessCol] = "X"
      if yourTurn == 7:
        print("Game Over")
        print("The correct corrdinates were:")
        print(shipRow)
        print(shipCol)
        break
    addBoard(board)

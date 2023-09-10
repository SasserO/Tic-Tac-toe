board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

currentPlayer = 'X'

winner = None

gameRunning = True



# print board
def printBoard(board):
  print(board[0] + ' | ' + board[1] + ' | ' + board[2])
  print(board[3] + ' | ' + board[4] + ' | ' + board[5])
  print(board[6] + ' | ' + board[7] + ' | ' + board[8])

# take player input
def playerInput(board):
  global currentPlayer
  inp = int(input('Choose a number from 1 - 9: '))
  if inp >= 1 and inp <= 9 and board[inp-1] == '-':
    board[inp - 1] = currentPlayer
  else:
    print('Oops! Please make a valid move.')
    currentPlayer = 'X'


# check for win or tie
def checkHorizontal(board):
  global winner
  if board[0] == board[1] == board[2] and board[1] != '-':
    winner = board[0]
    return True 
  elif board[3] == board[4] == board[5] and board[4] != '-':
    winner = board[3]
    return True
  elif board[6] == board[7] == board[8] and board[6] != '-':
    winner = board[6]
    return True
  else:
    winner = None
    return False
  
def checkVertical(board):
  global winner
  if board[0] == board[3] == board[6] and board[3] != '-':
    winner = board[0]
    return True
  elif board[1] == board[4] == board[7] and board[4] != '-':
    winner = board[1]
    return True
  elif board[2] == board[5] == board[8] and board[5] != '-':
    winner = board[5]
    return True
  else:
    winner = None
    return False
  
def checkDiagonal(board):
  global winner
  if board[0] == board[4] == board[8] and board[4] != '-':
    winner = board[0]
    return True
  elif board[2] == board[4] == board[6] and board[4] != '-':
    winner = board[2]
    return True
  else:
    winner = None
    return False

def checkTie(board):
  global gameRunning
  global winner
  if '-' not in board and winner == False:
    printBoard(board)
    print("It's a tie!")
    gameRunning = False

def checkWin():
  global gameRunning
  if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
    printBoard(board)
    print(f'The winner is {winner}!')
    gameRunning = False

  
# switch player
def switchPlayer():
  global currentPlayer
  if currentPlayer == 'O':
    currentPlayer = 'X'
  else:
    currentPlayer = 'O'


# check for win or tie again
while gameRunning:
  printBoard(board)
  playerInput(board)
  checkWin()
  checkTie(board)
  switchPlayer()


from random import randrange

def display_board(board):
  print('+','-'*7,'+','-'*7,'+','-'*7,'+',sep='')
  print('|',' '*5,'|',' '*5,'|',' '*5,'|')
  print('|',' ',board[0][0],' ','|',' ',board[0][1],' ','|',' ',board[0][2],' ','|')
  print('|',' '*5,'|',' '*5,'|',' '*5,'|')
  print('+','-'*7,'+','-'*7,'+','-'*7,'+',sep='')
  print('|',' '*5,'|',' '*5,'|',' '*5,'|')
  print('|',' ',board[1][0],' ','|',' ',board[1][1],' ','|',' ',board[1][2],' ','|')
  print('|',' '*5,'|',' '*5,'|',' '*5,'|')
  print('+','-'*7,'+','-'*7,'+','-'*7,'+',sep='')
  print('|',' '*5,'|',' '*5,'|',' '*5,'|')
  print('|',' ',board[2][0],' ','|',' ',board[2][1],' ','|',' ',board[2][2],' ','|')
  print('|',' '*5,'|',' '*5,'|',' '*5,'|')
  print('+','-'*7,'+','-'*7,'+','-'*7,'+',sep='')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
  try: 
    userChoice = int(input('Enter your move: '))
    if userChoice>0 and userChoice<10:
      freeFields = make_list_of_free_fields(board)
      chosenField = match_number_to_field(userChoice) 
      if chosenField in freeFields:
       board[chosenField[0]][chosenField[1]] = 'O'
       return True
      else:
        print('Field Already occupied')
        return False
        
    else :
      print('invalid choice')
      return False
  except:
    print('invalid choice')
    return False



def make_list_of_free_fields(board):
    #The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    arr = []
    for rowIndex, row in enumerate(board):
      for fieldIndex, field in enumerate(row):
        if type(field)==int :
          arr.append((rowIndex, fieldIndex))
    return arr


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if (board[0][0] == board[0][1] == board[0][2]) and (board[0][0] == sign):
      return True 
    elif (board[1][0] == board[1][1] == board[1][2]) and (board[1][0] == sign):
      return True 
    elif (board[2][0] == board[2][1] == board[2][2]) and (board[2][0] == sign):
      return True
    elif (board[0][0] == board[1][0] == board[2][0]) and (board[0][0] == sign):
      return True
    elif (board[0][1] == board[1][1] == board[2][1]) and (board[0][1] == sign):
      return True
    elif (board[0][2] == board[1][2] == board[2][2]) and (board[0][2] == sign):
      return True
    elif (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] == sign):
      return True
    elif (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] == sign):
      return True
    else :
      return False




def draw_move(board):
    # The function draws the computer's move and updates the board.
    computerChoice = randrange(1,10)
    freeFields = make_list_of_free_fields(board)
    chosenField = match_number_to_field(computerChoice) 
    
    while chosenField not in freeFields :
      computerChoice = randrange(1,10)
      freeFields = make_list_of_free_fields(board)
      chosenField = match_number_to_field(computerChoice)
    
    board[chosenField[0]][chosenField[1]] = 'X'
    


def match_number_to_field(number):
  match number:
        case 1:
          return (0,0)
        case 2:
          return (0,1)
        case 3:
          return (0,2)
        case 4:
          return (1,0)
        case 5:
          return (1,1)
        case 6:
          return (1,2)
        case 7:
          return (2,0)
        case 8:
          return (2,1)
        case 9:
          return (2,2)
        case _:
          return None

board = [
  [1,2,3],
  [4,'X',6],
  [7,8,9],
]

display_board(board)

#game loop
while True:

  validMove = enter_move(board)
  if not validMove:
    continue
  display_board(board)
  if victory_for(board, 'O'):
    print('You won!')
    break
  draw_move(board)
  display_board(board)
  if victory_for(board, 'X'):
    print('Computer wins')
    break
  if len(make_list_of_free_fields(board)) == 0:
    print('Its a Tie')
    break
  

  

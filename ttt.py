# This is the function that prints the board. It references the index of spaces to print out the value of the board.
def board(array):
    print("\n")
    for i in range(3):
        print(f"  {array[3*i]} | {array[3*i + 1]} | {array[3*i + 2]}  ")
        if i == 2:
            print("\n")
        else:
            print("-" * 13)

# Here we define the function to replace the value in spaces with an X or an O.
def play(marker, space, spaces, emptySpaces):
    spaces[int(space) - 1] = marker 
    emptySpaces[int(space) - 1] = marker

# Now we define what all occurs during a turn.
def turn(name, spaces, emptySpaces):
   if name == 1:
       marker = 'X'
   elif name == 2:
       marker = 'O'
   print("To see a board with numbers press n\nIf you want to exit press X\n")
   space = input(f"Player {name} where would you like to place your {marker}?\n")
   
   # Here we have input validation.
   if space == 'x':
       exit()
   elif space == 'n':
       board(spaces)
       turn(name)
   elif space in spaces:
       play(marker, space, spaces, emptySpaces)
   else:
       print("Please enter a valid option\n")
       turn(name, spaces, emptySpaces)

# This function defines what to do if a player wins.
def win(name):
   newGame = input(f"Player {name} wins the game!\nWould you like to play again y/n?")
   if newGame == 'y':
      main()
   elif newgame == 'n':
      exit()

# This is a function to check to see if a player won.
def checkWin(name, spaces):
    for i in [0,3,6]:
        if spaces[i] == spaces[i + 1] and spaces[i + 1] == spaces[i + 2]:
           win(name)
    for i in [0,1,2]:
        if spaces[i] == spaces[i + 3] and spaces[i + 3] == spaces[i + 6]:
            win(name)
    if (spaces[2] == spaces[4] and spaces[4] == spaces[6]) or (spaces[0] == spaces[4] and spaces[4] == spaces[8]):
        win(name) 

# This is the main function of the program. Where the plan comes together.
def main():
    spaces = ['1','2','3','4','5','6','7','8','9']
    emptySpaces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    
    board(spaces)
    for player in range(9):
       if (player % 2) == 0:
           name = 1
       elif (player % 2) == 1:
          name = 2
       turn(name, spaces, emptySpaces)
       board(emptySpaces)
       checkWin(name, spaces)

    
main()
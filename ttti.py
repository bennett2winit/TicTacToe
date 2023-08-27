# Here we define the board that will be printed each time the "board" function is called. 
# Additionally there is a board with numbered spaces to visualize the spaces.
spaces = ['1','2','3','4','5','6','7','8','9']
emptySpaces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

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
def play(marker, space):
    spaces[int(space) - 1] = marker 
    emptySpaces[int(space) - 1] = marker

# Now we define what all occurs during a turn.
def turn(player):
   if player == 1:
       marker = 'X'
   elif player == 2:
       marker = 'O'
   space = input(f"Player {player} where would you like to place your {marker}?\n")
   play(marker, space)
   
board(spaces)
turn(2)
board(emptySpaces)

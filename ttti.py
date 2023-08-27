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
   if (player % 2) == 0:
       marker = 'X'
       name = 1
   elif (player % 2) == 1:
       marker = 'O'
       name = 2
   print("To see a board with numbers press n\nIf you want to exit press X\n")
   space = input(f"Player {name} where would you like to place your {marker}?\n")
   
   # Here we have input validation.
   if space == 'x':
       exit()
   elif space == 'n':
       board(spaces)
       turn(player)
   elif space in spaces:
       play(marker, space)
   else:
       print("Please enter a valid option\n")
       turn(player)

# This is the main function of the program. Where the plan comes together.
def main():
    board(spaces)
    for player in range(9):
       turn(player)
       board(emptySpaces)

    
main()

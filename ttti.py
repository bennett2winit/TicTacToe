# Here we define the board that will be printed each time the "board" function is called
spaces = ['1','2','3','4','5','6','7','8','9']

def board():
    for i in range(3):
        print(f"| {spaces[3*i]} | {spaces[3*i + 1]} | {spaces[3*i + 2]} |")
        if i == 2:
            print("\n")
        else:
            print("-" * 13)

# Now we define what all occurs during a turn.
def turn(player):
   if player == 1:
        marker = ' X '
   elif player == 2:
       marker = ' O '
   print(f"Player {player} where would you like to place your {marker}?")

board()
turn(2)

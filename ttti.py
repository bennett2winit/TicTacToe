# Here we define the board that will be printed each time the "board" function is called
urow = [' 1 ', '|', ' 2 ', '|', ' 3 ']
div = '---------------'
mrow = [' 4 ', '|', ' 5 ', '|', ' 6 ']
brow = [' 7 ', '|', ' 8 ','|', ' 9 ']


def board():
    print(*urow)
    print(div)
    print(*mrow)
    print(div)
    print(*brow)

# Now we define what all occurs during a turn.
def turn(player):
   if player == 1:
        marker = ' X '
   elif player == 2:
       marker = ' O '
   print(f"Player {player} where would you like to place your {marker}?")

turn(2)

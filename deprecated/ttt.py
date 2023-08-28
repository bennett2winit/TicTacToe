global urow
urow = ['   ', '|', '   ', '|', '   ']
div = '--------------'
global mrow
mrow = ['   ', '|', '   ', '|', '   ']
global lrow
lrow = ['   ', '|', '   ', '|', '   ']
def board():
    print(*urow)
    print(div)
    print(*mrow)
    print(div)
    print(*lrow)
board()
def p1turn():
    p1row = input("Player 1 which row would you like to place your X? (U)pper, (M)iddle, or (L)ower?\n")
    p1col = input("Player 1 which column would you like to place your X? (1)st, (2)nd, or (3)rd?\n")
    if p1row[0] == 'u' or p1row[0] == 'U':
        global urow
        if p1col == '1' and urow[0] != ' O ' and urow[0] != ' X ':
            urow[0] = ' X '
        elif p1col == '2' and urow[2] != ' O ' and urow[2] != ' X ':
            urow[2] = ' X '
        elif p1col == '3' and urow[4] != ' O ' and urow[2] != ' X ':
            urow[4] = ' X '
        else:
            print('Please use a valid input')
            p1turn()
    elif p1row[0] == 'm' or p1row[0] == 'M':
        global mrow
        if p1col == '1' and mrow[0] != ' O ' and mrow[0] != ' X ':
            mrow[0] = ' X '
        elif p1col == '2' and mrow[2] != ' O ' and mrow[2] != ' X ':
            mrow[2] = ' X '
        elif p1col == '3' and mrow[4] != ' O ' and mrow[4] != ' X ':
            mrow[4] = ' X '
        else:
            print('Please use a valid input')
            p1turn()
    elif p1row[0] == 'l' or p1row[0] == ' L':
        global lrow
        if p1col == '1' and lrow[0] != ' O ' and lrow[0] != ' X ':
            lrow[0] = ' X '
        elif p1col == '2' and lrow[2] != ' O ' and lrow[2] != ' X ':
            lrow[2] = ' X '
        elif p1col == '3' and lrow[4] != ' O ' and lrow[4] != ' X ':
            lrow[4] = ' X '
        else:
            print('Please use a valid input')
            p1turn()

def p2turn():
    p2row = input("Player 2 which row would you like to place your O? (U)pper, (M)iddle, or (L)ower?\n")
    p2col = input("Player 2 which column would you like to place your O? (1)st, (2)nd, or (3)rd?\n")
    if p2row[0] == 'u' or p2row[0] =='U':
        global urow
        if p2col == '1' and urow[0] != ' O ' and urow[0] != ' X ':
            urow[0] = ' O '
        elif p2col == '2' and urow[2] != ' O ' and urow[2] != ' X ':
            urow[2] = ' O '
        elif p2col == '3' and urow[4] != ' O ' and urow[4] != ' X ':
            urow[4] = ' O '
        else:
            print('Please use a valid input')
            p2turn()
    elif p2row[0] == 'm' or p2row[0] == 'M':
        global mrow
        if p2col == '1' and mrow[0] != ' O ' and mrow[0] != ' X ':
            mrow[0] = ' O '
        elif p2col == '2' and mrow[2] != ' O ' and mrow[2] != ' X ':
            mrow[2] = ' O '
        elif p2col == '3' and mrow[4] != ' O ' and mrow[4] != ' X ':
            mrow[4] = ' O '
        else:
            print('Please use a valid input')
            p2turn()
    elif p2row[0] == 'l' or p2row[0] == 'L':
        global lrow
        if p2col == '1' and lrow[0] != ' O ' and lrow[0] != ' X ':
            lrow[0] = ' O '
        elif p2col == '2' and lrow[2] != ' O ' and lrow[2] != ' X ':
            lrow[2] = ' O '
        elif p2col == '3' and lrow[4] != ' O ' and lrow[4] != ' X ':
            lrow[4] = ' O '
        else:
            print('Please use a valid input')
            p2turn()

def round():
    p1turn()
    board()
    p2turn()
    board()
while(True):
    round()
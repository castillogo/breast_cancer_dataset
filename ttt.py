
ttt = [['X', 'O', 'X'],
       ['.', 'X', 'O'],
       ['X', 'O', 'O']]

ttt2 = [['X', 'O', 'X'],
       ['.', 'O', 'O'],
       ['X', 'O', 'O']]


def horizontal(x):
    # for i in range(2):
    if x[0] == 'X':
        if x[1] == 'X':
            if x[2] == 'X':
                print("You win!")
            else:
                print("You lost")
        else:
                print("You lost")
    else:
                print("You lost")

horizontal(ttt2[0])
horizontal(ttt2[1])
horizontal(ttt2[2])


def check_horizontal(tictac, player):
    for row in range(2):
        if tictac[row][0] == tictac[row][1] and tictac[row][0] == tictac[row][2] and tictac[row][0] == player:
            return player

def check_verticals(tictac, player):
    for col in range(2):
        if tictac[0][col] == tictac[1][col] and tictac[0][col] == tictac[2][col] and tictac[0][col] == player:
            return player

def check_diagonals(tictac, player):
    if tictac[0][0] == tictac[1][1] and tictac[0][0] == tictac[2][2] and tictac[0][0] == player:
        return player
    elif tictac[0][2] == tictac[1][1] and tictac[0][2] == tictac[2][0] and tictac[0][2] == player:
        return player

def ticfunc(tictac, player):
    return check_horizontal(tictac, player) \
        or check_verticals(tictac, player) \
        or check_diagonals(tictac, player)


result = ticfunc(ttt2, 'X') or ticfunc(ttt2, 'O')
if result:
    print(f"{result} won")
else:
    print("Tie!")


assert check_horizontal(ttt, 'X') == None
assert check_verticals(ttt, 'X') == None
assert ticfunc(ttt2, 'O') == 'O'

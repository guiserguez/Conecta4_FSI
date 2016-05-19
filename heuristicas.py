
import random
import utils

def memoize(f):
    memo = {}
    def helper(state):
        tupla = tuple(state.board.items())
        if tupla not in memo:
            memo[tupla] = f(state)
        return memo[tupla]
    return helper

def h0(state):
    return random.randint(-1000, 1000)

@memoize
def h1(state):
    if state.utility != 0:
        return utils.infinity*state.utility
    # Legal moves te da los movimientos posibles para ese tablero
    movimientos = legal_moves(state)
    n = 0
    tablero = state.board.copy()

    for move in movimientos:
        n += cuenta_fichas(tablero, move, 'X',(0,1))
        n += cuenta_fichas(tablero, move, 'X', (1,0))
        n += cuenta_fichas(tablero, move, 'X', (1,-1))
        n += cuenta_fichas(tablero, move, 'X', (1,1))

        n -= cuenta_fichas(tablero, move, 'O',(0,1))
        n -= cuenta_fichas(tablero, move, 'O', (1,0))
        n -= cuenta_fichas(tablero, move, 'O', (1,-1))
        n -= cuenta_fichas(tablero, move, 'O', (1,1))
    return n

def cuenta_fichas(board, move, player, (delta_x, delta_y)):
    "Return true if there is a line through move on board for player."
    if player == 'X':
        contrario='O'
    else:
        contrario = 'X'

    x, y = move
    puntuacion = 0
    fichas = 0

    while (board.get((x, y)) == player) or (board.get((x, y)) != contrario):
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
        if board.get((x, y)) == player:
            puntuacion += 3
        else:
            puntuacion += 1
        x, y = x + delta_x, y + delta_y
        fichas +=1
    x, y = move
    while (board.get((x, y)) == player) or (board.get((x, y)) != contrario):
        if x > 7 or x < 0 or y > 6 or y < 0:
            break
        if board.get((x, y)) == player:
            puntuacion += 3
        else:
            puntuacion += 1
        x, y = x - delta_x, y - delta_y
        fichas += 1
    # Because we counted move itself twice
    if fichas-1 < 4:
        return 0
    return puntuacion

def legal_moves(state):
    "Legal moves are any square not yet taken."
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
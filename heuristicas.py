
import random
import utils

def memoize(f):
    memo = {}
    def helper(state,player):
        tupla = tuple(state.board.items())
        if tupla not in memo:
            memo[tupla] = f(state,player)
        return memo[tupla]
    return helper

def h0(state):
    return random.randint(-1000, 1000)

@memoize
def h1(state,player):
    contrario = seleccionaContrario(player)

    if state.utility != 0:
        if player == 'O':
            return -1*utils.infinity * state.utility
        return utils.infinity * state.utility

    movimientos = legal_moves(state)
    n = 0
    tablero = state.board.copy()

    for move in movimientos:
        n = calculaN(contrario, move, n, player, tablero)
    return n


def seleccionaContrario(player):
    if player == 'X':
        contrario = 'O'
    else:
        contrario = 'X'
    return contrario


def calculaN(contrario, move, n, player, tablero):
    n += cuenta_fichas(tablero, move, player, (0, 1))
    n += cuenta_fichas(tablero, move, player, (1, 0))
    n += cuenta_fichas(tablero, move, player, (1, -1))
    n += cuenta_fichas(tablero, move, player, (1, 1))
    n -= cuenta_fichas(tablero, move, contrario, (0, 1))
    n -= cuenta_fichas(tablero, move, contrario, (1, 0))
    n -= cuenta_fichas(tablero, move, contrario, (1, -1))
    n -= cuenta_fichas(tablero, move, contrario, (1, 1))
    return n


def cuenta_fichas(board, move, player, (delta_x, delta_y)):
    contrario = seleccionaContrario(player)

    x, y = move
    puntuacion = 0
    fichas = 0

    fichas, puntuacion = recorrePosicion(board, contrario, delta_x, delta_y, fichas, player, puntuacion, x, y)
    x, y = move
    fichas, puntuacion = recorrePosicion(board, contrario, -delta_x, -delta_y, fichas, player, puntuacion,x,y)

    # Because we counted move itself twice
    if fichas-1 < 4:
        return 0
    # Because we counted move itself twice
    return puntuacion-1


def recorrePosicion(board, contrario, delta_x, delta_y, fichas, player, puntuacion, x, y):
    while (board.get((x, y)) == player) or (board.get((x, y)) != contrario):

        if x >= 8 or x < 1 or y >= 7 or y < 1:
            break
        puntuacion = sumaPuntuacion(board, player, puntuacion, x, y)
        x, y = x + delta_x, y + delta_y
        fichas += 1
    return fichas, puntuacion


def sumaPuntuacion(board, player, puntuacion, x, y):
    if board.get((x, y)) == player:
        puntuacion += 3
    else:
        puntuacion += 1
    return puntuacion


def legal_moves(state):
    "Legal moves are any square not yet taken."
    return [(x, y) for (x, y) in state.moves
            if y == 1 or (x, y - 1) in state.board]
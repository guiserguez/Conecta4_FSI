# coding=utf-8
import games
import heuristicas as h


def normal(player,state):
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        # Maquina = X, jugador = una O

        if player == 'O':
            state = juega_jugador(state)
            player = 'X'
        else:
            state = juega_maquina(player, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break


def juega_jugador(state):
    col_str = raw_input("Movimiento: ")
    coor = int(str(col_str).strip())
    x = coor
    y = -1
    legal_moves = game.legal_moves(state)
    for lm in legal_moves:
        if lm[0] == x:
            y = lm[1]
    state = game.make_move((x, y), state)
    return state


def maquinas(player,state):
    while True:
        print "Jugador a mover:", game.to_move(state)
        game.display(state)

        # Maquina = X, jugador = una O
        # Según Cayetano cuando una heuristica es perfecta debe quedar empate
        if player == 'O':
            state = juega_maquina(player, state)
            player = 'X'
        else:
            state = juega_maquina(player, state)
            player = 'O'
        print "-------------------"
        if game.terminal_test(state):
            game.display(state)
            print "Final de la partida"
            break


def juega_maquina(player, state):
    print "Thinking..."
    move = games.alphabeta_search(state, game, nivel, eval_fn=h.h1, player=player)
    state = game.make_move(move, state)
    return state


print("Introduzca el nivel de dificultad: ")
print("Nivel Fácil: 1")
print("Nivel Medio: 2")
print("Nivel Difícil: 3")
valor = int(input("Nivel deseado:  "))
if valor == 1:
    nivel = 1
elif valor == 2:
    nivel = 2
elif valor == 3:
    nivel = 4
else:
    nivel = 2
    print("Número incorrecto: se ha establecido el nivel intermedio")

print("¿Jugará usted contra la máquina? S/N")
entrada = raw_input("Respuesta: ")
if entrada != "S" and entrada != "N":
    print("La entrada no coincide con ninguna opción. Jugará contra la maquina")
    entrada = "S"
if entrada == "S":
    print("¿Quién empezará a jugar?")
    player = raw_input("¿La máquina (X) o usted (O)?: ")

    if player != 'X' and player != 'O':
        print("El texto introducido no coincide con ninguna opción. "
              "Empezará a jugar la máquina")
        player = 'X'
    game = games.ConnectFour(jugador=player)
    state = game.initial
    normal(player, state)
else:
    game = games.ConnectFour(jugador='X')
    state = game.initial
    maquinas('X', state)

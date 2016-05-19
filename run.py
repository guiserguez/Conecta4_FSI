# coding=utf-8
import games
import heuristicas

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

print("¿Quién empezará a jugar?")
jugador = raw_input("¿La máquina (X) o usted (O)?: ")
player = jugador
if jugador != 'X' and jugador != 'O':
    print("El texto introducido no coincide con ninguna opción. "
          "Empezará a jugar la máquina")
    player = 'X'

game = games.ConnectFour(jugador=player)
state = game.initial

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)

    # Maquina = X, jugador = una O

    if player == 'O':
        col_str = raw_input("Movimiento: ")
        coor = int(str(col_str).strip())
        x = coor
        y = -1
        legal_moves = game.legal_moves(state)
        for lm in legal_moves:
            if lm[0] == x:
                y = lm[1]

        state = game.make_move((x, y), state)
        player = 'X'
    else:
        print "Thinking..."
        move = games.alphabeta_search(state, game,d=nivel ,eval_fn=heuristicas.h1)

        state = game.make_move(move, state)
        player = 'O'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break

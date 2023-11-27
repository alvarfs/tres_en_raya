import os
tablero = [["-", "-", "-"], 
           ["-", "-", "-"], 
           ["-", "-", "-"]]
jugador = "X"
en_partida = True
empate = False

def mostrar_tablero():
    os.system('cls')
    print("  1|2|3")
    cont = 1
    for fila in tablero:
        print(cont, end = "|")
        print('|'.join(fila))
        cont += 1
    print("")

def actualizar_tablero(jugador, coords):
    tablero[coords[0]] [coords[1]] = jugador

def cambiar_turno(jugador):
    if jugador == "X":
        return "O"
    else:
        return "X"

def comprobar_ganador(jugador, tablero):
    n = len(tablero)
    diagonal_principal = 0
    diagonal_secundaria = 0

    for i in range(n):
        fila_ganadora = 0
        columna_ganadora = 0

        for j in range(n):
            if tablero[i][j] == jugador:
                fila_ganadora += 1
            if tablero[j][i] == jugador:
                columna_ganadora += 1

            if i == j and tablero[i][j] == jugador:
                diagonal_principal += 1
            if i + j == n - 1 and tablero[i][j] == jugador:
                diagonal_secundaria += 1

            if fila_ganadora == n or columna_ganadora == n:
                return True

    if diagonal_principal == n or diagonal_secundaria == n:
        return True

    return False

def comprobar_empate(tablero):
    for fila in tablero:
        if "-" in fila:
            return False
    return True

while en_partida:
    mostrar_tablero()
    coordX = int(input(f"Coordenada X para colocar la {jugador}: ")) - 1
    coordY = int(input(f"Coordenada Y para colocar la {jugador}: ")) - 1
    coords = [coordX, coordY]
    print("")

    if tablero[coords[0]] [coords[1]] == "-":
        actualizar_tablero(jugador, coords)
        fin_partida = comprobar_ganador(jugador, tablero)
        if fin_partida:
            en_partida = False
        else:
            empate = comprobar_empate(tablero)
            if empate:
                en_partida = False
                empate = True
            jugador = cambiar_turno(jugador)
        
    else:
        input("Casilla ocupada! ")

mostrar_tablero()
if empate:
    print(f"Empate!!")
else:
    print(f"Gana {jugador}!!!")
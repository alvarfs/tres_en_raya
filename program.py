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
    for row in tablero:
        print(cont, end = "|")
        print('|'.join(row))
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
    for i, row in enumerate(tablero):
        winner_cond = {
            "jugador_row": 0,
            "jugador_col": 0,
            "jugador_diaL": 0,
            "jugador_diaR": 0
        }
        cont = 2
        
        for j, value in enumerate(row):
            if tablero[i][j] == jugador:
                winner_cond["jugador_row"] += 1
            if tablero[j][i] == jugador:
                winner_cond["jugador_col"] += 1
            if tablero[j][j] == jugador:
                winner_cond["jugador_diaL"] += 1
            if tablero[j][cont] == jugador:
                winner_cond["jugador_diaR"] += 1

            check_in = winner_cond.values()
            for cond in check_in:
                if cond == 3:
                    return True
            
            cont -= 1

def comprobar_empate(tablero):
    for row in tablero:
        if "-" in row:
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
        print("Coordenadas ocupadas!")
        print("Prueba con otras.")


mostrar_tablero()
if empate:
    print(f"Empate!!")
else:
    print(f"Gana {jugador}!!!")


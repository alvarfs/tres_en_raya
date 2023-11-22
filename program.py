tablero = [["-", "-", "-"], 
           ["-", "-", "-"], 
           ["-", "-", "-"]]
in_game = True
player = "X"
tie = False

def mostrar_tablero():
    print("  1|2|3")
    cont = 1
    for row in tablero:
        print(cont, end = "|")
        print('|'.join(row))
        cont += 1
    print("")

def update_tablero(player, coords):
    tablero[coords[0]] [coords[1]] = player

def change_turno(player):
    if player == "X":
        return "O"
    else:
        return "X"

def check_winner(player, tablero):
    for i, row in enumerate(tablero):
        winner_cond = {
            "player_row": 0,
            "player_col": 0,
            "player_diaL": 0,
            "player_diaR": 0
        }
        cont = 2
        
        for j, value in enumerate(row):
            if tablero[i][j] == player:
                winner_cond["player_row"] += 1
            if tablero[j][i] == player:
                winner_cond["player_col"] += 1
            if tablero[j][j] == player:
                winner_cond["player_diaL"] += 1
            if tablero[j][cont] == player:
                winner_cond["player_diaR"] += 1

            check_in = winner_cond.values()
            for cond in check_in:
                if cond == 3:
                    return True
            
            cont -= 1
        
        print(winner_cond)

def check_empate(tablero):
    for row in tablero:
        if "-" in row:
            return False
    return True

while in_game:
    mostrar_tablero()
    coordX = int(input(f"Coordenada X para colocar la {player}: ")) - 1
    coordY = int(input(f"Coordenada Y para colocar la {player}: ")) - 1
    coords = [coordX, coordY]
    print("")

    if tablero[coords[0]] [coords[1]] == "-":
        update_tablero(player, coords)
        game_over = check_winner(player, tablero)
        if game_over:
            in_game = False
        else:
            tie = check_empate(tablero)
            if tie:
                in_game = False
                tie = True
            player = change_turno(player)
        
    else:
        print("Coordenadas ocupadas!")
        print("Prueba con otras.")


mostrar_tablero()
if tie:
    print(f"Empate!!")
else:
    print(f"Gana {player}!!!")


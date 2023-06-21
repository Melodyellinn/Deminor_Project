# ----------- TP Démineur ----------- #

# --- Programme de base --- #
import sys
import re


class NotRunningError(Exception):
    pass


class MineSweeper:
    def __init__(self):
        self.is_playing = False

    def new_game(self, grid_size):
        self.is_playing = True
        print(f'La partie commence avec une grille de : {grid_size}')

    def open(self, x, y):
        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")
        print(f"Ouvrir la case {x}, {y}")

    def flag(self, x, y):
        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")
        print(f"Flagger la case {x}, {y}")


ms = MineSweeper()

hauteur = sys.argv[1]
largeur = sys.argv[2]
print("Hauteur de la grille:", hauteur)
print("Largeur de la grille :", largeur)
grid = int(hauteur) * int(largeur)

ms.new_game(grid)

while True:
    input_player = input("Entrez deux chiffres (5 2 ou F 1 3), newgame ou quit : ")
    if not input_player:
        print('Indique quelque chose !')

    if input_player:
        input_player_split = input_player.split(" ")

        if input_player == "newgame":
            ms.new_game(grid)
        elif input_player_split[0] == "newgame" and len(input_player_split) > 1:
            print('test')
            grid = int(input_player_split[1]) * int(input_player_split[2])
            ms.new_game(grid)
        elif input_player == "quit":
            print('Fin de partie')
            break
        else:
            input_player_split = input_player.split(" ")

            if input_player[0] == "F":
                haut = input_player_split[1]
                larg = input_player_split[2]
                try:
                    ms.flag(haut, larg)
                except NotRunningError:
                    print("La partie n'est pas en cours")
            else:
                haut = input_player_split[0]
                larg = input_player_split[1]
                try:
                    ms.open(haut, larg)
                except NotRunningError:
                    print("La partie n'est pas en cours")

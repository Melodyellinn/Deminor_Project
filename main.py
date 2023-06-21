# ----------- TP Démineur ----------- #

# --- Programme de base --- #

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

hauteur = ""
largeur = ""

while hauteur == "":
    hauteur = input("Entrez la hauteur de la grille : ")
    print('Veuillez indiquer un chiffre')

while largeur == "":
    largeur = input("Entrez la largeur de la grille : ")
    print('Veuillez indiquer un chiffre')

grid = int(hauteur) * int(largeur)
ms.new_game(grid)

while True:
    input_player = input("Entrez deux chiffres (5 2 ou F 1 3), newgame ou quit : ")
    if not input_player:
        print('Indique quelque chose !')

    if input_player:
        if input_player == "newgame":
            ms.new_game(grid)
        elif input_player == "quit":
            print('Fin de partie')
            break
        else:
            input_player_split = input_player.split(" ")

            if input_player[0] == "F":
                haut = input_player_split[1]
                larg = input_player_split[2]
                ms.flag(haut, larg)
            else:
                haut = input_player_split[0]
                larg = input_player_split[1]
                ms.open(haut, larg)


# ----------- TP Démineur ----------- #

# --- Programme de base --- #

class NotRunningError(Exception):
    pass


class MineSweeper:
    def __init__(self):
        self.is_playing = False

    def open(self, x, y):
        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")
        print(f"Ouvrir la case {x}, {y}")

    def flag(self, x, y):
        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")
        print(f"Flagger la case {x}, {y}")

    def new_game(self, grid_size):
        self.is_playing = True
        print(f'La partie commence avec une grille de : {grid_size}')


ms = MineSweeper()
hauteur = int(input("Entrez la hauteur de la grille : "))
largeur = int(input("Entrez la largeur de la grille : "))
grid = hauteur * largeur
ms.new_game(grid)

while True:
    input_player = input("Entrez deux chiffres (5 2 ou F 1 3): ")
    if not input_player:
        print('Indique quelque chose !')
    input_player_split = input_player.split(" ")

    if input_player:
        if input_player[0] == "F":
            haut = input_player_split[1]
            larg = input_player_split[2]
            ms.flag(haut, larg)
        else:
            haut = input_player_split[0]
            larg = input_player_split[1]
            ms.open(haut, larg)


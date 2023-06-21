# ----------- TP Démineur ----------- #

# --- Programme de base --- #
import sys
from abc import ABC, abstractmethod


class NotRunningError(Exception):
    pass


class MineSweeper:
    def __init__(self):
        self.is_playing = False

    def new_game(self, grid_size):
        self.is_playing = True
        print(f'La partie commence avec une grille de : {grid_size}')
        new_grid = Grid()

    def open(self, x, y):
        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")
        print(f"Ouvrir la case {x}, {y}")

    def flag(self, x, y):
        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")
        print(f"Flagger la case {x}, {y}")


class Grid:
    pass


class Tile(ABC):
    @abstractmethod
    def __init__(self, _grid, _x, _y, is_open, is_flagged):
        self._grid = _grid
        self._x = _x
        self._y = _y
        self.is_open = is_open
        self.is_flagged = is_flagged

    @abstractmethod
    def __str__(self):
        if self.is_flagged:
            return "F"
        if not self.is_open:
            return "#"
        if self.is_open:
            raise NotImplementedError


class TileMine(Tile):
    def __init__(self, _grid, _x, _y, is_open, is_flagged):
        super().__init__(_grid, _x, _y, is_open, is_flagged)


class TileHint(Tile):
    def __init__(self, _grid, _x, _y, is_open, is_flagged, hint=0):
        super().__init__(_grid, _x, _y, is_open, is_flagged)
        self.hint = hint


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

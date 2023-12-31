# import random
#
# lst = [(0, 0), (0, 1), (0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]
# lst_tuple = [x for x in zip(*[iter(lst)])]
# lst_tuple = random.sample(lst_tuple, 7)
# print(lst_tuple)
#
# type(lst_tuple)
#



# ----------- TP Démineur ----------- #
import re
import sys
from abc import ABC, abstractmethod
from random import sample as sp


class NotRunningError(Exception):
    pass


class MineSweeper:
    def __init__(self):
        self.is_playing = False

    def new_game(self, height, width):
        self.is_playing = True
        print(f'La partie commence avec une grille de : {width} et {height}')
        new_grid = Grid(int(width), int(height))

    def open(self, x, y):
        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")
        print(f"Ouvrir la case {x}, {y}")

    def flag(self, x, y):
        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")
        print(f"Flagger la case {x}, {y}")


class Grid:
    def __init__(self, width, height):
        self._tiles = [[TileHint(self, i, j) for i in range(width)] for j in range(height)]
        self._width = width
        self._height = height

    def _mines_coord(self):
        tiles_coord = [(x, y) for x in range(self._width) for y in range(self._height)]
        percentage = 10
        mine_pc = len(tiles_coord) * percentage // 100
        mines = sp(tiles_coord, mine_pc)
        for x, y in mines:
            self._tiles[y][x] = TileMine(self, x, y)



    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self._mines += 1
    #     if self._mines :
    #         raise StopIteration
    #     return self._mines


class Tile(ABC):
    def __init__(self, _grid, _x, _y):
        self._grid = _grid
        self._x = _x
        self._y = _y
        self.is_open = False
        self.is_flagged = False

    @abstractmethod
    def __str__(self):
        if self.is_flagged:
            return "F"
        if not self.is_open:
            return "#"
        raise NotImplementedError


class TileMine(Tile):
    def __init__(self, _grid, _x, _y):
        super().__init__(_grid, _x, _y)

    def __str__(self):
        if not self.is_open:
            return super().__str__()
        return "O"


class TileHint(Tile):
    def __init__(self, _grid, _x, _y):
        super().__init__(_grid, _x, _y)
        self.hint = 0

    def __str__(self):
        if not self.is_open:
            return super().__str__()
        if self.hint == 0:
            return " "
        return str(self.hint)

    def __iter__(self):
        pass


ms = MineSweeper()

hauteur = sys.argv[1]
largeur = sys.argv[2]

ms.new_game(hauteur, largeur)

while True:
    input_player = input("Entrez deux chiffres (5 2 ou F 1 3), newgame ou quit : ")
    if not input_player:
        print('Indique quelque chose !')

    if input_player:
        if re.match(r'\w', input_player):
            input_player_split = input_player.split(" ")

            if input_player == "newgame":
                ms.new_game(hauteur, largeur)
            elif input_player_split[0] == "newgame" and len(input_player_split) > 1:
                ms.new_game(input_player_split[1], input_player_split[2])
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

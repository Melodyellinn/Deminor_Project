# ----------- TP Démineur ----------- #
import re
import sys
from abc import ABC, abstractmethod
from random import sample


class NotRunningError(Exception):
    pass


class MineSweeper:
    def __init__(self):
        self.is_playing = False
        self.grid = None

    def new_game(self, height, width):
        self.is_playing = True
        print(f'La partie commence avec une grille de : {width} et {height}')
        self.grid = Grid(width, height)

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
        self.width = width
        self.height = height
        mines = self._mines_coord()
        for x, y in mines:
            self._tiles[y][x] = TileMine(self, x, y)

    def _mines_coord(self):
        tiles_coord = [(x, y) for x in range(self.width) for y in range(self.height)]
        percentage = 10
        mine_pc = len(tiles_coord) * percentage // 100
        return sample(tiles_coord, mine_pc)

    def get_tile(self, x, y):
        return self._tiles[y][x]


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
        self._hint = None

    @property
    def hint(self):
        if self._hint is None:
            mines_count = 0
            adjacent_coords = [(self._x + dx, self._y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)]
            for x, y in adjacent_coords:
                if 0 <= x < self._grid.width and 0 <= y < self._grid.height:
                    tile = self._grid.get_tile(x, y)
                    if isinstance(tile, TileMine):
                        mines_count += 1
            self._hint = mines_count
        return self._hint

    def __str__(self):
        if not self.is_open:
            return super().__str__()
        if self.hint == 0:
            return " "
        return str(self.hint)


ms = MineSweeper()

hauteur = int(sys.argv[1])
largeur = int(sys.argv[2])

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
                ms.new_game(int(input_player_split[1]), int(input_player_split[2]))
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

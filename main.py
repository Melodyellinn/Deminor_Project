# ----------- TP Démineur ----------- #
import re
import sys
from abc import ABC, abstractmethod
from random import sample


class NotRunningError(Exception):
    pass


class TileAlreadyOpenError(Exception):
    pass


class FlaggedTileError(Exception):
    pass


class MineSweeper:
    def __init__(self):
        self.is_playing = False
        self.grid = None
        self.remaining = 0
        self.is_mine_open = False

    def new_game(self, height, width):
        self.is_playing = True
        print(f'La partie commence avec une grille de : {width} et {height}')
        self.grid = Grid(width, height)
        self.remaining = width * height

    def open(self, x, y):

        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")

        # if self.is_win() or self.is_lost():
        #     print("001Partie terminée")
        #     return

        try:
            tile = self.grid.get_tile(x, y)
            if isinstance(tile, TileMine):
                self.is_mine_open = True
            self.grid.open_grid(x, y)

            self.remaining -= 1
            print(f"Ouvrir la case {x}, {y}")

            if self.is_lost():
                self.is_playing = False
                print("Une mine ! Dommage, tu as perdu !")
            elif self.is_win():
                self.is_playing = False
                print("Gagné !")
                return

        except IndexError:
            print('On est en dehors de la grille')

    def flag(self, x, y):
        if not self.is_playing:
            raise NotRunningError("Pas de partie en cours")
        try:
            self.grid.toggle_flag(x, y)
        except IndexError:
            print('On est en dehors de la grille')

    def is_win(self):
        if self.remaining == 0 and not self.is_mine_open:
            print('TU AS GAGNE !')
            return True
        return False

    def is_lost(self):
        return self.is_mine_open


class Grid:
    def __init__(self, width, height):
        self._tiles = [[TileHint(self, i, j) for i in range(width)] for j in range(height)]
        self.width = width
        self.height = height
        mines = self._mines_coord()
        for x, y in mines:
            self._tiles[y][x] = TileMine(self, x, y)

    def __str__(self):
        grid_str = " "
        for row in self._tiles:
            row_str = " "
            for t in row:
                row_str += str(t) + " "
            grid_str += row_str.strip() + "\n"
        return grid_str.strip()

    def _mines_coord(self):
        tiles_coord = [(x, y) for x in range(self.width) for y in range(self.height)]
        percentage = 100
        mine_pc = len(tiles_coord) * percentage // 100
        return sample(tiles_coord, mine_pc)

    def get_tile(self, x, y):
        return self._tiles[y][x]

    def open_grid(self, x, y):
        if self.get_tile(x, y).is_open:
            raise TileAlreadyOpenError("C'est déjà ouvert")
        elif self.get_tile(x, y).is_flagged:
            raise FlaggedTileError("C'est déjà flag")
        self._open_full(x, y)

    def toggle_flag(self, x, y):
        if self.get_tile(x, y).is_open:
            raise TileAlreadyOpenError("C'est déjà ouvert")

        if self.get_tile(x, y).is_flagged:
            self.get_tile(x, y).is_flagged = False
            print("La case flag est déflag")
        else:
            self.get_tile(x, y).is_flagged = True
            print(f"Flagger la case {x}, {y}")

    def _open_full(self, x, y):
        if self.get_tile(x, y).is_open:
            return
        self.get_tile(x, y).open()


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

    def open(self):
        self.is_open = True


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
print(ms.grid)

while True:
    input_player = input("Entrez deux chiffres (5 2 ou F 1 3), newgame ou quit : ")
    if not input_player:
        print('Indique quelque chose !')

    if input_player:
        if re.match(r'\w', input_player):
            input_player_split = input_player.split(" ")

            if input_player == "newgame":
                ms.new_game(hauteur, largeur)
                print(ms.grid)
            elif input_player_split[0] == "newgame" and len(input_player_split) > 1:
                hauteur = int(input_player_split[1])
                largeur = int(input_player_split[2])
                ms.new_game(hauteur, largeur)
                print(ms.grid)
            elif input_player == "quit":
                print('Fin de partie')
                break
            else:
                input_player_split = input_player.split(" ")

                if input_player[0] == "F":
                    haut = int(input_player_split[1])
                    larg = int(input_player_split[2])
                    try:
                        ms.flag(haut, larg)
                    except NotRunningError:
                        print("La partie n'est pas en cours")
                    except TileAlreadyOpenError:
                        print("Impossible de flag une case déjà ouverte !")
                else:
                    haut = int(input_player_split[0])
                    larg = int(input_player_split[1])
                    try:
                        ms.open(haut, larg)
                    except NotRunningError:
                        print("La partie n'est pas en cours")
                    except TileAlreadyOpenError:
                        print("La case est déjà ouverte !")

# ----------- TP Démineur ----------- #

# --- Programme de base --- #

# ---- 1 ---- #

# import sys

# file_name = sys.argv[0]
# hauteur = sys.argv[1]
# largeur = sys.argv[2]
# print("Document", sys.argv)
# print("Hauteur :", hauteur)
# print("Largeur :", largeur)

# ---- 2 ---- #

# while True:
#     x = input("Entrez x :")
#     y = input("Entrez y :")

# ---- 3 ---- #

# while True:
#     input_player = input("Entrez deux chiffres (exp : 5 2) :")

#     if input_player[0] == "F":
#         input_player_split = input_player.split(" ")
#         x = input_player_split[1]
#         y = input_player_split[2]
#         print(f"Flagger la case {x}, {y}")
#     else:
#         xy_split = input_player.split(" ")
#         x = xy_split[0]
#         y = xy_split[1]
#         print(f"Ouvrir la case {x}, {y}")

# ---- 4 ---- #

class MineSweeper:
    def open(self, input_player):
        xy_split = input_player.split(" ")
        x = xy_split[0]
        y = xy_split[1]
        print(f"Ouvrir la case {x}, {y}")

    def flag(self, input_player):
        input_player_split = input_player.split(" ")
        x = input_player_split[1]
        y = input_player_split[2]
        print(f"Flagger la case {x}, {y}")


MineSweeper().open("5 2")

MineSweeper().flag("F 5 2")

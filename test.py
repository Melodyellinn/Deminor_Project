import random

lst = [(0, 0), (0, 1), (0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]
lst_tuple = [x for x in zip(*[iter(lst)])]
lst_tuple = random.sample(lst_tuple, 7)
print(lst_tuple)

type(lst_tuple)


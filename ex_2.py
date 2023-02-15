# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов,
# отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

import random
import matplotlib.pyplot as plt
import numpy as np

size = 15

price_house = np.random.randint(3000000, 20000000, size)
square_house = np.random.randint(100, 300, size)
price_metr = [round(price_house[index]/square_house[index])
              for index in range(len(price_house))]


house = ['дом 1',
         'дом 2',
         'дом 3',
         'дом 4',
         'дом 5',
         'дом 6',
         'дом 7',
         'дом 8',
         'дом 9',
         'дом 10',
         'дом 11',
         'дом 12',
         'дом 13',
         'дом 14',
         'дом 15',
         ]

plt.axhline(y=50000, color='r', linestyle='--')
plt.bar(house, price_metr)
# plt.plot(avg_price_metr, 'ro')
plt.show()

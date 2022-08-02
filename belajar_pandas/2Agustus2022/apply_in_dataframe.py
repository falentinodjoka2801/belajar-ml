from pandas import DataFrame, Series, read_csv
import numpy as np

_drinks =   read_csv('http://bit.ly/drinksbycountry')
print(_drinks)

# print(_drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=1))
print(_drinks.loc[:, 'beer_servings':'wine_servings'].apply(np.argmax, axis=1))

#axis = 0 itukan rows ya,
#artinya dari semua baris data itu di cari mana nilai yang paling tinggi per kolomnya

#axis = 1 itukan columns ya,
#artinya dari semua kolom data itu di cari mana nilai yg paling tinggi per barisnya
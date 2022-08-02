from pandas import DataFrame, Series, read_csv

_drinks     =   read_csv('http://bit.ly/drinksbycountry')
print(_drinks)

print(_drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float))
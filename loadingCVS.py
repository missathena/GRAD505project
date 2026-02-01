import pandas as pd
from pandas import DataFrame

pokedexFrame = DataFrame(pd.read_csv("pokemon_combined.csv"))
print(pokedexFrame.columns)
print(pokedexFrame)

typeDamageFrame = DataFrame(pd.read_csv("typeDamage.csv"))
print(typeDamageFrame.columns)
print(typeDamageFrame)
print(typeDamageFrame.iloc[0])
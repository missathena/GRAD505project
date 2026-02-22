#Packages Needed
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Data loading
pokedex = DataFrame(pd.read_csv('pokemon_combined.csv'))
typeDamageNumbers = DataFrame(pd.read_csv('typeDamageNumbers.csv'))
print(typeDamageNumbers.columns)
print(pokedex.columns)

#Hypothesis 1 Regression Analysis
atkStats = DataFrame(pokedex.groupby("Type")['Attack'].mean().round())
print(atkStats)
getsNoDamage = DataFrame(typeDamageNumbers[['Type','Gets No Damage']])
print(getsNoDamage)


#Hypothesis 2 ANOVA


#Hypothesis 3 ANOVA

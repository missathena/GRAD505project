#Packages Needed
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


#Data loading
pokedex = DataFrame(pd.read_csv('pokemon_combined.csv'))
pokedex = pokedex[pokedex.groupby('Type')['Type'].transform('count') >= 5]
pokedex = DataFrame.drop(pokedex,columns=["Abilities","Growth Rate"])
typeDamageNumbers = DataFrame(pd.read_csv('typeDamageNumbers.csv'))
#print(typeDamageNumbers.head())
#print(pokedex.head())

#Hypothesis 1 One Sided t Test
atkStats = DataFrame(pokedex.groupby(by='Type',as_index=False)['Attack'].sum())
atkStats[["Primary","Secondary"]] = atkStats.Type.str.split(expand=True)
atkStats = DataFrame.drop(atkStats, columns='Type')
atkStats = atkStats.groupby(by='Primary',as_index=False)['Attack'].mean().round()
atkStats.rename(columns={'Primary' : 'Type'}, inplace=True)
getsNoDamage = DataFrame(typeDamageNumbers[['Type','Gets No Damage']])
#Combined in CSV
atkStats.to_csv('pokemon_atkStats.csv')
getsNoDamage.to_csv('pokemon_getsNoDamage.csv')

immune_attack = DataFrame(pd.read_csv('immunity_attack.csv'))



#Hypothesis 2 ANOVA
kg_atk_def = DataFrame(pd.read_csv('weight_attack_defense.csv'))

light = kg_atk_def[kg_atk_def['Weight'] <= 150][['Weight','Attack','Defense']]
med = kg_atk_def [250 >= kg_atk_def['Weight']][kg_atk_def['Weight'] > 150][['Weight', 'Attack', 'Defense']]
heavy = kg_atk_def[kg_atk_def['Weight'] > 250 ][['Weight','Attack','Defense']]

'''light.to_csv('pokemon_light.csv')
med.to_csv('pokemon_med.csv')
heavy.to_csv('pokemon_heavy.csv')'''

kg_atk_def = pd.concat(map(pd.read_csv,['pokemon_light.csv','pokemon_med.csv','pokemon_heavy.csv']),ignore_index=True)
kg_atk_def = pd.get_dummies(kg_atk_def,columns=['Weight'],dtype=int)


#Hypothesis 3
stat_totals = DataFrame(pokedex[['Type','Total']])
stat_totals[["Primary","Secondary"]] = stat_totals.Type.str.split(expand=True)
stat_totals = DataFrame.drop(stat_totals,columns="Type")

stat_totals_primaryOnly = stat_totals
stat_totals_primaryOnly = pd.get_dummies(stat_totals_primaryOnly,columns=["Primary"],dtype=int)



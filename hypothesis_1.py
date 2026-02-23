
import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind,probplot

#Data loading
pokedex = DataFrame(pd.read_csv('pokemon_combined.csv'))
pokedex = pokedex[pokedex.groupby('Type')['Type'].transform('count') >= 5]
pokedex = DataFrame.drop(pokedex,columns=["Abilities","Growth Rate"])
typeDamageNumbers = DataFrame(pd.read_csv('typeDamageNumbers.csv'))
#print(typeDamageNumbers.head())
#print(pokedex.head())

#Hypothesis 1 Two Sample t test
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
print(immune_attack)


no_immunity = immune_attack[immune_attack['Gets No Damage'] == 0][['Attack']]
higher_immunity = immune_attack[immune_attack['Gets No Damage'] > 0][['Attack']]

result = ttest_ind(no_immunity,higher_immunity,equal_var=True)
tStat,p_value = ttest_ind(no_immunity,higher_immunity,equal_var=True)
print(f't-statistic:{tStat.round(2)} p-value:{p_value.round(2)}')

sns.histplot(no_immunity,bins=5,kde=True)
plt.title('Histogram of Attack Power for No Immunity')
plt.xlabel('Attack')
plt.show()

sns.histplot(higher_immunity,bins=5,kde=True)
plt.title('Histogram of Attack power for types with Immunity')
plt.xlabel('Attack')
plt.show()


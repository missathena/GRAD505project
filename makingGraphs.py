import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

pokedex = pd.DataFrame(pd.read_csv("pokemon_combined.csv"))
typeDamage = pd.DataFrame(pd.read_csv("typeDamage.csv"))
print(pokedex.columns)
print(typeDamage.columns)

pokedex = pokedex[pokedex.groupby('Type')['Type'].transform('count') >= 10]

topTypes = pd.DataFrame(pokedex["Type"].value_counts())
print(topTypes.head(20).describe())
sns.boxplot(topTypes.head(20))
tyoeDis = sns.barplot(topTypes.head(20), x=None, y='count', hue="Type", palette="pastel")
plt.title("Pokemon Type Distribution")
plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
plt.savefig(fname='dis',bbox_inches='tight')

doubleDamage = typeDamage[['Type','Gives Double Damage','Gives half damage']]
print(tabulate(doubleDamage, headers="keys", tablefmt="rst"))

noDamage = typeDamage[['Type','Gives No Damage', 'Gets No Damage']]
print(tabulate(noDamage, headers="keys", tablefmt="rst"))

typeCounts = pokedex.groupby('Type')['Type'].count().sort_values(ascending=False)
print(typeCounts.to_string())

statTotals = pokedex.groupby('Type')['Total'].describe()
atkStats = pokedex.groupby('Type')['Attack'].count()
print(atkStats)
print(statTotals)


atkVSdefAvg = pokedex[['Type', 'Attack', 'Defense']]
a = sns.barplot(data=atkVSdefAvg,x='Attack',y=atkVSdefAvg['Attack'].values,hue='Type',palette="pastel")
sns.move_legend(a,"lower right",ncol=5,bbox_to_anchor=(1, 1))
plt.savefig(fname='attack',bbox_inches='tight')

ad = sns.scatterplot(data=atkVSdefAvg,x='Attack', y="Defense", hue='Type', palette="bright",marker='s')

sns.move_legend(ad,"lower right",ncol=5,bbox_to_anchor=(1, 1))
plt.savefig(fname='defense',bbox_inches='tight')
spVSspAvg = pokedex[['Type', 'Sp. Atk', 'Sp. Def']].groupby('Type').agg('mean').round(1)
print(spVSspAvg.describe().round())
aa = sns.scatterplot(data=spVSspAvg,x='Sp. Atk', y="Sp. Def", hue='Type')
sns.move_legend(aa,"lower right",ncol=5,bbox_to_anchor=(1, 1))
plt.savefig(fname='spattack',bbox_inches='tight')


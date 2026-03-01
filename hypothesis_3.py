#Packages Needed
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

#Data loading
pokedex = DataFrame(pd.read_csv('pokemon_combined.csv'))
pokedex = pokedex[pokedex.groupby('Type')['Type'].transform('count') >= 5]
pokedex = DataFrame.drop(pokedex,columns=["Abilities","Growth Rate"])
typeDamageNumbers = DataFrame(pd.read_csv('typeDamageNumbers.csv'))

#Hypothesis 3 ANOVA
stat_totals = DataFrame(pokedex[['Type','Total']])
stat_totals[["Primary","Secondary"]] = stat_totals.Type.str.split(expand=True)
stat_totals = DataFrame.drop(stat_totals,columns="Type")

print('Stat Total Avg and Primary Type ANOVA')
mod = ols('Total ~ C(Primary)',data=stat_totals).fit()
print(mod.summary())
anova = anova_lm(mod)
print(anova)

box = sns.boxplot(data=stat_totals,x='Total',y='Primary',hue='Primary')
plt.title('Stat total Avgs for Primary types ')
plt.savefig('boxplot.png',bbox_inches='tight')

